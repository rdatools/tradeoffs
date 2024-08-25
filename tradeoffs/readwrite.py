"""
READ/WRITE UTILITIES
"""

from typing import List, Dict, Callable

import warnings

warnings.warn = lambda *args, **kwargs: None

from csv import DictReader
import pandas as pd

from rdaensemble.general import ratings_dimensions

from .constants import *
from .score import is_realistic


def filter_scores(scores: Dict[str, str]) -> bool:
    """Filter out maps that don't have 'roughly equal' population or are 'unrealistic'."""

    if "population_deviation" in scores:
        population_deviation: float = float(scores["population_deviation"])
        if population_deviation > (pop_threshold * 2):
            return False

    ratings: List[int | float] = [int(scores[d]) for d in ratings_dimensions]
    if not is_realistic(ratings):
        return False

    return True


def scores_to_df(
    scores_csv: str,
    fieldnames: List[str],
    fieldtypes: List[Callable],
    *,
    filter=False,
    verbose=False,
) -> pd.DataFrame:
    """Convert ratings in a scores CSV file into a Pandas dataframe."""

    scores: List[Dict[str, str]] = []
    total: int = 0
    filtered: int = 0
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            total += 1
            if filter:
                if filter_scores(row):
                    filtered += 1
                    scores.append(row)
            else:
                scores.append(row)

    if verbose and filter:
        print()
        print(
            f"Note: Only {filtered} of {total} plans had 'roughly equal' population and were 'realistic'."  # per the DRA Notable Maps criteria.
        )
        print()

    data: List[List[str | int | float]] = []
    for score in scores:
        data.append([fieldtypes[i](score[f]) for i, f in enumerate(fieldnames)])

    df: pd.DataFrame = pd.DataFrame(data, columns=fieldnames)

    return df


def read_ratings(
    scores_csv: str,
    *,
    verbose=False,
) -> List[Dict]:
    """Read a scores CSV file & filter out the unrealistic plans."""

    ratings: List[Dict] = []
    total: int = 0
    filtered: int = 0
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            total += 1
            if filter_scores(row):
                filtered += 1

                name: str = row["map"]
                plan_ratings: List[int | float] = [
                    int(row[d]) for d in ratings_dimensions
                ]
                ratings.append({"name": name, "ratings": plan_ratings})

    if verbose:
        print()
        print(
            f"Note: Only {filtered} of {total} plans had 'roughly equal' population and were 'realistic'."  # per the DRA Notable Maps criteria.
        )
        print()

    return ratings


### END ###
