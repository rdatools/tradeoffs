"""
PUSH A FRONTIER POINT
"""

from typing import Callable, Dict, List, Tuple

from rdaensemble.general import ratings_dimensions, ratings_indexes

from .plan import Plan, Mutation, Move, BorderKey, size_1_moves
from .datatypes import GeoID, DistrictID, DistrictOffset, Move, Mutation, Name, Weight


def push_point(
    plan: Plan,
    dimensions: Tuple[str, str],
    seed: int,
    *,
    verbose: bool = False,
    debug: bool = False,
) -> Dict[GeoID, DistrictID]:
    """Push a frontier point on two ratings dimensions."""

    # Apply a sequence of swap generators

    generators: Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]] = [
        size_1_moves
    ]

    for generator in generators:
        if verbose:
            print()
            print(f"Generator: {generator.__name__}")

        # Keep mutating the plan, until no swaps are made.

        while True:
            done: bool = True

            random_adjacent_districts: List[
                BorderKey
            ] = plan.random_adjacent_districts()

            if verbose:
                print()
                print(
                    f"# pairs of adjacent districts: {len(random_adjacent_districts)}"
                )

            for seg_key in random_adjacent_districts:
                mutations: List[Mutation] = plan.random_mutations(seg_key, generator)
                tried_count: int = 0
                valid_count: int = 0

                if verbose:
                    d1, d2 = seg_key
                    d1_id: DistrictID = plan.district_ids[d1]
                    d2_id: DistrictID = plan.district_ids[d2]

                    print()
                    print(f"{len(mutations)} mutations {d1}/{d1_id} <-> {d2}/{d2_id}:")

                for m in mutations:
                    tried_count += 1
                    plan.mutate(m)

                    if plan.is_valid_plan(seg_key):  # TODO - And if it's better
                        valid_count += 1
                        done = False

                        if verbose:
                            print("... Success!")
                    else:
                        plan.undo()

                    if verbose:
                        print()
                        print(
                            f"... # remaining mutations: {len(mutations) - tried_count}"
                        )

                if verbose:
                    print(
                        f"... Summary: {valid_count} of {tried_count} mutations tried were valid."
                    )
                    print()

            break  # TODO - One pass for debugging

        if verbose:
            print(plan)
            print()

    assignments: Dict[GeoID, DistrictID] = plan.to_dict()

    return assignments


### END ###
