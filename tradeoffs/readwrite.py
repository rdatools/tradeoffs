"""
READ/WRITE UTILITIES
"""

from typing import List, Dict, Callable

from csv import DictReader
import pandas as pd

from rdaensemble.general import ratings_dimensions
from .score import is_realistic


def filter_scores(scores: Dict[str, str]) -> bool:
    """Filter out maps that don't have 'roughly equal' population or are 'unrealistic'."""

    threshold: float = 0.01  # TODO - Pull this out as a project-wide value
    population_deviation: float = float(scores["population_deviation"])
    if population_deviation > (threshold * 2):
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
            if filter and filter_scores(row):
                filtered += 1
                scores.append(row)
            else:
                scores.append(row)

    if verbose:
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


### END ###
