#!/usr/bin/env python3

"""
TEST IS_BETTER COMPARE FUNCTIONS
"""

from tradeoffs.push import make_better_fn
from testutils import *


class TestCompareFunctions:
    def test_two_dimensions(self) -> None:
        is_better = make_better_fn()
        assert is_better((0.0, 0.0), (0.1, 0.0)) is True
        assert is_better((0.0, 0.0), (0.0, 0.1)) is True
        assert is_better((0.0, 0.0), (0.1, 0.1)) is True
        assert is_better((0.0, 0.0), (0.0, 0.0)) is False

    def test_one_dimension(self) -> None:
        is_better = make_better_fn(constrain=0, anchor=1.0)
        assert is_better((1.0, 1.0), (1.0, 1.0)) is False
        assert is_better((1.0, 1.0), (1.0, 1.1)) is True
        assert is_better((1.0, 1.0), (1.005, 1.1)) is True
        assert is_better((1.0, 1.0), (0.995, 1.1)) is True

        assert is_better((1.0, 1.0), (1.015, 1.1)) is False
        assert is_better((1.0, 1.0), (0.985, 1.1)) is False


### END ###
