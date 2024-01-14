#!/usr/bin/env python3

"""
DEBUGGING SCRIPT
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

    ep: EPlan = EPlan(
        district_by_geoid, pop_by_geoid, graph, seed, verbose=args.verbose
    )

    random_districts: List[
        Tuple[DistrictOffset, DistrictOffset]
    ] = ep.random_districts()

    if args.verbose:
        print(f"... # pairs of adjacent districts: {len(random_districts)}")

    for pair in random_districts:
        # TODO - Convert the underlying representation to a list?
        d1_features: List[Offset] = list(ep.district_features(pair[0]))
        d2_features: List[Offset] = list(ep.district_features(pair[1]))

        moves_from_one: List[Move]
        moves_from_two: List[Move]
        moves_from_one, moves_from_two = ep.random_moves(pair)

        if args.verbose:
            print(
                f"... # moves: {pair[0]} -> {pair[1]} = {len(moves_from_one)} | {pair[1]} -> {pair[0]} = {len(moves_from_two)}"
            )

        # TODO - Add the logic to alternate betwee the lists and end with the shortest one
        for move in moves_from_one:
            feature: Offset = move.feature
            district: DistrictOffset = move.from_district

            proposed: List[
                Offset
            ] = d1_features.copy()  # TODO - The list of features has change with moves!
            proposed.remove(feature)

            if not ep._is_connected(proposed):
                if args.verbose:
                    print(
                        f"...... district {district} would not be connected, if feature {feature} were removed!"
                    )

    # ep.to_csv("output/test_plan.csv")

    pass


if __name__ == "__main__":
    main()

### END ###
