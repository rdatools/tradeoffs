"""
PUSH A FRONTIER POINT
"""

from typing import Any, List, Dict, Tuple, Callable

from rdabase import time_function
from rdaensemble.general import ratings_dimensions, ratings_indexes

from .datatypes import (
    GeoID,
    DistrictID,
    DistrictOffset,
    BorderKey,
    Move,
    Mutation,
    Name,
    Weight,
)
from .plan import Plan, size_1_moves
from .score import Scorer


@time_function
def push_frontiers(
    ensemble: Dict[str, Any],
    frontiers: Dict[str, Any],
    pop_by_geoid: Dict[GeoID, int],
    graph: Dict[GeoID, List[GeoID]],
    scorer: Scorer,
    multiplier: int,
    seed: int,
    *,
    verbose: bool = False,
    debug: bool = False,
) -> List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]]:
    """Push the frontiers for an ensemble of plans."""

    plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = ensemble["plans"]
    pushed_plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = []

    # For each pair of ratings dimensions frontier

    for i, frontier_key in enumerate(frontiers["frontiers"].keys()):
        if verbose:
            print()
            print(
                f">>> Pushing the {frontier_key} frontier point ({i+1} of {len(frontiers['frontiers'].keys())}) <<<"
            )

        plan_names: List[Dict[str, Any]] = frontiers["frontiers"][frontier_key]
        plan_names = ["test"]  # DEBUG

        for j, plan_name in enumerate(plan_names):
            # TODO - Use the plan_name to get the plan from the ensemble
            # DEBUG
            p: Dict[str, Name | Weight | Dict[GeoID, DistrictID]] = plans[0]
            name: Name = str(p["name"])
            district_by_geoid: Dict[GeoID, DistrictID] = p["plan"]  # type: ignore

            # Push each frontier point one or more times

            frontier_pair: List[str] = list(frontier_key.split("_"))
            dimensions: Tuple[str, str] = (frontier_pair[0], frontier_pair[1])

            for j in range(1, multiplier + 1):
                if verbose:
                    print()
                    print(f"Search {j} of {multiplier}")

                try:
                    plan: Plan = Plan(
                        district_by_geoid,
                        pop_by_geoid,
                        graph,
                        seed,
                        verbose=verbose,
                        # debug=debug,
                    )
                    beg_measures = scorer.measure_dimensions(
                        plan.to_assignments(), dimensions
                    )

                    # plan.to_csv("output/test_starting_plan.csv") # DEBUG

                    plan_name: str = f"{frontier_key}_{i:03d}"
                    assignments: Dict[GeoID, DistrictID] = push_point(
                        plan,
                        scorer,
                        dimensions,
                        verbose=verbose,
                        # debug=debug,
                    )
                    end_measures = scorer.measure_dimensions(
                        plan.to_assignments(), dimensions
                    )

                    # plan.to_csv(f"output/test_pushed_{frontier_key}_plan.csv") # DEBUG

                    if verbose:
                        print()
                        print(f"Improved #'s: {dimensions} = {beg_measures}")
                        print(f"          to: {dimensions} = {end_measures}")
                        print()

                    pushed_plans.append(
                        {"name": plan_name, "plan": assignments}
                    )  # No weights.

                except:
                    pass
                finally:
                    seed += 1

        break  # DEBUG

    return pushed_plans


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

    generators: List[Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]]] = [
        size_1_moves
    ]  # Swap/mutation generators

    for generator in generators:
        n_pass: int = 1
        while True:
            if n_pass > limit:
                raise RuntimeError(f"Iteration threshold ({limit}) exceeded.")
            if verbose:
                print()
                print(f"Pass {n_pass} of up to {limit}")

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

            n_pass += 1

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

    stable: bool = True
    for seg_key in random_adjacent_districts:
        mutations: List[Mutation] = plan.random_mutations(seg_key, generator)
        tried: int = 0
        applied: int = 0

        for m in mutations:
            tried += 1
            plan.mutate(m)

            if not plan.is_valid_plan(seg_key):
                plan.undo()
                continue

            next_measures = scorer.measure_dimensions(plan.to_assignments(), dimensions)
            if not is_better(prev_measures, next_measures):
                plan.undo()
                continue

            measurements: Dict[str, float] = dict(zip(dimensions, next_measures))
            # TODO - Score the "other" dimensions
            # TODO - If not is_realistic(),
            # TODO - then undo() and continue

            # The mutated plan is valid, better, and realistic!

            prev_measures = next_measures

            applied += 1
            stable = False

            if verbose:
                print(f"Nudged #'s:   {dimensions} = {prev_measures}", end="\r")

    plan.inc_generation()

    return stable


def is_better(one: Tuple[float, float], two: Tuple[float, float]) -> bool:
    """Is the 2nd pair of measures better than the 1st?

    Two must be better than one on one or the other or both dimensions.
    """

    return (one[0] < two[0] and one[1] <= two[1]) or (
        one[0] <= two[0] and one[1] < two[1]
    )


### END ###
