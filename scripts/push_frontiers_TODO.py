#!/usr/bin/env python3

"""
PUSH FRONTIER POINTS

For example:

$ scripts/push_frontiers.py \
--state NC \
--plans testdata/synthetic_plans.json \
--frontier testdata/synthetic_frontier.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--no-debug

For documentation, type:

$ scripts/push_frontiers.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
from typing import Any, List, Dict, Tuple, Set

from csv import DictReader
import itertools

from rdabase import (
    require_args,
    Assignment,
    read_json,
    write_json,
)
from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
from rdascore import load_data, load_shapes, load_graph, load_metadata
from tradeoffs import GeoID, DistrictID, Name, Weight


def main() -> None:
    args: argparse.Namespace = parse_args()

    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    # TODO - DELETE
    # scores: List[Dict[str, str]] = read_scores(args.scores, ratings_dimensions)
    frontiers: Dict[str, Any] = read_json(args.frontier)
    frontiers = frontiers["frontiers"]

    data: Dict[str, Dict[str, str | int]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    pairs: List = list(itertools.combinations(ratings_dimensions, 2))
    for dd in pairs:
        d1: int = ratings_dimensions.index(dd[0])
        d2: int = ratings_dimensions.index(dd[1])

        pair_key: str = f"{dd[0]}_{dd[1]}"
        pair_key = "proportionality_compactness"  # TODO - DEBUG

        for pt in frontiers[pair_key]:
            # Get a frontier point & plan
            map_id: str = pt["map"]
            map_id = "057_591"  # TODO - DEBUG
            ratings: List[int] = pt["ratings"]

            pt_to_push: Tuple[int, int] = (ratings[d1], ratings[d2])

            plan_item: Dict[
                str, str | float | Dict[GeoID, DistrictID]
            ] = plan_from_ensemble(map_id, ensemble)
            plan_dict: Dict[GeoID, DistrictID] = plan_item["plan"]  # type: ignore
            assignments: List[Assignment] = make_plan(plan_dict)
            plan_to_push: List[Dict[GeoID, DistrictID]] = [
                {"GEOID": a.geoid, "DISTRICT": a.district} for a in assignments
            ]

            #

            district_by_geoid: Dict[GeoID, DistrictID] = index_plan(plan_to_push)
            geoids_by_district: Dict[DistrictID, Set[GeoID]] = invert_plan(plan_to_push)

            pass  # TODO - DEBUG

        break  # TODO - DEBUG

    pass  # TODO - DEBUG


def index_plan(plan: List[Dict[GeoID, DistrictID]]) -> Dict[GeoID, DistrictID]:
    """Index districts by geoid."""

    indexed: Dict[GeoID, DistrictID] = {}

    for row in plan:
        geoid: str = str(row["GEOID"])
        district: DistrictID = row["DISTRICT"]

        indexed[geoid] = district

    return indexed


def invert_plan(plan: List[Dict[GeoID, DistrictID]]) -> Dict[DistrictID, Set[GeoID]]:
    """Return geoids by district."""

    inverted: Dict[DistrictID, Set[GeoID]] = {}

    for row in plan:
        geoid: str = str(row["GEOID"])
        district: DistrictID = row["DISTRICT"]

        if district not in inverted:
            inverted[district] = set()

        inverted[district].add(geoid)

    return inverted


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a collection of random maps."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--plans",
        type=str,
        help="Ensemble of plans to score in a JSON file",
    )
    # TODO - DELETE
    # parser.add_argument(
    #     "--scores",
    #     type=str,
    #     help="A CSV ensemble of scores including ratings to plot",
    # )
    parser.add_argument(
        "--frontier",
        type=str,
        help="Frontier maps JSON file",
    )
    parser.add_argument(
        "--data",
        type=str,
        help="Data file",
    )
    parser.add_argument(
        "--shapes",
        type=str,
        help="Shapes abstract file",
    )
    parser.add_argument(
        "--graph",
        type=str,
        help="Graph file",
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "state": "NC",
        "plans": "testdata/synthetic_plans.json",
        # TODO - DELETE
        # "scores": "testdata/synthetic_ratings.csv",  # Only has map name & ratings
        "frontier": "testdata/synthetic_frontier.json",
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###