"""
CONNECTED - Is a district fully connected?

NOTE - This is a lightly edited generalized clone of the function in dra2020/drapy
that works on feature offsets instead of geoids.
"""

from typing import Any, TypeAlias, List, Dict, Set

from rdabase import OUT_OF_STATE
from .datatypes import *

Feature_ID: TypeAlias = int


def is_connected(
    ids: List[Feature_ID], graph: Dict[Feature_ID, List[Feature_ID]]
) -> bool:
    """Is a graph is fully connected?
    i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    ids - the list of ids for the geographies
    graph - the connectedness (adjacency) of the geos
    """
    visited: Set[Feature_ID] = set()
    all_geos: Set[Feature_ID] = set(ids)
    start: Feature_ID = next(iter(all_geos))
    to_process: List[Feature_ID] = [start]

    while to_process:
        node: Feature_ID = to_process.pop()
        visited.add(node)
        neighbors: List[Feature_ID] = graph[node]
        neighbors_to_visit: List[Feature_ID] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


### END ###
