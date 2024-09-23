#!/usr/bin/env python3

"""
Create a shell script to uplicate Official maps in DRA.

For example:

$ scripts-1time/duplicate_official_maps.py

For documentation, type:

$ scripts-1time/duplicate_official_maps.py -h

"""

from rdabase import plan_type, yyyy
from constants import SAMPLE_STATES, OFFICIAL_MAPS

group: str = "Official"
label: str = "PG-" + group.upper()


def make_command(group: str, label: str, xx: str, id: str) -> str:
    # scripts-1time/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
    return (
        f"scripts-1time/duplicate_map.sh {xx} {plan_type} {yyyy} {group} {label} {id}"
    )


print("#!/bin/bash")
print("# Duplicate Official maps in DRA.")
for xx, guids in OFFICIAL_MAPS.items():
    for plan_type, guid in guids.items():
        if plan_type == "congress":
            continue  # already duplicated
        if xx in SAMPLE_STATES:
            continue  # already duplicated
        print(make_command(group, label, xx, guid))
        # os.system(make_command(group, label, xx, id))

pass

#
