#!/usr/bin/env python3

"""
PUSH A PLAN ONCE ON TWO RATINGS DIMENSIONS

For example, see the workflows directory.

For documentation, type:

$ scripts/push_plan.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict, Tuple

import os

from rdabase import (
    require_args,
    Assignment,
    write_csv,
    load_plan,
    load_data,
    load_shapes,
    load_graph,
    load_metadata,
)

from tradeoffs import *


def main() -> None:
    """Push a plan on two ratings dimensions."""

    args: argparse.Namespace = parse_args()

    pin: str = args.pin if args.pin else ""
    assert pin in ["", args.dimensions[0], args.dimensions[1]]

    # Load the data & shapes for scoring

    data: Dict[str, Dict[str, str | int]] = load_data(os.path.expanduser(args.data))
    shapes: Dict[GeoID, Any] = load_shapes(os.path.expanduser(args.shapes))
    graph: Dict[GeoID, List[GeoID]] = load_graph(os.path.expanduser(args.graph))
    metadata: Dict[str, Any] = load_metadata(args.state, os.path.expanduser(args.data))

    # Load the plan to push

    assignments: List[Assignment] = load_plan(os.path.expanduser(args.plan))

    # Push the plan once on the given dimensions

    dimensions: Tuple[str, str] = (args.dimensions[0], args.dimensions[1])

    with open(os.path.expanduser(args.log), "w") as f:
        pushed_plan: Dict[GeoID, DistrictID] = push_plan(
            assignments,
            dimensions,
            args.seed,
            data,
            shapes,
            graph,
            metadata,
            realistic_filter=not args.norealisticfilter,
            pin=pin,
            pin_tolerance=args.tolerance,
            save_at_limit=args.saveatlimit,
            logfile=f,
            verbose=args.verbose,
            debug=args.debug,
        )

    # If the plan was successfully pushed, write it to a CSV file

    if pushed_plan:
        plan: List[Dict[GeoID, DistrictID]] = [
            {"GEOID": k, "DISTRICT": v} for k, v in pushed_plan.items()
        ]
        write_csv(os.path.expanduser(args.pushed), plan, ["GEOID", "DISTRICT"])
        print(f"Status: Success for {os.path.basename(args.pushed)}")
    else:
        print(f"Status: Failure for {os.path.basename(args.pushed)}")


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
        "--pushed",
        help="Path to pushed plan CSV file",
        type=str,
    )
    parser.add_argument(
        "--dimensions", nargs="+", help="A pair of ratings dimensions", type=str
    )
    parser.add_argument(
        "--no-realistic-filter",
        dest="norealisticfilter",
        action="store_true",
        help="Disable the 'realistic' filter",
    )
    parser.add_argument(
        "--pin",
        type=str,
        default="",
        help="One of the dimensions to hold constant (optional)",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=0.05,
        help="How much the pinned dimension can vary (optional)",
    )
    parser.add_argument(
        "--save-at-limit",
        dest="saveatlimit",
        action="store_true",
        help="Save the in-progress plan at the limit",
    )
    parser.add_argument(
        "--log",
        type=str,
        help="Path to Log TXT file",
    )
    #
    parser.add_argument("--seed", type=int, help="Random seed")
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
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    # debug_defaults: Dict[str, Any] = {
    #     "state": "NC",
    #     "plan": "testdata/test_plan.csv",
    #     "dimensions": ["proportionality", "minority"],
    #     "pin": "",
    #     # "pin": "proportionality",
    #     "saveatlimit": True,
    #     "pushed": "~/Downloads/test_plan_pushed.csv",
    #     "log": "~/Downloads/test_plan_pushed_log.txt",
    #     "seed": 518,
    #     "data": "../rdabase/data/NC/NC_2020_data.csv",
    #     "shapes": "../rdabase/data/NC/NC_2020_shapes_simplified.json",
    #     "graph": "../rdabase/data/NC/NC_2020_graph.json",
    #     "verbose": True,
    # }
    # debug_defaults: Dict[str, Any] = {
    #     "state": "NC",
    #     "plan": "~/Downloads/NC/plans/NC20C_9612_plan.csv",
    #     "dimensions": ["proportionality", "competitiveness"],
    #     "pin": "proportionality",
    #     "tolerance": 0.05,
    #     "saveatlimit": True,
    #     "pushed": "~/Downloads/NC/NC20C_9612_12_00_plan.csv",
    #     "log": "~/Downloads/NC/pushed/NC20C_9612_12_00_log.txt",
    #     "seed": 518,
    #     "data": "~/Downloads/NC/data/data.csv",
    #     "shapes": "~/Downloads/NC/data/shapes.json",
    #     "graph": "~/Downloads/NC/data/graph.json",
    #     "verbose": True,
    # }
    debug_defaults: Dict[str, Any] = {
        "state": "SC",
        "plan": "../../iCloud/fileout/tradeoffs/SC-alt/plans/SC20C_3437_plan.csv",
        # "plan": "../../iCloud/fileout/tradeoffs/SC-alt/plans/SC22C_official_plan.csv",
        "dimensions": ["proportionality", "minority"],
        "norealisticfilter": True,
        "pin": "proportionality",
        "tolerance": 0.01,
        "saveatlimit": True,
        "pushed": "../../iCloud/fileout/tradeoffs/SC-alt/pushed/SC20C_3437_131_00_plan_test.csv",
        "log": "../../iCloud/fileout/tradeoffs/SC-alt/pushed/SC20C_3437_131_00_plan_test_log.txt",
        # "pushed": "../../iCloud/fileout/tradeoffs/SC-alt/pushed/SC22C_official_plan_test.csv",
        # "log": "../../iCloud/fileout/tradeoffs/SC-alt/pushed/SC22C_official_plan_push_log.txt",
        "seed": 315,
        "data": "../../iCloud/fileout/tradeoffs/SC/data/data.csv",
        "shapes": "../../iCloud/fileout/tradeoffs/SC/data/shapes.json",
        "graph": "../../iCloud/fileout/tradeoffs/SC/data/graph.json",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###