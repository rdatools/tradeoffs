"""
TEST FIND FRONTIERS
"""

from typing import Any, Dict, List

import random
import pandas as pd
import numpy as np

from tradeoffs import is_pareto_efficient_value


class TestFindFrontiers:
    def test_find_frontiers(self) -> None:
        x: int = 10
        y: int = 10
        d: int = 5

        points: List[List[int]] = [
            [
                0,
                x,
                y,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                1,
                x + d,
                y + d,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                2,
                x + d - 1,
                y + d - 1,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                8,
                x + d,
                y + d - 1,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                9,
                x + d - 1,
                y + d,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                3,
                x,
                y + d,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                4,
                x + d,
                y,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                5,
                x - d,
                y + d - 1,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                6,
                x - d,
                y - d,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
            [
                7,
                x + d - 1,
                y - d,
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
                random.randint(x - d, x + d),
            ],
        ]
        expected: List[int] = [1]

        random.shuffle(points)

        df: pd.DataFrame = pd.DataFrame(points)
        subset: pd.DataFrame = df.iloc[:, 1:3]
        is_frontier: np.ndarray = is_pareto_efficient_value(subset.to_numpy())

        keep: List[int] = [i for i, f in enumerate(is_frontier) if f]
        frontier: pd.DataFrame = df.iloc[keep]

        actual: List[int] = list(frontier[frontier.columns[0]])

        assert len(actual) == len(expected)
        for a in actual:
            assert a in expected


### END ###
