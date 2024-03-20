"""
PUSH A FRONTIER POINT
"""

import traceback

from typing import Any, List, Dict, Tuple, Callable, Optional

from rdabase import Assignment, time_function, echo
from rdaensemble.general import ratings_dimensions  # , ratings_indexes

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


# @time_function
def push_plan(
    assignments: List[Assignment],
    dimensions: Tuple[str, str],
    seed: int,
    #
    data: Dict[str, Dict[str, str | int]],
    shapes: Dict[str, Any],
    graph: Dict[GeoID, List[GeoID]],
    metadata: Dict[str, Any],
    *,
    pin: str = "",
    save_at_limit: bool = False,
    logfile: Any = None,
    verbose: bool = False,
    debug: bool = False,
) -> Dict[GeoID, DistrictID]:
    """Push a plan on a pair of given dimensions *once*. Return the pushed assignments.

    NOTE - For multiple push attempts, call this multiple times with different seeds.
    """

    base_district_by_geoid: Dict[GeoID, DistrictID] = {
        a.geoid: a.district for a in assignments
    }
    pop_by_geoid: Dict[GeoID, int] = {k: int(v["TOTAL_POP"]) for k, v in data.items()}

    scorer: Scorer = Scorer(
        data,
        shapes,
        graph,
        metadata,
        verbose=verbose,
    )

    echo(console=verbose, log=logfile)
    echo(f"Pushing plan on {dimensions} dimensions", console=verbose, log=logfile)
    if pin:
        echo(f"Pinned on {pin}", console=verbose, log=logfile)
    echo(console=verbose, log=logfile)

    pushed_district_by_geoid: Dict[GeoID, DistrictID] = {}

    try:
        plan: Plan = Plan(
            base_district_by_geoid,
            pop_by_geoid,
            graph,
            seed,
            verbose=verbose,
            debug=debug,
        )

        pushed_district_by_geoid = push_point(
            plan,
            scorer,
            dimensions,
            pin=pin,
            save_at_limit=save_at_limit,
            logfile=logfile,
            verbose=verbose,
            debug=debug,
        )

    except Exception as err:
        traceback.print_tb(err.__traceback__)
        # traceback.print_stack()
        echo(f"FAIL: Push unsuccessful.", console=verbose, log=logfile)

    return pushed_district_by_geoid


# @time_function
def push_point(
    plan: Plan,
    scorer: Scorer,
    dimensions: Tuple[str, str],
    *,
    generator: Callable[
        [BorderKey, Plan], Tuple[List[Move], List[Move]]
    ] = size_1_moves,
    pin: str = "",
    save_at_limit: bool = False,
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
            if save_at_limit:
                break
            else:
                raise RuntimeError(f"Iteration threshold ({limit}) exceeded.")
        echo(console=verbose, log=logfile)
        echo(f"Pass {n_pass} of up to {limit}", console=verbose, log=logfile)

        stable: bool = sweep_once(
            plan,
            scorer,
            dimensions,
            generator=generator,
            pin=pin,
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
    *,
    pin: str = "",
    generator: Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]],
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

    is_better: Callable[[Tuple[float, float], Tuple[float, float]], bool] = (
        make_better_fn()
    )
    if pin:
        assert pin in dimensions
        pinned: int = dimensions.index(pin)
        value: float = prev_measures[pinned]
        is_better = make_better_fn(constrain=pinned, anchor=value)

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
                measure: float = (
                    scorer.measure_dimension(d) if d != "minority" else 0.0
                )  # NOTE: Don't need to measure minority
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

    echo(f"{plan}", console=verbose, log=logfile)
    plan.reset_counters()

    return stable


def make_better_fn(
    *,
    constrain: Optional[int] = None,
    anchor: Optional[float] = None,
    threshold: float = 0.05,  # 0.01,
) -> Callable[[Tuple[float, float], Tuple[float, float]], bool]:
    """Is a plan better on one or both dimensions? The value of one dimension can be 'pinned'."""

    assert constrain in (None, 0, 1)

    def is_better(one: Tuple[float, float], two: Tuple[float, float]) -> bool:
        if constrain is None:
            return (one[0] < two[0] and one[1] <= two[1]) or (
                one[0] <= two[0] and one[1] < two[1]
            )
        else:
            assert constrain is not None
            assert anchor is not None

            return (
                one[1 - constrain] < two[1 - constrain]
                and abs(anchor - two[constrain]) < threshold
            )

    return is_better


### END ###
