#!/usr/bin/env python3

"""
DEBUGG LOOPING - The Balzer looping

To run:

$ scripts/debug_looping.py

"""

from typing import Any, List, Dict, NamedTuple

from rdabase import read_json, starting_seed
from rdaensemble.general import ratings_dimensions, plan_from_ensemble, make_plan
from rdascore import load_data, load_shapes, load_graph, load_metadata

from tradeoffs import *  # TODO


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

    ep: Plan = Plan(district_by_geoid, pop_by_geoid, graph, seed)

    random_districts: List[
        Tuple[DistrictOffset, DistrictOffset]
    ] = ep.random_districts()

    if args.verbose:
        print(f"... # pairs of adjacent districts: {len(random_districts)}")

    for district_one, district_two in random_districts:
        moves_from_one: List[Move]
        moves_from_two: List[Move]
        moves_from_one, moves_from_two = ep.random_moves((district_one, district_two))

        n_moves_from_one: int = len(moves_from_one)
        n_moves_from_two: int = len(moves_from_two)

        n_valid_moves_from_one: int = 0
        n_valid_moves_from_two: int = 0

        if args.verbose:
            print(
                f"... # moves: {district_one} -> {district_two} = {n_moves_from_one} | {district_two} -> {district_one} = {n_moves_from_one}"
            )

        # Alternate between the two lists of moves, to try to maintain population balance.

        done: bool = False
        while True:
            move: Optional[Move] = None

            # TODO - Collapse these two loops into one loop, that alternates between the two lists of moves.
            # TODO - Randomize the order of the two lists

            # Try a move from district_one to district_two, until successful.

            while True:
                if len(moves_from_one) == 0:
                    done = True
                    break

                move = moves_from_one.pop()
                if not ep.is_valid_move(move):
                    if args.verbose:
                        print(
                            f"...... district {move.from_district} would not be valid, if features ({move.features}) were moved!"
                        )
                else:
                    n_valid_moves_from_one += 1

            pass  # TODO - Move the features ...

            # Try a move from district_two to district_one, until successful.

            while True:
                if len(moves_from_two) == 0:
                    done = True
                    break

                move = moves_from_two.pop()
                if not ep.is_valid_move(move):
                    if args.verbose:
                        print(
                            f"...... district {move.from_district} would not be valid, if features ({move.features}) were moved!"
                        )
                else:
                    n_valid_moves_from_two += 1

            pass  # TODO - Move the features ...

            if done:
                break

        if args.verbose:
            print(
                f"...... summary: {district_one} -> {district_two} = {n_valid_moves_from_one} of {n_moves_from_one} are valid."
            )
            print(
                f"......          {district_two} -> {district_one} = {n_valid_moves_from_two} of {n_moves_from_two} are valid."
            )

    # ep.to_csv("output/test_plan.csv")

    pass


if __name__ == "__main__":
    main()

### END ###
