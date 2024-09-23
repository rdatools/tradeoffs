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
from constants import NOTABLE_MAPS  # TODO - NOTABLE_MAPS_COPY

label: str = "PG-NOTABLE"
output_dir: str = "intermediate"

print("#!/bin/bash")
print("# Pull ratings for copies of notable maps in DRA.")
for xx, guids in NOTABLE_MAPS.items():
    for plan_type, notable_maps in guids.items():
        if plan_type == "congress":
            continue  # already duplicated

        for dim, guid in notable_maps.items():
            command: str = (
                f"scripts/pull_map_ratings.sh {xx} {yyyy} {dim.capitalize()} {label} {guid} {output_dir}"
            )
            print(command)
            # os.system(command)

pass


### END ###
