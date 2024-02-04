"""
PUSH A FRONTIER POINT
"""

from typing import Any, List, Dict, Tuple, Callable

from rdabase import Assignment, time_function
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
from .score import Scorer, is_realistic


# TODO - Move this
def echo(message: str = "", *, console: bool = False, log: Any = None) -> None:
    """Echo a message to the console and/or a logfile."""

    if console:
        print(message)
    if log:
        print(message, file=log)


# @time_function
def push_plan(
    assignments: List[Assignment],
    dimensions: Tuple[str, str],
    seed: int,
    multiplier: int,
    prefix: str,
    #
    data: Dict[str, Dict[GeoID, DistrictID]],
    shapes: Dict[str, Any],
    graph: Dict[GeoID, List[GeoID]],
    metadata: Dict[str, Any],
    *,
    logfile: Any = None,
    verbose: bool = False,
    debug: bool = False,
) -> List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]]:
    """Push a plan on a pair of given dimensions."""

    district_by_geoid: Dict[GeoID, DistrictID] = {
        a.geoid: a.district for a in assignments
    }
    pop_by_geoid: Dict[GeoID, int] = {k: int(v["TOTAL_POP"]) for k, v in data.items()}

    scorer: Scorer = Scorer(
        data,
        shapes,
        graph,
        metadata,
        verbose=verbose,
    )  # Initialize a reusable scorer.

    pushed_plans: List[Dict[str, Name | Weight | Dict[GeoID, DistrictID]]] = []

    for i in range(1, multiplier + 1):
        echo(console=verbose, log=logfile)
        echo(f"Search {i} of {multiplier}", console=verbose, log=logfile)

        try:
            plan: Plan = Plan(
                district_by_geoid,
                pop_by_geoid,
                graph,
                seed,
                verbose=verbose,
                # debug=debug,
            )  # Re-initialize the plan for each iteration.

            plan_name: str = f"{prefix}_{i:03d}"
            assignments: Dict[GeoID, DistrictID] = push_point(
                plan,
                scorer,
                dimensions,
                logfile=logfile,
                verbose=verbose,
                # debug=debug,
            )

            pushed_plans.append({"name": plan_name, "plan": assignments})  # No weights.

        except:
            pass  # Push unsuccessful
        finally:
            seed += 1

    return pushed_plans


# @time_function
def push_point(
    plan: Plan,
    scorer: Scorer,
    dimensions: Tuple[str, str],
    *,
    generator: Callable[
        [BorderKey, Plan], Tuple[List[Move], List[Move]]
    ] = size_1_moves,
    logfile: Any = None,
    verbose: bool = False,
    debug: bool = False,
) -> Dict[GeoID, DistrictID]:
    """Push a frontier point on two ratings dimensions."""

    n_pass: int = 1
    limit: int = 1000

    beg_measures = scorer.measure_dimensions(plan.to_assignments(), dimensions)

    while True:
        if n_pass > limit:
            raise RuntimeError(f"Iteration threshold ({limit}) exceeded.")
        echo(console=verbose, log=logfile)
        echo(f"Pass {n_pass} of up to {limit}", console=verbose, log=logfile)

        stable: bool = sweep_once(
            plan,
            scorer,
            dimensions,
            generator=generator,
            logfile=logfile,
            verbose=verbose,
            debug=debug,
        )

        if stable:
            break

        n_pass += 1

    end_measures = scorer.measure_dimensions(plan.to_assignments(), dimensions)

    echo(log=logfile)
    echo(f"Improved #'s: {dimensions} = {beg_measures}", log=logfile)
    echo(f"          to: {dimensions} = {end_measures}", log=logfile)
    echo(log=logfile)

    assignments: Dict[GeoID, DistrictID] = plan.to_dict()

    return assignments


# @time_function
def sweep_once(
    plan: Plan,
    scorer: Scorer,
    dimensions: Tuple[str, str],
    generator: Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]],
    *,
    logfile: Any = None,
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

    echo(f"Starting #'s: {dimensions} = {prev_measures}", log=logfile)

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

            measurements: List[float] = [0.0, 0.0, 0.0, 0.0, 0.0]
            for i, d in enumerate(dimensions):
                measurements[ratings_dimensions.index(d)] = next_measures[i]
            other_dimensions: List[str] = [
                d for d in ratings_dimensions if d not in dimensions
            ]
            for d in other_dimensions:
                measure: float = scorer.measure_dimension(d) if d != "minority" else 0.0
                measurements[ratings_dimensions.index(d)] = measure

            if not is_realistic(measurements):
                plan.undo()
                continue

            # The mutated plan is valid, better, and realistic!

            prev_measures = next_measures

            applied += 1
            stable = False

            echo(f"Nudged #'s:   {dimensions} = {prev_measures}", log=logfile)

    plan.inc_generation()

    return stable


def is_better(one: Tuple[float, float], two: Tuple[float, float]) -> bool:
    """Is the 2nd pair of measures better than the 1st?

    Two must be better than one on one or the other or both dimensions.
    """

    return (one[0] < two[0] and one[1] <= two[1]) or (
        one[0] <= two[0] and one[1] < two[1]
    )


def make_better_fn(
    *, constrain: int = None, anchor: float = None, threshold: float = 0.01
) -> Callable[[Tuple[float, float], Tuple[float, float]], bool]:
    """
    An initial value on the dimension to constrain
    """

    assert constrain in (None, 0, 1)

    def is_better(one: Tuple[float, float], two: Tuple[float, float]) -> bool:
        if constrain is None:
            return (one[0] < two[0] and one[1] <= two[1]) or (
                one[0] <= two[0] and one[1] < two[1]
            )
        else:
            return (
                one[1 - constrain] < two[1 - constrain]
                and abs(anchor - two[constrain]) < threshold
            )

    return is_better


### END ###
