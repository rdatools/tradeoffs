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


def id_most_notable_maps(frontiers: Dict[str, List[Dict]]) -> Dict[str, int]:
    """Identify the most notable map for each dimension in the frontiers.

    "notable_maps": [
    {
        "proportionality": "957_591",
        "ratings": [
            100,
            53,
            46,
            32,
            37
        ]
    },

    total: int = 0
    qualifying: int = 0

    for s in scores:
        total += 1
        ratings: List[int] = [int(s[m]) for m in metrics]
        if not qualifying_map(ratings, filters):
            continue

        for d in dimensions:
            if better_map(ratings, notable_maps[d], d):
                notable_maps[d][metrics[d]] = s["map"]
                notable_maps[d]["ratings"] = ratings

        qualifying += 1
    """

    # output: Dict[str, Any] = dict()
    # notable_maps: List[Dict[str, Any]] = [{m: "None", "ratings": []} for m in metrics]

    notable_maps: Dict[str, int] = dict()

    return notable_maps


### END ###
