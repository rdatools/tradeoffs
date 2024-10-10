#!/usr/bin/env python3

"""
Create a shell script to export no-split proxies of official maps in DRA.

For example:

$ scripts-1time/make_export_official_proxies_script.py

For documentation, type:

$ scripts-1time/make_export_official_proxies_script.py -h

"""

from constants import OFFICIAL_MAPS

print("#!/bin/bash")
print("# Export no-split proxies of official maps from DRA.")
for xx, plan_type_ids in OFFICIAL_MAPS.items():
    for plan_type, guid in plan_type_ids.items():
        command: str = (
            f"scripts-1time/export_official_proxy.sh --state {xx} --plantype {plan_type} --name {xx}_2022_{plan_type.capitalize()}_Official_Proxy.csv"
        )
        print(command)

pass

#
