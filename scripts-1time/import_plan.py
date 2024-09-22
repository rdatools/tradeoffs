#!/usr/bin/env python3
#

"""
Import a BAF into a DRA map.

For example:

$ scripts/import_plan.py -s NC -o ~/Downloads/NC/ -f NC_2022_Congress_Official.csv -l Official -g NC_2022_Congress_Official_guids.txt
$ scripts/import_plan.py -s NC -o ~/Downloads/NC/ -f NC_2022_Congress_Official_intersections.csv -l Official -g NC_2022_Congress_Official_intersections_guids.txt -i

For documentation, type:

$ scripts/import_plan.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

import os

from pg import *


def parse_args() -> Namespace:
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Import a BAF into a DRA map."
    )

    parser.add_argument(
        "-s",
        "--state",
        default="NC",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/Downloads/NC/",
        help="Path to the output root",
        type=str,
    )
    parser.add_argument(
        "-f",
        "--file",
        default="NC_2022_Congress_Official.csv",
        help="Path to the plan CSV",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--label",
        default="Official",
        help="The type of map (e.g., Official)",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--intersections",
        dest="intersections",
        action="store_true",
        help="Intersections map",
    )
    parser.add_argument(
        "-g",
        "--guids",
        default="NC_2022_Congress_Official_guids.txt",
        help="Path to the resulting DRA map GUIDs",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--prefix",
        default="081623",
        help="xid prefix (e.g., 081623)",
        type=str,
    )

    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    args: Namespace = parser.parse_args()
    return args


def main() -> None:
    """Expand a precinct-assignment file into a block-assignment file."""

    args: Namespace = parse_args()

    xx: str = args.state
    output_dir: str = os.path.expanduser(args.output)
    plan: str = os.path.join(output_dir, args.file)
    label: str = args.label
    intersections: bool = args.intersections
    guids: str = os.path.join(output_dir, args.guids)
    prefix: str = args.prefix

    verbose: bool = args.verbose

    #

    year: str = cycle if label == "Baseline" else yyyy

    user: str = "alec@davesredistricting.org"

    name: str = f"{xx} {year} {plan_type.title()} - {label}"
    if intersections:
        name += " (intersections)"

    qualified_label: str = (
        f"Notable {label.lower()}" if label not in ["Baseline", "Official"] else label
    )
    description: str = (
        f"{label}-baseline district intersections"
        if intersections
        else f"{qualified_label} map"
    )

    tag: str = f"PG-{label.upper()}"
    if intersections:
        tag = "PG-CORES"
    elif label not in ["Baseline", "Official"]:
        tag = "PG-NOTABLE"

    #

    xid: str = (
        f"{prefix}_{xx}_{year}_Congress_{label}"
        if not intersections
        else f"{prefix}_{xx}_{year}_Congress_{label}_intersections"
    )

    """
    On success, the importmap.js script echoes something like this:
    
    importmap: import succeeded: /Users/alecramsay/Downloads/NC/NC_2020_Congress_Baseline_canonical.csv (elapsed: 0:16)
    importmap: guid: e9fb3d3e-9e11-4e73-ad21-680b2feac04a
    importmap: shareguid: ff009f31-8017-4ae2-bc71-07a8f085f09e

    Capture these for downstream processing.
    """

    command: str = f"../dra-cli/importmap.js -u {user} -f {plan} -x {xid} -T {plan_type.lower()} -N '{name}' -D '{description}' -L {tag} &> {guids}"
    if verbose:
        print(command)
    os.system(command)

    pass


if __name__ == "__main__":
    main()

### END ###
