"""
CONNECTED - Is a district fully connected?

NOTE - This is a lightly edited generalized clone of the function in dra2020/drapy.
"""

from typing import Any, TypeAlias, List, Dict, Set

from rdabase import OUT_OF_STATE
from .datatypes import *


def is_connected(ids: List[Offset], graph: Dict[Offset, List[Offset]]) -> bool:
    """Is a graph is fully connected?
    i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    ids - the list of ids for the geographies
    graph - the connectedness (adjacency) of the geos
    """
    visited: Set[Offset] = set()
    all_geos: Set[Offset] = set(ids)
    start: Offset = next(iter(all_geos))
    to_process: List[Offset] = [start]

    while to_process:
        node: Offset = to_process.pop()
        visited.add(node)
        neighbors: List[Offset] = list(graph[node])
        neighbors_to_visit: List[Offset] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


### END ###
