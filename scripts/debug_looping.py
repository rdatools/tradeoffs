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
    Name,
    Weight,
    Plan,
    size_1_moves,
)


class Args(NamedTuple):
    state: str
    plans: str
    frontier: str
    data: str
    shapes: str
    graph: str
    iterations: int
    limit: int
    verbose: bool


def main() -> None:
    args: Args = Args(
        state="NC",
        plans="testdata/synthetic_plans.json",
        frontier="testdata/synthetic_frontier.json",
        data="../rdabase/data/NC/NC_2020_data.csv",
        shapes="../rdabase/data/NC/NC_2020_shapes_simplified.json",
        graph="../rdabase/data/NC/NC_2020_graph.json",
        iterations=2,  # TODO
        limit=1000,  # TODO
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

    # Starting plan
    # plan.to_csv("output/test_plan.csv")

    # Push the frontier point a number of times

    for i in range(1, args.iterations + 1):
        if args.verbose:
            print()
            print(f"Iteration {i} of {args.iterations}")

        # Apply a sequence of swap generators

        generators: Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]] = [
            size_1_moves
        ]

        for generator in generators:
            if args.verbose:
                print()
                print(f"Generator: {generator.__name__}")

            # Iterate until done.

            while True:
                done: bool = True

                random_adjacent_districts: List[
                    BorderKey
                ] = plan.random_adjacent_districts()

                if args.verbose:
                    print()
                    print(
                        f"# pairs of adjacent districts: {len(random_adjacent_districts)}"
                    )

                for seg_key in random_adjacent_districts:
                    mutations: List[Mutation] = plan.random_mutations(
                        seg_key, generator
                    )
                    tried_count: int = 0
                    valid_count: int = 0

                    if args.verbose:
                        d1, d2 = seg_key
                        d1_id: DistrictID = plan.district_ids[d1]
                        d2_id: DistrictID = plan.district_ids[d2]

                        print()
                        print(
                            f"{len(mutations)} mutations {d1}/{d1_id} <-> {d2}/{d2_id}:"
                        )

                    for m in mutations:
                        tried_count += 1
                        plan.mutate(m)

                        if plan.is_valid_plan(seg_key):  # TODO - And if it's better
                            valid_count += 1
                            done = False

                            if args.verbose:
                                print("... Success!")
                        else:
                            plan.undo()

                        if args.verbose:
                            print()
                            print(
                                f"... # remaining mutations: {len(mutations) - tried_count}"
                            )

                    if args.verbose:
                        print(
                            f"... Summary: {valid_count} of {tried_count} mutations tried were valid."
                        )
                        print()

                break  # TODO - One pass for debugging

            # TODO - Save the modified plan
            # plan.to_csv("output/test_plan.csv")

            if args.verbose:
                print(plan)
                print()

    pass


if __name__ == "__main__":
    main()

### END ###
