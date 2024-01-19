"""
FRONTIER HELPERS
"""

from typing import Any, Dict, List, Callable

import numpy as np
import pandas as pd
import itertools

from rdaensemble.general import ratings_dimensions


def find_frontiers(ratings: pd.DataFrame, fn: Callable) -> Dict[str, List[Dict]]:
    """Find the frontiers for a ratings dataframe."""

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))
    frontiers: Dict[str, List[Dict]] = {}

    for p in pairs:
        label: str = f"{p[0]}_{p[1]}"
        frontiers[label] = []

        subset: pd.DataFrame = ratings[list(p)]
        is_frontier: np.ndarray = fn(subset.to_numpy())

        maps: List[str] = []
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

        d1: int = ratings_dimensions.index(p[0])
        d2: int = ratings_dimensions.index(p[1])
        frontiers[label] = sorted(
            frontiers[label],
            key=lambda d: (d["ratings"][d1], d["ratings"][d2]),
            reverse=True,
        )

    return frontiers


def is_pareto_efficient_cost(costs: np.ndarray[Any, Any]) -> np.ndarray:
    """Pareto efficient costs. Smaller is better."""

    is_efficient: np.ndarray = np.ones(costs.shape[0], dtype=bool)
    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i] > c, axis=1)) and np.all(
            np.any(costs[i + 1 :] > c, axis=1)
        )
    return is_efficient


def is_pareto_efficient_value(values: np.ndarray[Any, Any]) -> np.ndarray:
    """Pareto efficient values. Bigger is better."""

    is_efficient: np.ndarray = np.ones(values.shape[0], dtype=bool)
    for i, v in enumerate(values):
        is_efficient[i] = np.all(np.any(values[:i] < v, axis=1)) and np.all(
            np.any(values[i + 1 :] < v, axis=1)
        )
    return is_efficient


# Modeled after this from:
# https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python


def is_pareto_efficient_dumb(costs: np.ndarray[Any, Any]) -> np.ndarray:
    """
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
