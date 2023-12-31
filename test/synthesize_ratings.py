#!/usr/bin/env python3

"""
FAKE UP ENSEMBLE SCORES

$ test/synthesize_ratings.py

"""

from typing import List, Dict
import random
from csv import DictReader

import os

scores_csv: str = "~/iCloud/fileout/ensembles/NC20C_RMfRST_100_scores.csv"

cols: List[str] = [
    "map",
    "proportionality",
    "competitiveness",
    "minority",
    "compactness",
    "splitting",
]


def synthesize_ratings(
    scores_csv: str,
    cols: List[str],
    *,
    spread: List[int] = [10, 10, 10, 10, 10],
    delta: List[int] = [0, 0, 0, 0, 0, 20]
):
    """Synthesize ratings for a 1,000 plan ensemble."""

    scores: List[Dict[str, str]] = list()

    with open(os.path.expanduser(scores_csv), "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            ratings: Dict[str, str] = {k: row[k] for k in cols}
            scores.append(ratings)

            for i in range(9):
                dup: Dict[str, str] = dict()
                dup["map"] = str(i + 1) + row["map"][1:]
                for j, k in enumerate(cols[1:]):
                    mid: int = int(ratings[k]) + delta[j]
                    dup[k] = str(
                        random.randint(
                            max(mid - spread[j], 0), min(mid + spread[j], 100)
                        )
                    )
                scores.append(dup)

    # TODO - Write the new file

    pass


synthesize_ratings(scores_csv, cols)


pass

### END ###
