#!/usr/bin/env python3

"""
PUSH A PLAN ON TWO RATINGS DIMENSIONS

For example:

$ scripts/push_plan.py \
--state NC \
--plan testdata/NC_2020_Congress_HB1029 \
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

from typing import Any, List, Dict, Tuple, NamedTuple

import random

from rdabase import (
    require_args,
    read_json,
    read_csv,
    # load_plan, # TODO - Update this
    starting_seed,
    Assignment,
    write_json,
    write_csv,
)
from rdaensemble.general import (
    ratings_dimensions,
    plan_from_ensemble,
    make_plan,
    ensemble_metadata,
)
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import (
    GeoID,
    DistrictID,
    DistrictOffset,
    Move,
    Mutation,
    Name,
    Weight,
    Plan,
    size_1_moves,
    push_frontiers,
    Scorer,
)


def main() -> None:
    """Push a plan on two ratings dimensions."""

    args: argparse.Namespace = parse_args()

    # Load the data & shapes for scoring

    data: Dict[str, Dict[GeoID, DistrictID]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    pop_by_geoid: Dict[GeoID, int] = {k: int(v["TOTAL_POP"]) for k, v in data.items()}

    # Load the plan to push

    assignments: List[Assignment] = load_plan(args.plan)

    # Generate a repeatable random seed

    N: int = int(metadata["D"])
    seed: int = starting_seed(args.state, N)

    # Instantiate a scorer

    scorer: Scorer = Scorer(
        data,
        shapes,
        graph,
        metadata,
        verbose=args.verbose,
    )

    # Push the plan

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
        "frontier": "testdata/synthetic_frontier.json",
        "data": "../rdabase/data/NC/NC_2020_data.csv",
        "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
        "graph": "../rdabase/data/NC/NC_2020_graph.json",
        "output": "~/Downloads/",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###