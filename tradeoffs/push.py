"""
PUSH A FRONTIER POINT
"""

from typing import Callable, Dict, List, Tuple

from rdabase import time_function
from rdaensemble.general import ratings_dimensions, ratings_indexes

from .datatypes import GeoID, DistrictID, DistrictOffset, BorderKey, Move, Mutation
from .plan import Plan, size_1_moves
from .score import Scorer


@time_function
def push_point(
    plan: Plan,
    scorer: Scorer,
    dimensions: Tuple[str, str],
    *,
    verbose: bool = False,
    debug: bool = False,
) -> Dict[GeoID, DistrictID]:
    """Push a frontier point on two ratings dimensions."""

    limit: int = 1000

    generators: Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]] = [
        size_1_moves
    ]  # Swap/mutation generators

    for generator in generators:
        if debug:
            print()
            print(f"Generator: {generator.__name__}")

        npass: int = 1
        while True:
            if npass > limit:
                raise RuntimeError(f"Iteration threshold ({limit}) exceeded.")
            if verbose:
                print(f"Pass {npass} of {limit}")

            stable: bool = sweep_once(
                plan,
                scorer,
                dimensions,
                generator=generator,
                verbose=verbose,
                debug=debug,
            )

            if stable:
                break

            npass += 1

    assignments: Dict[GeoID, DistrictID] = plan.to_dict()

    return assignments


@time_function
def sweep_once(
    plan: Plan,
    scorer: Scorer,
    dimensions: Tuple[str, str],
    *,
    generator: Callable[
        [BorderKey, Plan], Tuple[List[Move], List[Move]]
    ] = size_1_moves,
    verbose: bool = False,
    debug: bool = False,
) -> bool:
    """
    Sweep across random pairs of adjacent districts applying random mutations
    that improve the plan on one or both ratings dimensions.
    """

    prev_measures: Tuple[float, float] = scorer.measure_dimensions(
        plan.to_assignments(), dimensions
    )
    next_measures: Tuple[float, float]

    if verbose:
        print(f"Starting #'s: {dimensions} = {prev_measures}", end="\n")

    random_adjacent_districts: List[BorderKey] = plan.random_adjacent_districts()

    if debug:
        print()
        print(f"# pairs of adjacent districts: {len(random_adjacent_districts)}")

    stable: bool = True
    for seg_key in random_adjacent_districts:
        mutations: List[Mutation] = plan.random_mutations(seg_key, generator)
        tried: int = 0
        valid_and_better: int = 0

        if debug:
            d1, d2 = seg_key
            d1_id: DistrictID = plan.district_ids[d1]
            d2_id: DistrictID = plan.district_ids[d2]

            print()
            print(f"{len(mutations)} mutations {d1}/{d1_id} <-> {d2}/{d2_id}:")

        for m in mutations:
            tried += 1
            plan.mutate(m)

            valid: bool = plan.is_valid_plan(seg_key)
            if valid:
                next_measures = scorer.measure_dimensions(
                    plan.to_assignments(), dimensions
                )
                better: bool = is_better(prev_measures, next_measures)

                if better:
                    prev_measures = next_measures
                    valid_and_better += 1
                    stable = False

                    if debug:
                        print("... Valid mutation the plan better!")

                    if verbose:
                        print(f"Nudged #'s:   {dimensions} = {prev_measures}", end="\r")

            if not valid or not better:
                plan.undo()

            if debug:
                print()
                print(f"... # remaining mutations: {len(mutations) - tried}")

        if debug:
            print(
                f"... Summary: {valid_and_better} of {tried} mutations tried were valid."
            )
            print()

    plan.generation += 1

    if verbose:
        print()
        print(plan)
        print()

    return stable


def is_better(one: Tuple[float, float], two: Tuple[float, float]) -> bool:
    """Is the 2nd pair of measures better than the 1st?

    Two must be better than one on one or the other or both dimensions.
    """

    return (one[0] < two[0] and one[1] <= two[1]) or (
        one[0] <= two[0] and one[1] < two[1]
    )


### END ###
