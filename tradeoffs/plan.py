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

    # Static

    _verbose: bool

    _feature_indexes: Dict[GeoID, FeatureOffset]
    _feature_graph: Dict[FeatureOffset, List[FeatureOffset]]
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
        self._feature_indexes = {f.id: i for i, f in enumerate(self._features)}

        self._districts = self._invert_plan()
        self._district_indexes = {d["id"]: i for i, d in enumerate(self._districts)}
        self._district_ids = {v: k for k, v in self._district_indexes.items()}

        self._feature_graph = self._index_graph(graph)

        if not self.is_valid_plan():
            raise Exception("Starting plan is not valid!")
        elif self._verbose:
            print("Starting plan is valid.")

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

            inverted[f.district]["features"].append(self._feature_indexes[f.id])
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
            node: FeatureOffset = self._feature_indexes[geoid]
            indexed_graph[node] = [
                self._feature_indexes[n] for n in neighbors if n != OUT_OF_STATE
            ]

        return indexed_graph

    def _is_within_tolerance(self, features: List[FeatureOffset]) -> bool:
        """Would a district with these features be within the population tolerance?"""

        pop: int = 0
        for offset in features:
            pop += self._features[offset].pop

        tolerance: int = round(self._target_pop * self._pop_threshold)
        lower: int = self._target_pop - tolerance
        upper: int = self._target_pop + tolerance

        return pop >= lower and pop <= upper

    def _size_1_moves(self, seg_key: BorderKey) -> Tuple[List[Move], List[Move]]:
        """Generate all size-1 moves between two districts."""

        d1, d2 = seg_key
        d1_id: DistrictID = self._district_ids[d1]
        d2_id: DistrictID = self._district_ids[d2]

        from_one: List[FeatureOffset] = []
        for fo in self._districts[d1]["features"]:
            for no in self._feature_graph[fo]:
                if self._features[no].district == d2_id:
                    from_one.append(fo)
                    break
        from_two: List[FeatureOffset] = []
        for fo in self._districts[d2]["features"]:
            for no in self._feature_graph[fo]:
                if self._features[no].district == d1_id:
                    from_one.append(fo)
                    break

        moves_from_one: List[Move] = [Move([f], d1, d2) for f in from_one]
        moves_from_two: List[Move] = [Move([f], d2, d1) for f in from_two]

        return (moves_from_one, moves_from_two)

    ### PUBLIC ###

    def random_adjacent_districts(self) -> List[BorderKey]:
        """Get all pairs of adjacent districts in random order."""

        border_segments: Set[BorderKey] = set()

        for node, neighbors in self._features_graph.items():
            d_node: DistrictOffset = self._district_indexes[
                self._features[node].district
            ]

            for neighbor in neighbors:
                d_neighbor: DistrictOffset = self._district_indexes[
                    self._features[neighbor].district
                ]

                if d_node == d_neighbor:
                    continue

                seg_key: BorderKey = segment_key(d_node, d_neighbor)
                if seg_key not in border_segments:
                    border_segments.add(seg_key)

        pairs: List[BorderKey] = list(border_segments)
        random.shuffle(pairs)

        return pairs

    def random_mutations(self, seg_key: BorderKey, size: int = 1) -> List[Mutation]:
        """Generate random mutations of two districts."""

        d1, d2 = seg_key

        if self._debug:
            if seg_key not in self._border_segments:
                raise Exception("No border segments between these districts!")

        moves_from_one: List[Move]
        moves_from_two: List[Move]

        match size:
            case 1:
                moves_from_one, moves_from_two = self._size_1_moves(seg_key)
            case _:
                raise Exception("Only size-1 moves are supported right now!")

        random.shuffle(moves_from_one)
        random.shuffle(moves_from_two)

        mutations: List[Mutation] = []
        while len(moves_from_one) > 0 or len(moves_from_two) > 0:
            mutation: Mutation = []

            if len(moves_from_one) > 0:
                mutation.append(moves_from_one.pop())
            if len(moves_from_two) > 0:
                mutation.append(moves_from_two.pop())

            mutations.append(mutation)

        return mutations

    def is_valid_plan(self, changed: Optional[BorderKey] = None) -> bool:
        """Is this plan state valid?"""

        district_offsets: List[DistrictOffset] = (
            list(changed)
            if changed is not None
            else list(self._district_indexes.values())
        )

        valid: bool = True
        for do in district_offsets:
            d_id: DistrictID = self._district_ids[do]
            district_features: List[FeatureOffset] = self._districts[do]["features"]
            if not self._is_within_tolerance(district_features):
                if self._verbose:
                    print(f"District {do}/{d_id} is not within population tolerance!")
                valid = False
            if not is_connected(district_features, self._feature_graph):
                if self._verbose:
                    print(f"District {do}/{d_id} is not connected!")
                valid = False

        return valid

    def is_valid_mutation(self, mutation: Mutation) -> bool:
        """Would this be a valid mutation?"""

        for move in mutation:
            if not self.is_valid_move(move):
                return False

        # TODO - It's possible that each move is valid, but the overall mutation is not.

        return True

    def is_valid_move(self, move: Move) -> bool:
        """Would this be a valid move?"""

        from_id: DistrictID = self._district_ids[move.from_district]
        to_id: DistrictID = self._district_ids[move.to_district]
        enum_features: List = [f"{f}/{self._features[f].id}" for f in move.features]

        # NOTE - Syntactically incorrect moves may have been valid when they were specified.
        # 1 - The from & to districts are adjacent

        seg_key: BorderKey = segment_key(move.from_district, move.to_district)
        if seg_key not in self._border_segments:
            if self._verbose:
                print(
                    f"... Warning - Districts {move.from_district}/{from_id} and {move.to_district}/{to_id} are not adjacent!"
                )
            return False

        # 2 - Mutiple move features are connected

        if len(move.features) > 1 and not is_connected(
            move.features, self._feature_graph
        ):
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

        if not is_connected(proposed, self._feature_graph):
            if self._verbose:
                print(
                    f"... WARNING - District {move.from_district}/{from_id} would not be connected, if feature(s) {enum_features} were moved."
                )
            return False

        # 6 - The moved-from district population would still be w/in population tolerance

        if not self._is_within_tolerance(proposed):
            if self._verbose:
                print(
                    f"... WARNING - Districts {move.from_district}/{from_id} would not be within population tolerance, if feature(s) {enum_features} were moved."
                )
            return False

        return True

    # TODO - HERE
    def mutate(self, mutation: Mutation):
        """Mutate the plan by applying a mutation."""

        for move in mutation:
            from_district: District = self._districts[move.from_district]
            to_district: District = self._districts[move.to_district]

            from_id: DistrictID = self._district_ids[move.from_district]
            to_id: DistrictID = self._district_ids[move.to_district]

            # border_segments: Set[BorderKey] = set()
            # border_segments.add(segment_key(move.from_district, move.to_district))

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

                for neighbor in self._feature_graph[offset]:
                    neighbor_district: DistrictOffset = self._district_indexes[
                        self._features[neighbor].district
                    ]
                    if neighbor_district not in [move.from_district, move.to_district]:
                        border_segments.add(
                            segment_key(move.to_district, neighbor_district)
                        )

            # Update the affected border segments

            # for bs in border_segments:
            #     self._update_border_segment(bs)

        self._generation += 1

    def to_csv(self, plan_path: str) -> None:
        """Write the plan to a CSV."""

        plan: List[Dict[GeoID, DistrictID]] = [
            {"GEOID": f.id, "DISTRICT": f.district} for f in self._features
        ]

        write_csv(plan_path, plan, ["GEOID", "DISTRICT"])


### HELPERS ###


def segment_key(d1: DistrictOffset, d2: DistrictOffset) -> BorderKey:
    """Construct the canonical border segment key for a pair of districts (offsets)."""

    seg_key: BorderKey = (d1, d2) if d1 < d2 else (d2, d1)

    return seg_key


### END ###
