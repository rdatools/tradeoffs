#!/usr/bin/env python3

"""
Create a shell script to duplicate Official maps in DRA.

For example:

$ scripts-1time/make_dup_officials_script.py

Remember to start a server. Open a new Terminal and type:

$ cd dra
$ npm run test

Then open a browser and go to http://localhost:3000/.

For documentation, type:

$ scripts-1time/make_dup_officials_script.py -h

"""

from rdabase import yyyy
from constants import SAMPLE_STATES, OFFICIAL_MAPS

dim: str = "Official"
label: str = "PG-" + dim.upper()


def make_command(xx: str, plan_type: str, dim: str, label: str, id: str) -> str:
    # scripts-1time/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
    return f"scripts-1time/duplicate_map.sh {xx} {plan_type} {yyyy} {dim} {label} {id}"


print("#!/bin/bash")
print("# Duplicate Official maps in DRA.")
print("# Remember to start the DRA server before running these commands!")
for xx, plan_type_ids in OFFICIAL_MAPS.items():
    for plan_type, guid in plan_type_ids.items():
        if plan_type == "congress":
            continue  # already duplicated
        if xx in SAMPLE_STATES:
            continue  # already duplicated

        log_file: str = (
            f"intermediate/{xx}_{yyyy}_{plan_type.capitalize()}_duplicate.log"
        )
        command: str = (
            make_command(xx, plan_type.capitalize(), dim, label, guid)
            + f" > {log_file}"
        )
        print(command)

pass

#
