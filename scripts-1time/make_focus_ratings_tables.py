#!/usr/bin/env python3
#

"""
Generate a shell script to make focus ratings tables for the copies of official maps in DRA,
for the upper & lower state houses. Do the congressional, non-sample states manually from
the previously-generate ratings tables that include the official maps.

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
for xx, plan_type_ids in OFFICIAL_MAPS_COPY.items():
    if xx in SAMPLE_STATES:
        continue  # Already done

    for plan_type, _ in plan_type_ids.items():
        if plan_type == "congress":
            continue  # do these manually
        command: str = (
            f"scripts-1time/make_focus_ratings_table.py --state {xx} --plantype {plan_type.capitalize()} --no-debug -v"
        )
        print(command)
        # os.system(command)

pass


### END ###
