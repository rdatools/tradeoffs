#!/usr/bin/env python3

"""
PUSH A PLAN ON TWO RATINGS DIMENSIONS

For example:

$ scripts/push_plan.py \
--state NC \
--plan testdata/NC_2020_Congress_HB1029.csv \
--dimensions proportionality minority \
--seed 518 \
--multiplier 1 \
--prefix NC_proportionality_minority \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--output ~/Downloads/ \
--no-debug

For documentation, type:

$ scripts/push_plan.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Tuple

import random

from rdabase import (
    require_args,
    read_json,
    read_csv,
    # load_plan, # TODO - Update this
    starting_seed,
    Assignment,
    write_csv,
)
from rdaensemble.general import ratings_dimensions
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import push_plan


def main() -> None:
    """Push a plan on two ratings dimensions."""

    args: argparse.Namespace = parse_args()

    # Load the plan to push

    assignments: List[Assignment] = load_plan(args.plan)

    # Load the data & shapes for scoring

    data: Dict[str, Dict[GeoID, DistrictID]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    # Push the plan

    dimensions: Tuple[str, str] = (args.dimensions[0], args.dimensions[1])

    pushed_plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = push_plan(
        assignments,
        dimensions,
        args.seed,
        args.multiplier,
        args.prefix,
        data,
        shapes,
        graph,
        metadata,
        verbose=args.verbose,
        debug=args.debug,
    )

    # TODO - Write the pushed plans to CSV files

    pass


def load_plan(plan_file: str) -> List[Assignment]:
    """Read a precinct-assignment file.

    TODO - Update this in rdabase
    """

    raw_assignments: List[Dict[str, str | int]] = read_csv(plan_file, [str, int])

    fields: List[str] = list(raw_assignments[0].keys())
    geoid: str = fields[0]
    district: str = fields[1]

    assignments: List[Assignment] = [
        Assignment(geoid=str(a[geoid]), district=a[district]) for a in raw_assignments
    ]

    return assignments


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Push a given plan on two ratings dimensions."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "--plan",
        type=str,
        help="The plan CSV to push",
    )
    parser.add_argument(
        "--dimensions", nargs="+", help="A pair of ratings dimensions", type=str
    )
    parser.add_argument("--seed", type=int, help="Random seed")
    parser.add_argument(
        "--multiplier", type=int, help="How many times to push the plan"
    )
    parser.add_argument(
        "--prefix",
        type=str,
        help="A prefix for the pushed plans' filenames",
    )
    #
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
    #
    parser.add_argument(
        "--output",
        default="~/Downloads/",
        help="Path to output directory",
        type=str,
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
        "plan": "testdata/NC_2020_Congress_HB1029.csv",
        "dimensions": ["proportionality", "minority"],
        "seed": 518,
        "multiplier": 1,
        "prefix": "NC_proportionality_minority",
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
        "output": "~/Downloads/",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
