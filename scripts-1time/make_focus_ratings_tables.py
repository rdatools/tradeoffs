#!/usr/bin/env python3
#

"""
Generate a shell script to make focus ratings tables for the copies of official maps in DRA.

For example:

$ scripts-1time/make_focus_ratings_tables.py

For documentation, type:

$ scripts-1time/make_focus_ratings_tables.py -h

"""

from rdabase import plan_type, yyyy
from constants import SAMPLE_STATES, OFFICIAL_MAPS_COPY

output_dir: str = "intermediate"

print("#!/bin/bash")
print("# Make focus ratings tables for the copies of official maps in DRA.")
for xx, guids in OFFICIAL_MAPS_COPY.items():
    if xx in SAMPLE_STATES:
        continue  # Already done

    for plan_type, _ in guids.items():
        command: str = (
            f"scripts-1time/make_focus_ratings_table.py --state {xx} --plantype {plan_type.capitalize()} --no-debug -v"
        )
        print(command)
        # os.system(command)

pass


### END ###
