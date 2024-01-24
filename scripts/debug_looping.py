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

from tradeoffs import Plan, GeoID, DistrictID, DistrictOffset, Move, Name, Weight


class Args(NamedTuple):
    state: str
    plans: str
    frontier: str
    data: str
    shapes: str
    graph: str
    verbose: bool


def main() -> None:
    args: Args = Args(
        state="NC",
        plans="testdata/synthetic_plans.json",
        frontier="testdata/synthetic_frontier.json",
        data="../rdabase/data/NC/NC_2020_data.csv",
        shapes="../rdabase/data/NC/NC_2020_shapes_simplified.json",
        graph="../rdabase/data/NC/NC_2020_graph.json",
        verbose=True,
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

    ## Get a plan and ratings for debugging ##

    frontier: List[Dict[str, Any]] = frontiers["frontiers"][
        "proportionality_compactness"
    ]

    # TODO - Use the offset in the frontier, to get the plan in the ensemble

    p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
    name: Name = str(p["name"])
    district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore

    ##

    plan: Plan = Plan(
        district_by_geoid, pop_by_geoid, graph, seed, verbose=args.verbose, debug=True
    )

    # plan.to_csv("output/test_plan.csv")

    # TODO - Iterate until done.
    done: bool = True

    random_districts: List[
        Tuple[DistrictOffset, DistrictOffset]
    ] = plan.random_districts()

    if args.verbose:
        print(f"# pairs of adjacent districts: {len(random_districts)}")
        print()

    for seg_key in random_districts:
        mutations: List[Mutation] = plan.random_mutations(seg_key)
        tried_count: int = 0
        valid_count: int = 0

        if args.verbose:
            print()
            print(f"# mutations between districts {seg_key}: {len(mutations)}")

        for m in mutations:
            tried_count += 1
            if plan.is_valid_mutation(m):
                plan.mutate(m)
                valid_count += 1
                done = False

            print(f"... # remaining mutations: {len(mutations)}")

        if args.verbose:
            print(
                f"    Summary: {valid_count} of {tried_count} mutations tried were valid."
            )
            print()

    if args.verbose:
        print(plan)
        print()

    # plan.to_csv("output/test_plan.csv")

    pass


if __name__ == "__main__":
    main()

### END ###
