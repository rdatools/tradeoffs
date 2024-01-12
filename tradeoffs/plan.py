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
    district: District
"""
Feature = Assignment

FeatureOffsets: TypeAlias = Set[Offset]
BorderSegment: TypeAlias = Dict[
    District, FeatureOffsets
]  # Two: one for each side/district


class EPlan:
    """A plan from an ensemble that can easily & efficiently evolve."""

    _features: List[Feature]
    _features_index: Dict[str, Offset]
    _features_by_district: Dict[District, Set[Offset]]
    _features_graph: Dict[Offset, List[Offset]]
    _border_segments: Dict[Tuple[District, District], BorderSegment]

    def __init__(
        self, district_by_geoid: Dict[GeoID, District], graph: Dict[GeoID, List[GeoID]]
    ) -> None:
        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = assignments
        self._features_index = {f.geoid: i for i, f in enumerate(assignments)}
        self._features_by_district = self.invert_plan()
        self._features_graph = self.index_graph(graph)

        if not self.all_connected():
            raise Exception("Starting plan is not connected!")
        else:
            print("Starting plan is connected!")

        self._border_segments = self.init_border_segments()

    def invert_plan(self) -> Dict[District, Set[Offset]]:
        """Collect geoid offsets by district."""

        inverted: Dict[District, Set[Offset]] = dict()

        for i, f in enumerate(self._features):
            offset: Offset = self._features_index[f.geoid]
            district: District = f.district

            if district not in inverted:
                inverted[district] = set()

            inverted[district].add(offset)

        return inverted

    def index_graph(
        self, graph: Dict[GeoID, List[GeoID]]
    ) -> Dict[Offset, List[Offset]]:
        """Convert a geoid-based graph to an offset-based graph."""

        indexed_graph: Dict[Offset, List[Offset]] = dict()

        for geoid, neighbors in graph.items():
            if geoid == OUT_OF_STATE:
                continue
            offset: Offset = self._features_index[geoid]
            indexed_graph[offset] = [
                self._features_index[n] for n in neighbors if n != OUT_OF_STATE
            ]

        return indexed_graph

    def all_connected(self) -> bool:
        """Is the plan fully connected?"""

        for district, offsets in self._features_by_district.items():
            if not is_connected(list(offsets), self._features_graph):  # type: ignore
                return False

        return True

    def is_connected(self, ids: List[Offset]) -> bool:
        """Would a district with these features be connected?"""

        return is_connected(ids, self._features_graph)  # type: ignore

    def init_border_segments(self) -> Dict[Tuple[District, District], BorderSegment]:
        """Initialize border segments."""

        border_segments: Dict[Tuple[District, District], BorderSegment] = dict()

        for i, neighbors in self._features_graph.items():
            for n in neighbors:
                d1: District = self._features[i].district
                d2: District = self._features[n].district

                if d1 == d2:
                    continue

                seg_key: Tuple[District, District] = (
                    (d1, d2) if int(d1) < int(d2) else (d2, d1)
                )
                if seg_key not in border_segments:
                    border_segments[seg_key] = {
                        d1: set(),
                        d2: set(),
                    }

                border_segments[seg_key][d1].add(i)
                border_segments[seg_key][d2].add(n)

        return border_segments

    def district_adjacencies(self) -> List[Tuple[District, District]]:
        """Get all district adjacencies."""

        return sorted(list(self._border_segments.keys()))

    def district_features(self, district: District) -> Set[Offset]:
        """Get all feature offsets for a district."""

        return self._features_by_district[district]

    def border_features(
        self, from_district: District, to_district: District
    ) -> Set[Offset]:
        """The offsets for features that could be reassigned from one district to another."""

        seg_key: Tuple[District, District] = (
            (from_district, to_district)
            if int(from_district) < int(to_district)
            else (to_district, from_district)
        )

        border_features: Set[Offset] = self._border_segments[seg_key][from_district]

        return border_features

    def to_csv(self, plan_path: str) -> None:
        """Write the plan to a CSV."""

        plan: List[Dict[GeoID, District]] = [
            {"GEOID": a.geoid, "DISTRICT": a.district} for a in self._features
        ]

        write_csv(plan_path, plan, ["GEOID", "DISTRICT"])

    # TODO - More ...


### END ###
