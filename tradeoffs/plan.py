"""
EVOLVING PLAN
"""

from typing import List, Dict, Set, NamedTuple

from rdabase import Assignment, OUT_OF_STATE
from rdaensemble.general import make_plan

"""
class Assignment(NamedTuple):
    geoid: str
    district: int | str
"""
Feature = Assignment


class EvolvingPlan:
    """An ensemble plan that can be evolved."""

    _features: List[Feature]
    _feature_index: Dict[str, int]
    _features_by_district: Dict[str | int, Set[int]]
    _indexed_graph: Dict[int, List[int]]

    def __init__(
        self, district_by_geoid: Dict[str, int | str], graph: Dict[str, List[str]]
    ) -> None:
        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = assignments
        self._feature_index = {f.geoid: i for i, f in enumerate(assignments)}
        self._features_by_district = self.invert_plan()
        self._indexed_graph = self.index_graph(graph)

    def invert_plan(self):
        """Collect geoids by district."""

        inverted: Dict[str | int, Set[int]] = dict()

        for i, f in enumerate(self._features):
            offset: int = self._feature_index[f.geoid]
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
            offset: int = self._feature_index[geoid]
            indexed_graph[offset] = [
                self._feature_index[n] for n in neighbors if n != OUT_OF_STATE
            ]

        return indexed_graph

    # TODO - More ...


### END ###
