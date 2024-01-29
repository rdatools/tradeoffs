"""
CONNECTED - Is a district fully connected?

NOTE - This is a lightly edited generalized clone of the function in dra2020/drapy
that works on feature offsets instead of geoids.
"""

from typing import Any, TypeAlias, List, Dict, Set

from rdabase import OUT_OF_STATE, IntUnionFind
from .datatypes import *


def is_connected(
    ids: List[FeatureOffset], graph: Dict[FeatureOffset, List[FeatureOffset]]
) -> bool:
    """Is a collection of features fully connected?
    i.e., w/o regard to the virtual state boundary 'shapes'.

    Kenshi's iterative implementation of the recursive algorithm

    ids - the list of ids for the geographies
    graph - the connectedness (adjacency) of the geos
    """
    visited: Set[FeatureOffset] = set()
    all_geos: Set[FeatureOffset] = set(ids)
    start: FeatureOffset = next(iter(all_geos))
    to_process: List[FeatureOffset] = [start]

    while to_process:
        node: FeatureOffset = to_process.pop()
        visited.add(node)
        neighbors: List[FeatureOffset] = graph[node]
        neighbors_to_visit: List[FeatureOffset] = [
            n for n in neighbors if n in all_geos and n not in visited
        ]
        to_process.extend(neighbors_to_visit)

    return len(visited) == len(all_geos)


def is_connected_implied(
    ids: List[FeatureOffset], graph: Dict[FeatureOffset, List[FeatureOffset]]
) -> bool:
    """Is a collection of features fully connected?
    i.e., w/o regard to the virtual state boundary 'shapes'.

    Todd's union-find approach

    ids - the list of ids for the geographies
    graph - the connectedness (adjacency) of the geos
    """

    district: Set[FeatureOffset] = set(ids)
    ds = IntUnionFind(district)
    for node in district:
        for neighbor in graph[node]:
            if neighbor in district:
                ds.merge(node, neighbor)

    return ds.n_subsets == 1


### END ###
