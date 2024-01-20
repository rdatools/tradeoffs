"""
A REDISTRICTING PLAN THAT CAN EASILY & EFFICIENTLY EVOLVE
"""

from typing import (
    Any,
    List,
    Dict,
    Set,
    Tuple,
    TypeAlias,
    NamedTuple,
    TypedDict,
    Optional,
)

import random

from rdabase import Assignment, OUT_OF_STATE, write_csv
from rdaensemble.general import make_plan

from .datatypes import *
from .connected import is_connected


class Plan:
    """A plan that can easily & efficiently evolve."""

    # Dynamic

    _generation: int

    _features: List[Feature]
    _districts: List[District]
    _border_segments: Dict[Tuple[DistrictOffset, DistrictOffset], BorderSegment]

    # Static

    _verbose: bool

    _features_index: Dict[GeoID, FeatureOffset]
    _features_graph: Dict[FeatureOffset, List[FeatureOffset]]
    _districts_index: Dict[DistrictID, DistrictOffset]

    _total_pop: int
    _target_pop: int
    _pop_threshold: float

    _measurements: Optional[Tuple[float, float]]

    def __init__(
        self,
        district_by_geoid: Dict[GeoID, DistrictID],
        pop_by_geoid: Dict[GeoID, int],
        graph: Dict[GeoID, List[GeoID]],
        seed: int,
        *,
        pop_threshold: float = 0.01,  # +/- 1% for each district
        verbose: bool = False,
    ) -> None:
        """Initialize the plan."""

        self._generation = 0  # Incremented w/ each move
        self._pop_threshold = pop_threshold
        self._verbose = verbose

        random.seed(seed)

        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = [
            Feature(a.geoid, a.district, pop_by_geoid[a.geoid]) for a in assignments
        ]
        self._features_index = {f.id: i for i, f in enumerate(self._features)}

        self._districts = self._invert_plan()
        self._districts_index = {d["id"]: i for i, d in enumerate(self._districts)}

        self._features_graph = self._index_graph(graph)

        if not self.is_valid_plan():
            raise Exception("Starting plan is not valid!")

        self._border_segments = self._init_border_segments()

        self._measurements = None

        if self._verbose:
            print("Starting plan is connected!")
            print(self)

    def __repr__(self) -> str:
        return f"Plan({self._generation})"  # TODO - Flesh this out

    ### PRIVATE ###

    def _invert_plan(self) -> List[District]:
        inverted: Dict[DistrictID, District] = {}

        self._total_pop = 0

        for i, f in enumerate(self._features):
            if f.district not in inverted:
                inverted[f.district] = {"id": f.district, "features": [], "pop": 0}

            inverted[f.district]["features"].append(self._features_index[f.id])
            inverted[f.district]["pop"] += f.pop
            self._total_pop += f.pop

        districts: List[District] = list(inverted.values())  # Lose the keys
        self._target_pop = self._total_pop // len(districts)

        return districts

    def _index_graph(
        self, graph: Dict[GeoID, List[GeoID]]
    ) -> Dict[FeatureOffset, List[FeatureOffset]]:
        """Convert a geoid-based graph to an offset-based graph."""

        indexed_graph: Dict[FeatureOffset, List[FeatureOffset]] = {}

        for geoid, neighbors in graph.items():
            if geoid == OUT_OF_STATE:
                continue
            offset: FeatureOffset = self._features_index[geoid]
            indexed_graph[offset] = [
                self._features_index[n] for n in neighbors if n != OUT_OF_STATE
            ]

        return indexed_graph

    def _all_connected(self) -> bool:
        """Is the plan fully connected?"""

        for d in self._districts:
            if not is_connected(d["features"], self._features_graph):
                return False

        return True

    def _all_within_tolerance(self) -> bool:
        """Are all districts within population tolerance?"""

        for d in self._districts:
            if not self.is_within_tolerance(d["features"]):
                return False

        return True

    def _is_connected(self, offsets: List[FeatureOffset]) -> bool:
        """Would a district with these feature offsets be connected?"""

        return is_connected(offsets, self._features_graph)

    def is_within_tolerance(self, features: List[FeatureOffset]) -> bool:
        """Would a district with these features be within the population tolerance?"""

        pop: int = 0
        for offset in features:
            pop += self._features[offset].pop

        tolerance: int = round(self._target_pop * self._pop_threshold)
        lower: int = self._target_pop - tolerance
        upper: int = self._target_pop + tolerance

        return pop >= lower and pop <= upper

    def _init_border_segments(
        self,
    ) -> Dict[Tuple[DistrictOffset, DistrictOffset], BorderSegment]:
        """Initialize border segments."""

        border_segments: Dict[
            Tuple[DistrictOffset, DistrictOffset],
            Dict[DistrictOffset, Set[FeatureOffset]],  # A set to avoid duplicates
        ] = {}

        for i, neighbors in self._features_graph.items():
            for n in neighbors:
                d1: DistrictOffset = self._districts_index[self._features[i].district]
                d2: DistrictOffset = self._districts_index[self._features[n].district]

                if d1 == d2:
                    continue

                seg_key: Tuple[DistrictOffset, DistrictOffset] = self.segment_key(
                    d1, d2
                )
                if seg_key not in border_segments:
                    border_segments[seg_key] = {
                        d1: set(),
                        d2: set(),
                    }

                border_segments[seg_key][d1].add(i)
                border_segments[seg_key][d2].add(n)

        converted: Dict[Tuple[DistrictOffset, DistrictOffset], BorderSegment] = {}
        for k, v in border_segments.items():
            converted[k] = {d: list(offsets) for d, offsets in v.items()}

        return border_segments

    def _size_1_moves(
        self,
        seg_key: Tuple[DistrictOffset, DistrictOffset],
        district_one: DistrictOffset,
        district_two: DistrictOffset,
    ) -> Tuple[List[Move], List[Move]]:
        """Generate all size-1 moves between two districts."""

        from_one: List[List[FeatureOffset]] = [
            [f] for f in self._border_segments[seg_key][district_one]
        ]
        from_two: List[List[FeatureOffset]] = [
            [f] for f in self._border_segments[seg_key][district_two]
        ]

        moves_from_one: List[Move] = [
            Move(m, district_one, district_two) for m in from_one
        ]
        moves_from_two: List[Move] = [
            Move(m, district_two, district_one) for m in from_two
        ]

        return (moves_from_one, moves_from_two)

    def _are_connected_border_features(
        self,
        features: List[FeatureOffset],
        from_district: DistrictOffset,
        to_district: DistrictOffset,
    ) -> bool:
        """Is the set of features connected and is at least one on the border between the two districts?"""

        # The from & to districts are adjacent

        seg_key: Tuple[DistrictOffset, DistrictOffset] = self.segment_key(
            from_district, to_district
        )
        if seg_key not in self._border_segments:
            if self._verbose:
                print(
                    f"... the move districts ({from_district} -> {to_district}) are not adjacent!"
                )
            return False

        # At least one feature in the move is on the border between the two districts

        from_border: List[FeatureOffset] = self._border_segments[seg_key][from_district]
        # to_border: List[FeatureOffset] = self._border_segments[seg_key][to_district]

        is_border: bool = False
        for f in features:
            if f in from_border:
                is_border = True
                break
        if not is_border:
            if self._verbose:
                print(
                    f"... no move feature ({features}) is on the border between the move districts ({from_district} -> {to_district})!"
                )
            return False

        # The move features are connected

        if not self._is_connected(features):
            if self._verbose:
                print(f"... the move features ({features}) are not connected!")
            return False

        return True

    ### PUBLIC ###

    def segment_key(
        self, d1: DistrictOffset, d2: DistrictOffset
    ) -> Tuple[DistrictOffset, DistrictOffset]:
        """Construct the canonical border segment key for a pair of districts (offsets)."""

        seg_key: Tuple[DistrictOffset, DistrictOffset] = (
            (d1, d2) if d1 < d2 else (d2, d1)
        )

        return seg_key

    def sorted_districts(self) -> List[Tuple[DistrictOffset, DistrictOffset]]:
        """Get all pairs of adjacent districts in sorted order."""

        pairs: List[Tuple[DistrictOffset, DistrictOffset]] = list(
            self._border_segments.keys()
        )

        return pairs

    def random_districts(self) -> List[Tuple[DistrictOffset, DistrictOffset]]:
        """Get all pairs of adjacent districts in random order."""

        pairs: List[Tuple[DistrictOffset, DistrictOffset]] = list(
            self._border_segments.keys()
        )
        random.shuffle(pairs)

        return pairs

    def random_moves(
        self, pair: Tuple[DistrictOffset, DistrictOffset], size: int = 1
    ) -> Tuple[List[Move], List[Move]]:
        """Generate random moves between two districts."""

        d1, d2 = pair
        seg_key: Tuple[DistrictOffset, DistrictOffset] = self.segment_key(d1, d2)
        if seg_key not in self._border_segments:
            raise Exception("No border segments between these districts!")

        district_one, district_two = seg_key

        moves_from_one: List[Move]
        moves_from_two: List[Move]

        match size:
            case 1:
                moves_from_one, moves_from_two = self._size_1_moves(
                    seg_key, district_one, district_two
                )
            case _:
                raise Exception("Only size-1 moves are supported right now!")

        random.shuffle(moves_from_one)
        random.shuffle(moves_from_two)

        return (moves_from_one, moves_from_two)

    def is_valid_plan(self) -> bool:
        """Is this plan state valid?"""

        valid: bool = True

        if not self._all_connected():
            print("Starting plan is not connected!")
            valid = False

        if not self._all_within_tolerance():
            print("Starting plan is not within population tolerance!")
            valid = False

        return valid

    def is_valid_move(self, move: Move) -> bool:
        """Would this be a valid move?"""

        d1: DistrictOffset = move.from_district
        d2: DistrictOffset = move.to_district

        # 1 - The from & to districts are adjacent

        seg_key: Tuple[DistrictOffset, DistrictOffset] = self.segment_key(d1, d2)
        if seg_key not in self._border_segments:
            if self._verbose:
                print(f"Move: {move}")
                print(f"... districts {d1} and {d2} are not adjacent!")
            return False

        # 2 - The move features are connected & at least one is on that border

        if not self._are_connected_border_features(move.features, d1, d2):
            if self._verbose:
                print(f"Move: {move}")
                print(
                    f"... features {move.features} are not connected and/or none are on the border between districts {d1} and {d2}!"
                )
            return False

        # 3 - The moved-from district would still be connected

        proposed: List[FeatureOffset] = list(
            self.district_features(move.from_district)
        )  # Copy the list of feature offsets

        for offset in move.features:
            proposed.remove(offset)

        if not self._is_connected(proposed):
            if self._verbose:
                print(f"Move: {move}")
                print(
                    f"... districts {d1} would not be connected, if ({move.features}) features were moved."
                )
            return False

        # 4 - The moved-from district population would still be w/in population tolerance

        if not self.is_within_tolerance(proposed):
            if self._verbose:
                print(f"Move: {move}")
                print(
                    f"... districts {d1} would not be within population tolerance, if ({move.features}) features were moved."
                )
            return False

        if self._verbose:
            print(f"Move: {move} is valid!")

        return True

    def mutate(self, move: Move):
        """Mutate the plan by applying a move.

        - Update the feature assignments
        - Update the districts' features
        - Update the affected border segments -- find affected districts | all borders (?)
        - Bump the generation
        """

        # TODO - NYI

        self._generation += 1

    def district_features(self, district: DistrictOffset) -> Set[FeatureOffset]:
        """Get all feature offsets for a district."""

        return self._districts[district]["features"]

    def to_csv(self, plan_path: str) -> None:
        """Write the plan to a CSV."""

        plan: List[Dict[GeoID, DistrictID]] = [
            {"GEOID": f.id, "DISTRICT": f.district} for f in self._features
        ]

        write_csv(plan_path, plan, ["GEOID", "DISTRICT"])


### END ###
