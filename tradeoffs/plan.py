"""
EVOLVING PLAN
"""

from typing import Any, List, Dict, Set, Tuple, NamedTuple, TypeAlias

from rdabase import Assignment, OUT_OF_STATE, write_csv
from rdaensemble.general import make_plan

"""
class Assignment(NamedTuple):
    geoid: str
    district: int | str
"""
Feature = Assignment

District: TypeAlias = int | str
FeatureOffsets: TypeAlias = Set[int]


class BorderSegment(NamedTuple):
    features: Dict[District, FeatureOffsets]  # Two: one for each side/district


class EvolvingPlan:
    """An ensemble plan that can be evolved."""

    _features: List[Feature]
    _features_index: Dict[str, int]
    _features_by_district: Dict[str | int, Set[int]]
    _features_graph: Dict[int, List[int]]
    _border_segments: Dict[Tuple[District, District], BorderSegment]

    def __init__(
        self, district_by_geoid: Dict[str, int | str], graph: Dict[str, List[str]]
    ) -> None:
        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = assignments
        self._features_index = {f.geoid: i for i, f in enumerate(assignments)}
        self._features_by_district = self.invert_plan()
        self._features_graph = self.index_graph(graph)

    def invert_plan(self):
        """Collect geoids by district."""

        inverted: Dict[str | int, Set[int]] = dict()

        for i, f in enumerate(self._features):
            offset: int = self._features_index[f.geoid]
            district: int | str = f.district

            if district not in inverted:
                inverted[district] = set()

            inverted[district].add(offset)

        return inverted

    def index_graph(self, graph: Dict[str, List[str]]):
        """Convert a geoid-based graph to an offset-based graph."""

        indexed_graph: Dict[int, List[int]] = dict()

        for geoid, neighbors in graph.items():
            if geoid == OUT_OF_STATE:
                continue
            offset: int = self._features_index[geoid]
            indexed_graph[offset] = [
                self._features_index[n] for n in neighbors if n != OUT_OF_STATE
            ]

        return indexed_graph

    def to_csv(self, plan_path: str) -> None:
        """Write the plan to a CSV."""

        plan: List[Dict[str, str | int]] = [
            {"GEOID": a.geoid, "DISTRICT": a.district} for a in self._features
        ]

        write_csv(plan_path, plan, ["GEOID", "DISTRICT"])

    # TODO - More ...


### END ###
