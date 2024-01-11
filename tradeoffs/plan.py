"""
EVOLVING PLAN
"""

from typing import List, Dict, Set, NamedTuple

from rdabase import Assignment
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
    _index: Dict[str, int]
    _inverted: Dict[str | int, Set[int]]

    def __init__(self, district_by_geoid: Dict[str, int | str]) -> None:
        assignments: List[Assignment] = make_plan(district_by_geoid)
        self._features = assignments
        self._index = {f.geoid: i for i, f in enumerate(assignments)}
        self._inverted = self.invert_plan()

    def invert_plan(self):
        """Collect geoids by district."""

        inverted: Dict[str | int, Set[int]] = dict()

        for i, f in enumerate(self._features):
            offset: int = self._index[f.geoid]
            district: int | str = f.district

            if district not in inverted:
                inverted[district] = set()

            inverted[district].add(offset)

        return inverted

    # TODO - More ...


### END ###
