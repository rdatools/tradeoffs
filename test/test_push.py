#!/usr/bin/env python3

"""
TEST IS_BETTER COMPARE FUNCTIONS
"""

from tradeoffs.push import make_better_fn
from testutils import *


class TestCompareFunctions:
    def test_two_dimensions(self) -> None:
        is_better = make_better_fn()
        assert is_better((50.0, 50.0), (51.0, 50.0)) is True
        assert is_better((50.0, 50.0), (50.0, 51.0)) is True
        assert is_better((50.0, 50.0), (51.0, 51.0)) is True
        assert is_better((50.0, 50.0), (50.0, 50.0)) is False
        assert is_better((50.0, 50.0), (49.0, 50.0)) is False
        assert is_better((50.0, 50.0), (50.0, 49.0)) is False
        assert is_better((50.0, 50.0), (49.0, 49.0)) is False

    def test_one_dimension(self) -> None:
        is_better = make_better_fn(constrain=0, anchor=50.0, tolerance=0.01)
        assert is_better((50.0, 50.0), (50.0, 50.0)) is False
        assert is_better((50.0, 50.0), (50.0, 51.0)) is True
        assert is_better((50.0, 50.0), (50.1, 51.0)) is True
        assert is_better((50.0, 50.0), (49.9, 51.0)) is True

        assert is_better((50.0, 50.0), (52.0, 51.0)) is False
        assert is_better((50.0, 50.0), (48.0, 51.0)) is False


### END ###
