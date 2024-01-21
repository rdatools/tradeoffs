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

    plan: Plan = Plan(district_by_geoid, pop_by_geoid, graph, seed)

    random_districts: List[
        Tuple[DistrictOffset, DistrictOffset]
    ] = plan.random_districts()

    if args.verbose:
        print(f"# pairs of adjacent districts: {len(random_districts)}")

    moves_made: int = 0
    for d1, d2 in random_districts:
        districts: List[DistrictOffset] = [d1, d2]

        moves: List[List[Move]] = plan.random_moves((d1, d2))
        list_lengths: List[int] = [len(moves[0]), len(moves[1])]
        tried_counts: List[int] = [0, 0]
        valid_counts: List[int] = [0, 0]

        one: int = random.randint(0, 1)  # Start w/ one list at random
        two: int = 1 - one
        move_lists: List[int] = [one, two]

        if args.verbose:
            print(
                f"# moves: {districts[0]} -> {districts[1]} = {list_lengths[0]} | {districts[1]} -> {districts[0]} = {list_lengths[1]}"
            )

        # Alternate between the two lists of moves, to try to maintain population balance.
        # Stop when either list is empty.

        done: bool = False
        while True:
            for i in move_lists:
                j: int = 1 - i

                while True:
                    print(
                        f"... # remaining moves: {districts[0]} = {len(moves[0])} | {districts[1]} = {len(moves[1])}"
                    )
                    if len(moves[i]) == 0:
                        done = True
                        break

                    move: Move = moves[i].pop()
                    tried_counts[i] += 1

                    if not plan.is_valid_move(move):
                        if args.verbose:
                            print(
                                f"... district {move.from_district} would not be valid, if features ({move.features}) were moved!"
                            )
                        continue
                    else:
                        plan.mutate(move)
                        moves_made += 1
                        valid_counts[i] += 1
                        break

                if done:
                    break

            if done:
                break

        if args.verbose:
            print(
                f"    Summary: {districts[0]} -> {districts[1]} = {valid_counts[0]} of {tried_counts[0]} tried were valid."
            )
            print(
                f"             {districts[1]} -> {districts[0]} = {valid_counts[1]} of {tried_counts[1]} tried were valid."
            )
            print()

    if args.verbose:
        print(f"# moves made: {moves_made}")
        print()

    # plan.to_csv("output/test_plan.csv")

    pass


if __name__ == "__main__":
    main()

### END ###
