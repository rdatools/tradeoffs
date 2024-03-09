"""
FRONTIER HELPERS
"""

from typing import Any, Dict, List, Tuple, Callable

import numpy as np
import pandas as pd
from scipy.spatial import ConvexHull
import itertools

from rdaensemble.general import ratings_dimensions

### PARETO FRONTIERS ###


def find_frontiers(
    ratings: pd.DataFrame, fn: Callable, *, verbose: bool = False
) -> Dict[str, List[Dict]]:
    """Find the frontiers for a ratings dataframe."""

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))
    frontiers: Dict[str, List[Dict]] = {}

    for p in pairs:
        d1: int = ratings_dimensions.index(p[0])
        d2: int = ratings_dimensions.index(p[1])

        # Find the unique pairs of ratings & the associated maps

        unique_points: List[List[int]] = []
        maps_by_point: Dict[Tuple[int, int], List[str]] = {}
        for i, df_row in ratings.iterrows():
            row = df_row.values.flatten().tolist()  # type: ignore
            name: str = row.pop(0)
            values: Tuple[int, int] = (row[d1], row[d2])

            if values not in maps_by_point:
                unique_points.append(list(values))
                maps_by_point[values] = []

            maps_by_point[values].append(name)

        # Find the frontier points

        subset: pd.DataFrame = pd.DataFrame(unique_points, columns=list(p))
        is_frontier: np.ndarray = fn(subset.to_numpy())

        # Collect the maps associated with those frontier points

        maps: List[str] = []
        for i, is_efficient in enumerate(is_frontier):
            if is_efficient:
                values = tuple(subset.iloc[i].values.flatten().tolist())  # type: ignore
                unique_point: Tuple[int, int] = (values[0], values[1])
                for m in maps_by_point[unique_point]:
                    maps.append(m)

        # Add each map to the frontier along with the ratings

        label: str = f"{p[0]}_{p[1]}"
        frontiers[label] = []

        for m in maps:
            row = (
                ratings.loc[ratings["map"] == m, ["map"] + ratings_dimensions]
                .values.flatten()
                .tolist()
            )
            name: str = row.pop(0)
            point: List[int] = [int(r) for r in row]
            frontiers[label].append({"map": name, "ratings": point})

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


### CONVEX HULL ###


def line_segment_hull(
    xvalues: List[int], yvalues: List[int], *, verbose=False
) -> Tuple[List[int], List[int]]:
    """
    Given the x & y values for the points of a ratings frontier line segment,
    return the corresponding partial convex hull.

    Add 'interior' points so the hulling will 'push out' (NE) the input line segment.
    """

    xinterior: List[int] = [0, max(xvalues), 0]
    yinterior: List[int] = [0, 0, max(yvalues)]

    input_points = np.array([x for x in zip(xinterior + xvalues, yinterior + yvalues)])
    hull = ConvexHull(input_points)
    hull_indices = np.unique(hull.simplices.flatten())
    hull_points = [input_points[i] for i in hull_indices]

    hull = [[int(pt[0]), int(pt[1])] for pt in hull_points]
    unzipped = list(zip(*hull[3:]))

    if verbose and (len(hull) < len(input_points)):
        print(
            f"Fewer points on the partial convex hull ({len(hull)-3}) than on the input line segment ({len(input_points)-3})."
        )

    return unzipped[0], unzipped[1]


### ZONES NEAR FRONTIERS ###


def is_near(pt: Tuple[int, int], f_pt: Tuple[int, int], *, delta: int = 5) -> bool:
    """Is a pair ratings 'near' a given frontier point?"""

    assert not (pt[0] > f_pt[0] and pt[1] > f_pt[1])

    result: bool = ((f_pt[0] - pt[0]) <= delta) and ((f_pt[1] - pt[1]) <= delta)

    return result


def is_near_any(
    pt: Tuple[int, int], f_pts: List[Tuple[int, int]], *, delta: int = 5
) -> bool:
    """Is a pair ratings 'near' any given frontier point?"""

    for f_pt in f_pts:
        if is_near(pt, f_pt, delta=delta):
            return True

    return False


### END ###
