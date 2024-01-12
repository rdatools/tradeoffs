"""
CONNECTED - Is a district fully connected?

NOTE - This is a lightly edited generalized clone of the function in dra2020/drapy.
"""

from typing import Any, TypeAlias, List, Dict, Set

from rdabase import OUT_OF_STATE
from .datatypes import *

ID: TypeAlias = GeoID | Offset


def is_connected(ids: List[ID], graph: Dict[ID, List[ID]]) -> bool:
    """Is a graph is fully connected?
    i.e., w/o regard to the virtual state boundary "shapes".

    Kenshi's iterative implementation of the recursive algorithm

    ids - the list of ids for the geographies
    graph - the connectedness (adjacency) of the geos
    """
    visited: Set[ID] = set()

    all_geos: Set[ID] = set(ids)
    all_geos.discard(OUT_OF_STATE)

    start: ID = next(iter(all_geos))
    assert start != OUT_OF_STATE

    to_process: List[ID] = [start]
    while to_process:
        node: ID = to_process.pop()
        visited.add(node)
        neighbors: List[ID] = list(graph[node])
        if OUT_OF_STATE in neighbors:
            neighbors.remove(OUT_OF_STATE)
        neighbors_to_visit: List[ID] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


### END ###
