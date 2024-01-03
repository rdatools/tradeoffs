"""
FRONTIER HELPERS
"""

from typing import Any, Dict, List

import numpy as np
import pandas as pd
import itertools

from rdaensemble.general import ratings_dimensions


def find_frontiers(
    ratings: pd.DataFrame,  # , fieldnames: List[str]
) -> Dict[str, List[Dict]]:
    """Find the frontier for a ratings dataframe.

    TODO - Verify that this works visually ... or add test cases!
    """

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))
    frontiers: Dict[str, List[Dict]] = dict()

    for p in pairs:
        label: str = f"{p[0]}_{p[1]}"
        frontiers[label] = list()

        subset: pd.DataFrame = ratings[list(p)]
        is_frontier: np.ndarray = is_pareto_efficient_dumb(subset.to_numpy())

        maps: List[str] = list()
        for i, is_efficient in enumerate(is_frontier):
            if is_efficient:
                maps.append(ratings.iloc[i]["map"])

        for m in maps:
            row = (
                ratings.loc[ratings["map"] == m, ["map"] + ratings_dimensions]
                .values.flatten()
                .tolist()
            )
            name: str = row.pop(0)
            point: List[int] = [int(r) for r in row]
            frontiers[label].append({"map": name, "ratings": point})

        dimension: int = ratings_dimensions.index(p[0])
        frontiers[label] = sorted(
            frontiers[label], key=lambda d: d["ratings"][dimension], reverse=True
        )

    return frontiers


def is_pareto_efficient_dumb(costs) -> np.ndarray:
    """
    Source: https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python

    Very slow for many datapoints.  Fastest for many costs, most readable

    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """

    is_efficient: np.ndarray = np.ones(costs.shape[0], dtype=bool)
    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i] > c, axis=1)) and np.all(
            np.any(costs[i + 1 :] > c, axis=1)
        )
    return is_efficient


### END ###
