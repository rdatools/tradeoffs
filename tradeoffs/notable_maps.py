"""
ID NOTABLE MAPS IN A SET OF PAIRWISE FRONTIERS
"""

from typing import Any, Dict, List

# TODO - Import these from rdaensemble
metrics: List[str] = [
    "proportionality",
    "competitiveness",
    "minority",
    "compactness",
    "splitting",
]
dimensions: List[int] = list(range(5))


def better_map(
    ratings: List[int], current_best: Dict[str, Any], dimension: int
) -> bool:
    if current_best[metrics[dimension]] == "None":
        return True
    if (ratings[dimension] > current_best["ratings"][dimension]) or (
        ratings[dimension] == current_best["ratings"][dimension]
        and sum(ratings) > sum(current_best["ratings"])
    ):
        return True
    else:
        return False


# end import


def id_most_notable_maps(
    frontiers: Dict[str, List[Dict]]
) -> List[Dict[str, Dict[str, str | int]]]:
    """Identify the *most* notable map for each dimension in the frontiers.

    TODO - Hand verify these results.
    """

    # output: Dict[str, Any] = dict()
    notable_maps: List[Dict[str, Any]] = [{m: "None", "ratings": []} for m in metrics]
    indices: List[Dict[str, Dict[str, str | int]]] = [
        {m: {"frontier": "None", "offset": -1}} for m in metrics
    ]

    for k, v in frontiers.items():
        for i, m in enumerate(v):
            name: str = m["map"]
            ratings: List[int] = m["ratings"]
            assert len(ratings) == len(dimensions)
            j: int = i + 1

            for d in dimensions:
                if better_map(ratings, notable_maps[d], d):
                    notable_maps[d][metrics[d]] = name
                    notable_maps[d]["ratings"] = ratings

                    indices[d] = {metrics[d]: {"frontier": k, "offset": i}}

    return indices


### END ###
