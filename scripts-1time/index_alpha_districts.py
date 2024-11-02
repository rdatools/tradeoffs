#!/usr/bin/env python3

"""
REPLACE STR DISTRICT IDS WITH INT DISTRICT IDS

$ ./index_alpha_districts.py

"""

from typing import List, Dict, Set
import csv

plan_dir: str = "official_maps"
plan_name: str = "MA_2022_Lower_Official_Proxy"
# plan_name: str = "MA_2022_Upper_Official_Proxy"
# plan_name: str = "MN_2022_Lower_Official_Proxy"

in_plan_path: str = f"{plan_dir}/{plan_name}_alpha.csv"

alpha_plan: List[Dict[str, str]] = list()
districts: Set[str] = set()
with open(in_plan_path, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        alpha_plan.append(row)
        districts.add(row["District"])

district_to_int: Dict[str, int] = {
    district: i + 1 for i, district in enumerate(districts)
}

int_plan: List[Dict[str, str | int]] = list()
for row in alpha_plan:
    int_plan.append(
        {"GEOID20": row["GEOID20"], "District": district_to_int[row["District"]]}
    )

out_plan_path: str = f"{plan_dir}/{plan_name}.csv"

with open(out_plan_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["GEOID20", "District"])
    writer.writeheader()
    writer.writerows(int_plan)

pass

### END ###
