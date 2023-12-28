"""
READ/WRITE UTILITIES
"""

from typing import List, Dict, Callable

from csv import DictReader
import pandas as pd


def scores_to_df(
    scores_csv: str, fieldnames: List[str], fieldtypes: List[Callable]
) -> pd.DataFrame:
    """Convert ratings in a scores CSV file into a Pandas dataframe."""

    scores: List[Dict[str, str]] = list()
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            scores.append(row)

    data: List[List[str | int | float]] = list()
    for score in scores:
        data.append([fieldtypes[i](score[f]) for i, f in enumerate(fieldnames)])

    df: pd.DataFrame = pd.DataFrame(data, columns=fieldnames)

    return df


### END ###
