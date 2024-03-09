"""
TEST FIND FRONTIERS
"""

from typing import Any, Dict, List

import warnings

warnings.warn = lambda *args, **kwargs: None

import random
import pandas as pd
import numpy as np

from tradeoffs.frontiers import is_pareto_efficient_value, line_segment_hull, is_near


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

    def test_convex_hull(self) -> None:
        # Concave

        fyvalues: List[int] = [4, 2, 1]
        fxvalues: List[int] = [1, 2, 4]

        hyvalues: List[int]
        hxvalues: List[int]
        hxvalues, hyvalues = line_segment_hull(fxvalues, fyvalues, verbose=True)

        assert list(hyvalues) == [4, 1]
        assert list(hxvalues) == [1, 4]

        # Convex

        fyvalues: List[int] = [4, 3, 1]
        fxvalues: List[int] = [1, 3, 4]

        hyvalues: List[int]
        hxvalues: List[int]
        hxvalues, hyvalues = line_segment_hull(fxvalues, fyvalues, verbose=True)

        assert list(hyvalues) == [4, 3, 1]
        assert list(hxvalues) == [1, 3, 4]

    def test_is_near(self):
        assert is_near((5, 2), (10, 7))
        assert not is_near((5, 1), (10, 7))
        assert not is_near((4, 2), (10, 7))
        assert is_near((6, 3), (10, 7))
        assert is_near((10, 7), (10, 7))
        try:
            is_near((11, 7), (10, 7))
            assert False
        except:
            assert True


### END ###
