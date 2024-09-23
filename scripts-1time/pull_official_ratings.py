#!/usr/bin/env python3
#

"""
Generate a shell script to pull the ratings for copies of official DRA maps.

For example:

$ scripts-1time/pull_official_ratings.py

For documentation, type:

$ scripts-1time/pull_official_ratings.py -h

"""

from rdabase import plan_type, yyyy
from constants import OFFICIAL_MAPS  # OFFICIAL_MAPS_COPY

label: str = "Official"
output_dir: str = "intermediate"

print("#!/bin/bash")
print("# Pull ratings for copies of official maps in DRA.")
for xx, guids in OFFICIAL_MAPS.items():
    for plan_type, guid in guids.items():
        if plan_type == "congress":
            continue  # already duplicated

        command: str = (
            f"scripts-1time/pull_map_ratings.sh {xx} {yyyy} {plan_type.capitalize()} {label} {guid} {output_dir}"
        )
        print(command)
        # os.system(command)

pass


### END ###
