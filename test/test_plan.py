#!/usr/bin/env python3

"""
TEST PLAN CLASS
"""

import random
from typing import List, Dict, Tuple, Set

from rdabase import Assignment
from tradeoffs import GeoID, DistrictID, FeatureOffset, DistrictOffset, Plan

from tradeoffs.plan import *
from testutils import *


class TestPlan:
    def test_grid_plam(self) -> None:
        """Test border segments."""

        # Setup

        assignments: List[Assignment] = [
            Assignment(geoid="A1", district=2),
            Assignment(geoid="B1", district=2),
            Assignment(geoid="C1", district=1),
            Assignment(geoid="D1", district=1),
            Assignment(geoid="A2", district=2),
            Assignment(geoid="B2", district=2),
            Assignment(geoid="C2", district=1),
            Assignment(geoid="D2", district=1),
            Assignment(geoid="A3", district=3),
            Assignment(geoid="B3", district=3),
            Assignment(geoid="C3", district=4),
            Assignment(geoid="D3", district=4),
            Assignment(geoid="A4", district=3),
            Assignment(geoid="B4", district=3),
            Assignment(geoid="C4", district=4),
            Assignment(geoid="D4", district=4),
        ]  # Four square districts, ea. with four features

        border_keys: List[Tuple[DistrictID, DistrictID]] = [
            (1, 2),
            (1, 4),
            (2, 3),
            (3, 4),
        ]
        border_segments = {
            (1, 2): {1: {"C1", "C2"}, 2: {"B1", "B2"}},
            (1, 4): {1: {"C2", "D2"}, 4: {"C3", "D3"}},
            (2, 3): {2: {"A2", "B2"}, 3: {"A3", "B3"}},
            (3, 4): {3: {"B3", "B4"}, 4: {"C3", "C4"}},
        }

        pop_by_geoid: Dict[GeoID, int] = {a.geoid: 1 for a in assignments}

        graph: Dict[GeoID, List[GeoID]] = {
            "A1": ["B1", "A2"],
            "B1": ["A1", "C1", "B2"],
            "C1": ["B1", "D1", "C2"],
            "D1": ["C1", "D2"],
            "A2": ["A1", "B2", "A3"],
            "B2": ["A2", "C2", "B1", "B3"],
            "C2": ["B2", "D2", "C1", "C3"],
            "D2": ["C2", "D1", "D3"],
            "A3": ["B3", "A2", "A4"],
            "B3": ["A3", "C3", "B2", "B4"],
            "C3": ["B3", "D3", "C2", "C4"],
            "D3": ["C3", "D2", "D4"],
            "A4": ["A3", "B4"],
            "B4": ["A4", "C4", "B3"],
            "C4": ["B4", "D4", "C3"],
            "D4": ["C4", "D3"],
        }

        seed: int = 0

        #

        for _ in range(10):
            district_by_geoid: Dict[GeoID, DistrictID] = {
                a.geoid: a.district for a in assignments
            }
            plan: Plan = Plan(district_by_geoid, pop_by_geoid, graph, seed)

            assert True

            # indexed_border_keys: List[Tuple[DistrictOffset, DistrictOffset]] = []
            # for x, y in border_keys:
            #     d1: DistrictOffset = plan._district_indexes[x]
            #     d2: DistrictOffset = plan._district_indexes[y]
            #     seg_key: Tuple[DistrictOffset, DistrictOffset] = segment_key(d1, d2)
            #     indexed_border_keys.append(seg_key)

            # indexed_border_segs = {}
            # for k, v in border_segments.items():
            #     x, y = k

            #     x_offsets = [plan._feature_indexes[geoid] for geoid in v[x]]
            #     y_offsets = [plan._feature_indexes[geoid] for geoid in v[y]]

            #     d1: DistrictOffset = plan._district_indexes[x]
            #     d2: DistrictOffset = plan._district_indexes[y]

            #     seg_key: Tuple[DistrictOffset, DistrictOffset] = segment_key(d1, d2)

            #     indexed_border_segs[seg_key] = (
            #         {d1: set(x_offsets), d2: set(y_offsets)}
            #         if d1 < d2
            #         else {d2: set(y_offsets), d1: set(x_offsets)}
            #     )

            # Tests

            # TODO


### END ###
