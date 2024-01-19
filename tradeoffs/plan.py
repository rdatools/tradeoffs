"""
EVOLVING PLAN
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

"""
class Assignment(NamedTuple):
    geoid: str
    district: DistrictID
"""

FeatureOffset: TypeAlias = Offset
DistrictOffset: TypeAlias = Offset


class Feature(NamedTuple):
    id: GeoID
    district: DistrictID
    pop: int


class District(TypedDict):
    id: DistrictID
    features: List[FeatureOffset]
    pop: int


BorderSegment: TypeAlias = Dict[
    DistrictOffset, List[FeatureOffset]
]  # Two: one for each side/district


class Move(NamedTuple):
    features: List[FeatureOffset]
    from_district: DistrictOffset
    to_district: DistrictOffset


class Plan:
    """A plan that can easily & efficiently evolve."""

    _generation: int

    _features: List[Feature]
    _features_index: Dict[GeoID, FeatureOffset]

    _measurements: Optional[Tuple[float, float]]

    _districts: List[District]
    _districts_index: Dict[DistrictID, DistrictOffset]

    _total_pop: int
    _target_pop: int

    _features_graph: Dict[FeatureOffset, List[FeatureOffset]]
    _border_segments: Dict[Tuple[DistrictOffset, DistrictOffset], BorderSegment]

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
        self._generation = 0  # TODO - Increment this with each move
        random.seed(seed)

        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = [
            Feature(a.geoid, a.district, pop_by_geoid[a.geoid]) for a in assignments
        ]
        self._features_index = {f.id: i for i, f in enumerate(self._features)}

        self._districts = self._invert_plan()
        self._districts_index = {d["id"]: i for i, d in enumerate(self._districts)}

        self._features_graph = self._index_graph(graph)

        if not self._all_connected():
            raise Exception("Starting plan is not connected!")

        self._border_segments = self._init_border_segments()

        self._measurements = None

        if verbose:
            print("Starting plan is connected!")
            print(self)

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

    def _is_connected(self, offsets: List[FeatureOffset]) -> bool:
        """Would a district with these feature offsets be connected?"""

        return is_connected(offsets, self._features_graph)

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

                seg_key: Tuple[DistrictOffset, DistrictOffset] = (
                    (d1, d2) if d1 < d2 else (d2, d1)
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

    ### PUBLIC ###

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

        district_one: DistrictOffset = pair[0] if pair[0] < pair[1] else pair[1]
        district_two: DistrictOffset = pair[1] if pair[0] < pair[1] else pair[0]

        seg_key: Tuple[DistrictOffset, DistrictOffset] = (district_one, district_two)
        if seg_key not in self._border_segments:
            raise Exception("No border segments between these districts!")

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

    def is_valid(self, move: Move) -> bool:
        """Would this be a valid move?"""

        # TODO - from & to districts are adjacent
        # TODO - precinct is on the border

        proposed: List[Offset] = list(
            self.district_features(move.from_district)
        )  # Copy the list of feature offsets
        for feature in move.features:
            proposed.remove(feature)

        # TODO - Check that the population would be OK

        if not self._is_connected(proposed):
            return False

        return True

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
