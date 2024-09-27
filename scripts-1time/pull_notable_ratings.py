#!/usr/bin/env python3
#

"""
Generate a shell script to pull the ratings for copies of notable maps in DRA.

For example:

$ scripts-1time/pull_notable_ratings.py

For documentation, type:

$ scripts-1time/pull_notable_ratings.py -h

"""

from rdabase import plan_type, yyyy
from constants import NOTABLE_MAPS_COPY

output_dir: str = "intermediate"

print("#!/bin/bash")
print("# Pull ratings for copies of notable maps in DRA.")
for xx, plan_type_ids in NOTABLE_MAPS.items():
    for plan_type, notable_maps in plan_type_ids.items():
        if plan_type == "congress":
            continue  # already duplicated

        for dim, guid in notable_maps.items():
            command: str = (
                f"scripts-1time/pull_map_ratings.sh {xx} {yyyy} {plan_type.capitalize()} {dim.capitalize()} {guid} {output_dir}"
            )
            print(command)
            # os.system(command)

pass


### END ###
