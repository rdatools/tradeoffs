"""
ID NOTABLE MAPS IN A SET OF PAIRWISE FRONTIERS
"""

from typing import Any, Dict, List

from rdaensemble.general import ratings_dimensions, ratings_indexes, better_map


def id_most_notable_maps(
    frontiers: Dict[str, List[Dict]]
) -> List[Dict[str, Dict[str, str | int]]]:
    """Identify the *most* notable map for each dimension in the frontiers.

    TODO - Hand verify these results.
    """

    # output: Dict[str, Any] = dict()
    notable_maps: List[Dict[str, Any]] = [
        {m: "None", "ratings": []} for m in ratings_dimensions
    ]
    indices: List[Dict[str, Dict[str, str | int]]] = [
        {m: {"frontier": "None", "offset": -1}} for m in ratings_dimensions
    ]

    for k, v in frontiers.items():
        for i, m in enumerate(v):
            name: str = m["map"]
            ratings: List[int] = m["ratings"]
            assert len(ratings) == len(ratings_dimensions)

            for j in ratings_indexes:
                if better_map(ratings, notable_maps[j], j):
                    notable_maps[j][ratings_dimensions[j]] = name
                    notable_maps[j]["ratings"] = ratings

                    indices[j] = {ratings_dimensions[j]: {"frontier": k, "offset": i}}

    return indices


### END ###
