"""
PUSH A FRONTIER POINT
"""

from typing import Callable, Dict, List, Tuple

from rdaensemble.general import ratings_dimensions, ratings_indexes

from .datatypes import GeoID, DistrictID, DistrictOffset, BorderKey, Move, Mutation
from .plan import Plan, size_1_moves
from .score import Scorer, is_better


def push_point(
    plan: Plan,
    scorer: Scorer,
    dimensions: Tuple[str, str],
    seed: int,
    *,
    limit: int = 1000,
    verbose: bool = False,
    debug: bool = False,
) -> Dict[GeoID, DistrictID]:
    """Push a frontier point on two ratings dimensions."""

    prev_measures: Tuple[float, float] = scorer.measure_dimensions(
        plan.to_assignments(), dimensions, "\n"
    )
    next_measures: Tuple[float, float]

    generators: Callable[[BorderKey, Plan], Tuple[List[Move], List[Move]]] = [
        size_1_moves
    ]  # Swap/mutation generators

    for generator in generators:
        if debug:
            print()
            print(f"Generator: {generator.__name__}")

        iteration: int = 1
        while True:
            if iteration > limit:
                raise RuntimeError(f"Iteration threshold {limit} exceeded.")
            if debug:
                print(f"Iteration: {iteration}")

            done: bool = True

            random_adjacent_districts: List[
                BorderKey
            ] = plan.random_adjacent_districts()

            if debug:
                print()
                print(
                    f"# pairs of adjacent districts: {len(random_adjacent_districts)}"
                )

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
                            plan.to_assignments(), dimensions, "\r"
                        )
                        better: bool = is_better(prev_measures, next_measures)

                        if better:
                            prev_measures = next_measures
                            valid_and_better += 1
                            done = False

                            if debug:
                                print("... Success!")

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

            if verbose:
                print()
                print(f"Pushed plan {iteration} of {limit}:")
                print(plan)
                print()

            iteration += 1

            plan.generation += 1

        if verbose:
            print(plan)
            print()

    assignments: Dict[GeoID, DistrictID] = plan.to_dict()

    return assignments


### END ###
