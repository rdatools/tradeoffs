#!/usr/bin/env python3

"""
MAKE SAMPLE "PUSH" JOBS

For documentation, type:

$ scripts/make_sample_jobs.py

"""

import itertools

from rdaensemble.general import ratings_dimensions


def main() -> None:
    """Make sample 'push_plan.py' jobs."""

    xx: str = "NC"
    plan: str = "sample/sample_plan.csv"
    seed: int = 518
    multiplier: int = 1
    data: str = "../rdabase/data/NC/NC_2020_data.csv"
    shapes: str = "../rdabase/data/NC/NC_2020_shapes_simplified.json"
    graph: str = "../rdabase/data/NC/NC_2020_graph.json"
    output: str = "sample/"

    ratings_pairs: List = list(itertools.combinations(ratings_dimensions, 2))
    for pair in ratings_pairs:
        dimensions: str = " ".join(pair)
        prefix: str = f"sample_{'_'.join(pair)}_plan"
        logfile: str = f"{output[:-1]}/sample_{'_'.join(pair)}_log.txt"

        print(f"scripts/push_plan.py \\")
        print(f"--state {xx} \\")
        print(f"--plan {plan} \\")
        print(f"--dimensions {dimensions} \\")
        print(f"--seed {seed} \\")
        print(f"--multiplier {multiplier} \\")
        print(f"--prefix {prefix} \\")
        print(f"--data ../rdabase/data/{xx}/{xx}_2020_data.csv \\")
        print(f"--shapes ../rdabase/data/{xx}/{xx}_2020_shapes_simplified.json \\")
        print(f"--graph ../rdabase/data/{xx}/{xx}_2020_graph.json \\")
        print(f"--output {output} \\")
        print(f"--log {logfile} \\")
        print(f"--verbose \\")
        print(f"--no-debug")
        print()

        seed += 1


if __name__ == "__main__":
    main()

### END ###
