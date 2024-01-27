#!/usr/bin/env python3

"""
DEBUGG LOOPING - The Balzer looping

To run:

$ scripts/debug_looping.py

"""

import random

from typing import Any, List, Dict, NamedTuple

from rdabase import read_json, starting_seed
from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
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
    push_point,
)


class Args(NamedTuple):
    state: str
    plans: str
    frontier: str
    data: str
    shapes: str
    graph: str
    runs: int
    limit: int
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
        runs=1,  # TODO
        limit=1000,  # TODO
        verbose=True,
        debug=True,
    )

    # Load data

    data: Dict[str, Dict[GeoID, DistrictID]] = load_data(args.data)
    shapes: Dict[str, Any] = load_shapes(args.shapes)
    graph: Dict[GeoID, List[GeoID]] = load_graph(args.graph)
    metadata: Dict[str, Any] = load_metadata(args.state, args.data)

    pop_by_geoid: Dict[GeoID, int] = {k: int(v["TOTAL_POP"]) for k, v in data.items()}

    frontiers: Dict[str, Any] = read_json(args.frontier)
    ensemble: Dict[str, Any] = read_json(args.plans)
    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]

    N: int = int(metadata["D"])
    seed: int = starting_seed(args.state, N)

    #

    pushed_plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = []

    ## Get a plan and ratings for debugging ##

    frontier_key = "proportionality_compactness"  # TODO
    frontier: List[Dict[str, Any]] = frontiers["frontiers"][frontier_key]

    dimensions: Tuple[str, str] = tuple(frontier_key.split("_"))

    # TODO - Use the offset in the frontier, to get the plan in the ensemble

    p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
    name: Name = str(p["name"])
    district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore

    ##

    # Push a frontier point one or more times

    for i in range(1, args.runs + 1):
        if args.verbose:
            print()
            print(f"Iteration {i} of {args.runs}")

        plan: Plan = Plan(
            district_by_geoid,
            pop_by_geoid,
            graph,
            seed,
            verbose=args.verbose,
            debug=args.debug,
        )

        plan_name: str = f"{frontier_key}_{i:03d}"
        assignments: Dict[GeoID, DistrictID] = push_point(
            plan, dimensions, seed, verbose=args.verbose, debug=args.debug
        )
        pushed_plans.append({"name": plan_name, "plan": assignments})  # No weights.

        seed += 1

    # TODO - Save the ensemble to disk

    pass


if __name__ == "__main__":
    main()

### END ###
