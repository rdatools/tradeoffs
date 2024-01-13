"""
EVOLVING PLAN
"""

from typing import Any, List, Dict, Set, Tuple, TypeAlias, NamedTuple, TypedDict

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
    features: Set[FeatureOffset]
    pop: int


BorderSegment: TypeAlias = Dict[
    DistrictOffset, Set[FeatureOffset]
]  # Two: one for each side/district


class EPlan:
    """A plan from an ensemble that can easily & efficiently evolve."""

    _features: List[Feature]
    _features_index: Dict[GeoID, FeatureOffset]

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
    ) -> None:
        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = [
            Feature(a.geoid, a.district, pop_by_geoid[a.geoid]) for a in assignments
        ]
        self._features_index = {f.id: i for i, f in enumerate(self._features)}

        self._districts = self.invert_plan()
        self._districts_index = {d["id"]: i for i, d in enumerate(self._districts)}

        self._features_graph = self.index_graph(graph)

        if not self.all_connected():
            raise Exception("Starting plan is not connected!")
        else:
            print("Starting plan is connected!")

        self._border_segments = self.init_border_segments()

    def invert_plan(self) -> List[District]:
        inverted: Dict[DistrictID, District] = dict()

        self._total_pop = 0

        for i, f in enumerate(self._features):
            if f.district not in inverted:
                inverted[f.district] = {"id": f.district, "features": set(), "pop": 0}

            inverted[f.district]["features"].add(self._features_index[f.id])
            inverted[f.district]["pop"] += f.pop
            self._total_pop += f.pop

        districts: List[District] = list(inverted.values())
        self._target_pop = self._total_pop // len(districts)

        return districts

    def index_graph(
        self, graph: Dict[GeoID, List[GeoID]]
    ) -> Dict[FeatureOffset, List[FeatureOffset]]:
        """Convert a geoid-based graph to an offset-based graph."""

        indexed_graph: Dict[FeatureOffset, List[FeatureOffset]] = dict()

        for geoid, neighbors in graph.items():
            if geoid == OUT_OF_STATE:
                continue
            offset: FeatureOffset = self._features_index[geoid]
            indexed_graph[offset] = [
                self._features_index[n] for n in neighbors if n != OUT_OF_STATE
            ]

        return indexed_graph

    def all_connected(self) -> bool:
        """Is the plan fully connected?"""

        for d in self._districts:
            if not is_connected(list(d["features"]), self._features_graph):
                return False

        return True

    def is_connected(self, offsets: List[FeatureOffset]) -> bool:
        """Would a district with these feature offsets be connected?"""

        return is_connected(offsets, self._features_graph)

    def init_border_segments(
        self,
    ) -> Dict[Tuple[DistrictOffset, DistrictOffset], BorderSegment]:
        """Initialize border segments."""

        border_segments: Dict[
            Tuple[DistrictOffset, DistrictOffset], BorderSegment
        ] = dict()

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

        return border_segments

    def district_adjacencies(self) -> List[Tuple[DistrictOffset, DistrictOffset]]:
        """Get all district adjacencies."""

        return sorted(list(self._border_segments.keys()))

    def district_features(self, district: DistrictOffset) -> Set[FeatureOffset]:
        """Get all feature offsets for a district."""

        return self._districts[district]["features"]

    def border_features(
        self, from_district: DistrictOffset, to_district: DistrictOffset
    ) -> Set[FeatureOffset]:
        """The offsets for features that could be reassigned from one district to another."""

        seg_key: Tuple[DistrictOffset, DistrictOffset] = (
            (from_district, to_district)
            if from_district < to_district
            else (to_district, from_district)
        )

        border_features: Set[FeatureOffset] = self._border_segments[seg_key][
            from_district
        ]

        return border_features

    def to_csv(self, plan_path: str) -> None:
        """Write the plan to a CSV."""

        plan: List[Dict[GeoID, DistrictID]] = [
            {"GEOID": f.id, "DISTRICT": f.district} for f in self._features
        ]

        write_csv(plan_path, plan, ["GEOID", "DISTRICT"])

    # TODO - More ...


### END ###
