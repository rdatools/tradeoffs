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

    _generation: int  # Number of mutations applied
    _moves: int  # Number of features moved

    _features: List[Feature]
    _districts: List[District]
    _border_segments: Dict[Tuple[DistrictOffset, DistrictOffset], BorderSegment]

    # Static

    _verbose: bool

    _features_index: Dict[GeoID, FeatureOffset]
    _features_graph: Dict[FeatureOffset, List[FeatureOffset]]
    _district_indexes: Dict[DistrictID, DistrictOffset]
    _district_ids: Dict[DistrictOffset, DistrictID]

    _total_pop: int
    _target_pop: int
    _pop_threshold: float

    def __init__(
        self,
        district_by_geoid: Dict[GeoID, DistrictID],
        pop_by_geoid: Dict[GeoID, int],
        graph: Dict[GeoID, List[GeoID]],
        seed: int,
        *,
        pop_threshold: float = 0.01,
        verbose: bool = False,
        debug: bool = False,
    ) -> None:
        """Initialize the plan."""

        random.seed(seed)

        self._verbose = verbose
        self._debug = debug

        self._generation = 0
        self._moves = 0
        self._pop_threshold = pop_threshold

        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = [
            Feature(a.geoid, a.district, pop_by_geoid[a.geoid]) for a in assignments
        ]
        self._features_index = {f.id: i for i, f in enumerate(self._features)}

        self._districts = self._invert_plan()
        self._district_indexes = {d["id"]: i for i, d in enumerate(self._districts)}
        self._district_ids = {v: k for k, v in self._district_indexes.items()}

        self._features_graph = self._index_graph(graph)

        if not self.is_valid_plan():
            raise Exception("Starting plan is not valid!")
        elif self._verbose:
            print("Starting plan is valid.")

        self._border_segments = self._init_border_segments()

        if self._verbose:
            print()
            print(self)
            print()

    def __repr__(self) -> str:
        return f"Plan: # of mutations = {self._generation}, # features moves = {self._moves}"

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
                d1: DistrictOffset = self._district_indexes[self._features[i].district]
                d2: DistrictOffset = self._district_indexes[self._features[n].district]

                if d1 == d2:
                    continue

                seg_key: Tuple[DistrictOffset, DistrictOffset] = segment_key(d1, d2)
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

        if self._debug:
            valid: bool = True
            print()
            print("DEBUG - Check initial border segments:")
            for k, v in converted.items():
                if not self._valid_border_segment(k, v):
                    valid = False
                    print("DEBUG - Likely more ...")
                    break
            if valid:
                print("DEBUG - Initial border segments are valid.")

        return converted

    def _update_border_segment(
        self, seg_key: Tuple[DistrictOffset, DistrictOffset]
    ) -> None:
        """Initialize a border segment."""

        d1, d2 = seg_key
        if self._debug:
            if d1 >= d2:
                print("DEBUG - Badly formed segment key: ({d1}, {d2})!")

        border_segment: Dict[
            DistrictOffset, Set[FeatureOffset]  # A set to avoid duplicates
        ] = {
            d1: set(),
            d2: set(),
        }  # A pair of adjacent districts

        districts: List[DistrictOffset] = [d1, d2]
        for i, d in enumerate(districts):
            j: int = 1 - i
            for f in self._districts[d]["features"]:
                if self._does_border_district(f, districts[j]):
                    border_segment[d].add(f)

        converted: BorderSegment = {}
        for k, v in border_segment.items():
            converted[k] = list(v)

        if self._debug:
            if not self._valid_border_segment(seg_key, converted):
                print()
                print(f"DEBUG - Initial border segment {seg_key} is not valid.")

        self._border_segments[seg_key] = converted

    def _valid_border_segment(
        self, seg_key: Tuple[DistrictOffset, DistrictOffset], bs: BorderSegment
    ) -> bool:
        """Validate a border segment."""

        valid: bool = True
        for d, offsets in bs.items():
            d_id: DistrictID = self._district_ids[d]

            if d not in seg_key:
                valid = False
                print(
                    f"DEBUG - Border district {d}/{d_id} is not in segment key {seg_key}!"
                )
                break

            for offset in offsets:
                f: Feature = self._features[offset]

                if f.district != d_id:
                    valid = False
                    d_index: DistrictOffset = self._district_indexes[f.district]
                    print(
                        f"DEBUG - Border segment feature {offset}/{f.id} is assigned to district {d_index}/{f.district} not {d}/{d_id}!"
                    )
                    break

                if not self._does_border_district(offset, d):
                    valid = False
                    print(
                        f"DEBUG - Border segment feature {offset}/{f.id} is not on the border with district {d}/{d_id}!"
                    )
                    break

            if not valid:
                break

        return valid

    def _does_border_district(self, f: FeatureOffset, d: DistrictOffset) -> bool:
        """Does this feature border that district?"""

        for neighbor in self._features_graph[f]:
            if self._features[neighbor].district == d:
                return True

        return False

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
    ) -> List[List[Move]]:
        """Generate random moves between two districts."""

        d1, d2 = pair
        seg_key: Tuple[DistrictOffset, DistrictOffset] = segment_key(d1, d2)
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

        return [moves_from_one, moves_from_two]

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

        from_id: DistrictID = self._district_ids[move.from_district]
        to_id: DistrictID = self._district_ids[move.to_district]
        enum_features: List = [f"{f}/{self._features[f].id}" for f in move.features]

        # NOTE - Syntactically incorrect moves may have been valid when they were specified.
        # 1 - The from & to districts are adjacent

        seg_key: Tuple[DistrictOffset, DistrictOffset] = segment_key(
            move.from_district, move.to_district
        )
        if seg_key not in self._border_segments:
            if self._verbose:
                print(
                    f"... Warning - Districts {move.from_district}/{from_id} and {move.to_district}/{to_id} are not adjacent!"
                )
            return False

        # 2 - Mutiple move features are connected

        if len(move.features) > 1 and not self._is_connected(move.features):
            if self._verbose:
                print(
                    f"... Warning - The move features {enum_features} are not connected!"
                )
                return False

        # 3 - The move features are all in the moved-from district

        proposed: List[FeatureOffset] = list(
            self._districts[move.from_district]["features"]
        )  # Copy the list of feature offsets

        for offset in move.features:
            if offset not in proposed:
                if self._verbose:
                    f: Feature = self._features[offset]
                    geoid: GeoID = f.id
                    d_id: DistrictID = self._district_ids[move.from_district]
                    print(
                        f"... Warning - Feature {offset}/{geoid} is not in district {move.from_district}/{d_id}!"
                    )
                return False

        # 4 - At least one feature in the move is on the border between the two districts

        from_border: List[FeatureOffset] = self._border_segments[seg_key][
            move.from_district
        ]

        on_border: bool = False
        for f in move.features:
            if f in from_border:
                on_border = True
                break
        if not on_border:
            if self._verbose:
                print(
                    f"... Warning - None of {len(move.features)} features is on the border between districts ({move.from_district}/{from_id} -> {move.to_district}/{to_id})!"
                )
            return False

        # The move is well formed, syntactically. Now warn about semantic effects.

        # 5 - The moved-from district would still be connected

        for offset in move.features:
            proposed.remove(offset)

        if not self._is_connected(proposed):
            if self._verbose:
                print(
                    f"... WARNING - District {move.from_district}/{from_id} would not be connected, if feature(s) {enum_features} were moved."
                )
            return False

        # 6 - The moved-from district population would still be w/in population tolerance

        if not self.is_within_tolerance(proposed):
            if self._verbose:
                print(
                    f"... WARNING - Districts {move.from_district}/{from_id} would not be within population tolerance, if feature(s) {enum_features} were moved."
                )
            return False

        return True

    def mutate(self, move: Move):
        """Mutate the plan by applying a move."""

        from_district: District = self._districts[move.from_district]
        to_district: District = self._districts[move.to_district]

        from_id: DistrictID = self._district_ids[move.from_district]
        to_id: DistrictID = self._district_ids[move.to_district]

        border_segments: Set[Tuple[DistrictOffset, DistrictOffset]] = set()
        border_segments.add(segment_key(move.from_district, move.to_district))

        for offset in move.features:
            f: Feature = self._features[offset]

            if self._verbose:
                print(
                    f"... Moving feature {offset}/{f.id} from district {move.from_district}/{from_id} to {move.to_district}/{to_id}."
                )

            # Update the feature assignment

            self._features[offset] = Feature(f.id, to_id, f.pop)

            # Update the two districts' features

            from_district["features"].remove(offset)
            from_district["pop"] -= f.pop

            to_district["features"].append(offset)
            to_district["pop"] += f.pop

            self._moves += 1

            # Find all the affected border segments -- could be others

            for neighbor in self._features_graph[offset]:
                neighbor_district: DistrictOffset = self._district_indexes[
                    self._features[neighbor].district
                ]
                if neighbor_district not in [move.from_district, move.to_district]:
                    border_segments.add(
                        segment_key(move.to_district, neighbor_district)
                    )

        # Update the affected border segments

        for bs in border_segments:
            self._update_border_segment(bs)

        self._generation += 1

    def to_csv(self, plan_path: str) -> None:
        """Write the plan to a CSV."""

        plan: List[Dict[GeoID, DistrictID]] = [
            {"GEOID": f.id, "DISTRICT": f.district} for f in self._features
        ]

        write_csv(plan_path, plan, ["GEOID", "DISTRICT"])


### HELPERS ###


def segment_key(
    d1: DistrictOffset, d2: DistrictOffset
) -> Tuple[DistrictOffset, DistrictOffset]:
    """Construct the canonical border segment key for a pair of districts (offsets)."""

    seg_key: Tuple[DistrictOffset, DistrictOffset] = (d1, d2) if d1 < d2 else (d2, d1)

    return seg_key


### END ###
