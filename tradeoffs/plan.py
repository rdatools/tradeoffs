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
import copy

from rdabase import Assignment, OUT_OF_STATE, write_csv
from rdaensemble.general import make_plan

from .datatypes import *
from .connected import is_connected


class Plan:
    """A plan that can easily & efficiently evolve."""

    # Static

    _feature_indexes: Dict[GeoID, FeatureOffset]
    _feature_graph: Dict[FeatureOffset, List[FeatureOffset]]
    _district_indexes: Dict[DistrictID, DistrictOffset]
    _district_ids: Dict[DistrictOffset, DistrictID]

    _total_pop: int
    _target_pop: int
    _pop_threshold: float

    _verbose: bool

    # Dynamic

    _features: List[Feature]
    _districts: List[District]

    _generation: int
    _features_moved: int

    _undo_feature_offsets: List[FeatureOffset]
    _undo_features: List[Feature]
    _undo_district_offsets: List[DistrictOffset]
    _undo_districts: List[District]

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
        self._features_moved = 0
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
        return f"Plan: # of mutations = {self._generation}, # features moves = {self._features_moved}"

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

    def _is_within_tolerance(self, do: DistrictOffset) -> bool:
        """Is this district within the population tolerance?"""

        pop: int = self._districts[do]["pop"]

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
                    from_two.append(fo)
                    break

        assert len(from_one) > 0 and len(from_two) > 0

        moves_from_one: List[Move] = [Move([f], d1, d2) for f in from_one]
        moves_from_two: List[Move] = [Move([f], d2, d1) for f in from_two]

        return (moves_from_one, moves_from_two)

    ### PUBLIC ###

    def random_adjacent_districts(self) -> List[BorderKey]:
        """Get all pairs of adjacent districts in random order."""

        border_segments: Set[BorderKey] = set()

        for node, neighbors in self._feature_graph.items():
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
            if not self._is_within_tolerance(do):
                if self._verbose:
                    print(
                        f"... District {do}/{d_id} is not within population tolerance!"
                    )
                valid = False
                break
            district_features: List[FeatureOffset] = self._districts[do]["features"]
            if not is_connected(district_features, self._feature_graph):
                if self._verbose:
                    print(f"... District {do}/{d_id} is not connected!")
                valid = False
                break

        return valid

    # TODO
    def mutate(self, mutation: Mutation):
        """Mutate the plan by applying a mutation. Save undo info."""

        self._undo_district_offsets = [
            mutation[0].from_district,
            mutation[0].to_district,
        ]  # The pair of districts is the same for all moves in a mutation
        self._undo_districts = [
            copy.deepcopy(self._districts[d]) for d in self._undo_district_offsets
        ]  # Copy the districts

        self._undo_feature_offsets = []
        self._undo_features = []

        for move in mutation:
            from_id: DistrictID = self._districts[move.from_district]["id"]
            to_id: DistrictID = self._districts[move.to_district]["id"]

            for fo in move.features:
                self._undo_feature_offsets.append(fo)
                f: Feature = Feature(*self._features[fo])  # Copy the feature
                self._undo_features.append(f)

                if self._verbose:
                    print(
                        f"... Moving feature {fo}/{f.id} from district {move.from_district}/{from_id} to {move.to_district}/{to_id}."
                    )

                self._features[fo] = Feature(f.id, to_id, f.pop)  # Update the features

                self._districts[move.from_district]["features"].remove(fo)
                self._districts[move.from_district]["pop"] -= f.pop

                self._districts[move.to_district]["features"].append(fo)
                self._districts[move.to_district]["pop"] += f.pop

                self._features_moved += 1

        self._generation += 1

    # TODO
    def undo(self):
        """Undo the last mutation applied to the plan."""

        if self._verbose:
            print("... Undoing the last mutation.")

        for i, do in enumerate(self._undo_district_offsets):
            self._districts[do] = self._undo_districts[i]

        for j, fo in enumerate(self._undo_feature_offsets):
            self._features[fo] = self._undo_features[j]
            self._features_moved -= 1

        self._generation -= 1

        if self._debug:
            if not self.is_valid_plan(segment_key(*self._undo_district_offsets)):
                raise Exception("Plan is not valid after undo!")

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
