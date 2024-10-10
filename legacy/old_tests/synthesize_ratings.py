#!/usr/bin/env python3

"""
SYNTHESIZE RATINGS FOR 1,000 PLANS

$ test/synthesize_ratings.py

"""

from typing import List, Dict
import random
from csv import DictReader

import os

from rdabase import write_csv


def main() -> None:
    """Synthesize ratings for a 1,000 plan ensemble."""

    scores_csv: str = "~/iCloud/fileout/ensembles/NC20C_RMfRST_100_scores.csv"
    ratings_csv: str = "testdata/test_scores.csv"

    cols: List[str] = [
        "map",
        "proportionality",
        "competitiveness",
        "minority",
        "compactness",
        "splitting",
    ]

    spread: List[int] = [10, 10, 10, 10, 10]
    delta: List[int] = [0, 0, 0, 0, 30]

    scores: List[Dict[str, str]] = []

    with open(os.path.expanduser(scores_csv), "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            ratings: Dict[str, str] = {k: row[k] for k in cols}
            scores.append(ratings)

            for i in range(9):
                dup: Dict[str, str] = {}
                dup["map"] = str(i + 1) + row["map"][1:]
                for j, k in enumerate(cols[1:]):
                    mid: int = int(ratings[k]) + delta[j]
                    dup[k] = str(
                        random.randint(
                            max(mid - spread[j], 0), min(mid + spread[j], 100)
                        )
                    )
                scores.append(dup)

    write_csv(ratings_csv, scores, cols)


if __name__ == "__main__":
    main()

### END ###
