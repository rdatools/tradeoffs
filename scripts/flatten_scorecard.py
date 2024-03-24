#!/usr/bin/env python3

"""
FLATTEN THE map-analytics.json SCORECARD FROM DRA INTO A ONE ROW CSV

For example, see the workflows directory.

For documentation, type:

$ scripts/flatten_scorecard.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Any, List, Dict

from rdabase import require_args, read_json, write_csv

from tradeoffs import (
    cull_partisan_metrics,
    cull_minority_metrics,
    cull_compactness_metrics,
    cull_splitting_metrics,
    cull_ratings,
)


def main() -> None:
    """Flatten a DRA scorecard into a single row of analytics."""

    args: argparse.Namespace = parse_args()

    data: Dict[str, Any] = read_json(args.export)

    partisan_metrics: Dict[str, float] = cull_partisan_metrics(data)
    minority_metrics: Dict[str, float] = cull_minority_metrics(data)
    compactness_metrics: Dict[str, float] = cull_compactness_metrics(data)
    splitting_metrics: Dict[str, float] = cull_splitting_metrics(data)
    ratings: Dict[str, int] = cull_ratings(data)

    scorecard: Dict[str, Any] = {}
    scorecard["map"] = args.name
    # scorecard["population_deviation"] = deviation # Not exported
    scorecard.update(partisan_metrics)
    scorecard.update(minority_metrics)
    scorecard.update(compactness_metrics)
    scorecard.update(splitting_metrics)
    scorecard.update(ratings)

    scores: List[Dict] = [scorecard]
    fields: List[str] = list(scores[0].keys())
    write_csv(args.scores, scores, fields, precision="{:.4f}")


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Flatten a DRA scorecard into a single row of analytics."
    )

    parser.add_argument(
        "--export",
        type=str,
        help="A map-analytics.json export file from DRA",
    )
    parser.add_argument(
        "--name",
        type=str,
        help="A name for the map",
    )
    parser.add_argument(
        "--scores",
        type=str,
        help="The flattened scores for the map a CSV file",
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
        "export": "testdata/test_focus_analytics.json",
        "name": "NC_2024_Congressional",
        "scores": "testdata/test_focus_scores.csv",
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
