#!/usr/bin/env python3

"""
DEBUGG LOOPING - The Balzer looping

To run:

$ scripts/debug_looping.py

"""

import random

from typing import Any, List, Dict, Tuple, NamedTuple

from rdabase import require_args, read_json, starting_seed, write_json
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


class Args(NamedTuple):
    state: str
    plans: str
    frontier: str
    data: str
    shapes: str
    graph: str
    pushed: str
    multiplier: int
    verbose: bool
    debug: bool


def main() -> None:
    args: Args = Args(
        state="NC",
        plans="testdata/synthetic_plans.json",
        frontier="testdata/synthetic_frontier.json",
        data="../rdabase/data/NC/NC_2020_data.csv",
        shapes="../rdabase/data/NC/NC_2020_shapes_simplified.json",
        graph="../rdabase/data/NC/NC_2020_graph.json",
        pushed="output/test_pushed_plans.json",
        multiplier=1,
        verbose=True,
        debug=True,
    )

    # Load the data & shapes for scoring

    data: Dict[str, Dict[GeoID, DistrictID]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    pop_by_geoid: Dict[GeoID, int] = {k: int(v["TOTAL_POP"]) for k, v in data.items()}

    frontiers: Dict[str, Any] = read_json(args.frontier)
    ensemble: Dict[str, Any] = read_json(args.plans)

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

    # Push the ensemble frontiers

    pushed_plans: List[
        Dict[str, Name | Weight | Dict[GeoID, DistrictID]]
    ] = push_frontiers(
        ensemble,
        frontiers,
        pop_by_geoid,
        graph,
        scorer,
        args.multiplier,
        seed,
        verbose=args.verbose,
        # debug=args.debug,
    )

    pushed_ensemble: Dict[str, Any] = ensemble_metadata(
        xx=args.state,
        ndistricts=N,
        size=len(pushed_plans),
        method="Maps pushed from the frontier points",
        repo="rdatools/tradeoffs",
    )
    pushed_ensemble["plans"] = pushed_plans

    write_json(args.pushed, pushed_ensemble)


if __name__ == "__main__":
    main()

### END ###