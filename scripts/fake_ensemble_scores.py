#!/usr/bin/env python3

"""
FAKE UP ENSEMBLE SCORES

$ scripts/fake_box_plot.py

"""

from typing import List, Dict
import random
from csv import DictReader

scores_csv: str = "sample/sample_scores.csv"

cols: List[str] = [
    "map",
    "proportionality",
    "competitiveness",
    "minority",
    "compactness",
    "splitting",
]


def wtf(scores_csv: str, cols: List[str]):
    scores: List[Dict[str, str]] = list()
    with open(scores_csv, "r", encoding="utf-8-sig") as f:
        reader: DictReader[str] = DictReader(
            f, fieldnames=None, restkey=None, restval=None, dialect="excel"
        )
        for row in reader:
            keep: Dict[str, str] = {k: row[k] for k in cols}
            scores.append(keep)

            for i in range(9):
                dup: Dict[str, str] = dict()
                for k in cols:
                    if k == "map":
                        dup[k] = str(i + 1) + keep[k][1:]
                    else:
                        offset: int = random.randint(-50, 50)
                        dup[k] = str(max(min(int(keep[k]) + offset, 100), 0))
                scores.append(dup)

    # TODO - Write the new file

    pass


wtf(scores_csv, cols)


pass

### END ###
