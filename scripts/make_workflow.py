#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py \
--state NC \
--no-debug \
> workflows/NC.sh

For documentation, type:

$ scripts/make_workflow.py

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Dict, Any

from rdabase import require_args


def main() -> None:
    """Generate the workflow for a state.

    Note, I copied some V1 artifacts from the 'pg' repo en masse on 02/20/24:
    - DRA notable map BAF's from pg/data, and
    - DRA notable maps ratings tables from pg/docs/_data

    """

    """
    STEP 1

    Generate an ensemble of 100 random plans:

    scripts/rmfrsp_ensemble.py \
    --state NC \
    --size 100 \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/ensembles/NC20C_RMfRSP_100_plans.json \
    --log ../../iCloud/fileout/ensembles/NC20C_RMfRSP_100_log.txt \
    --no-debug
    
    Approximate a root map with them:

    scripts/approx_root_map.py \
    --state NC \
    --plans ../../iCloud/fileout/ensembles/NC20C_RMfRST_100_plans.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --map ../../iCloud/fileout/rootmaps/NC20C_rootmap.csv \
    --candidates ../../iCloud/fileout/rootmaps/NC20C_rootcandidates.json \
    --log ../../iCloud/fileout/rootmaps/NC20C_rootlog.txt \
    --no-debug

    """

    """
    STEP 2

    Generate 10K random plans, using ReCom and the root map as the starting plan:

    scripts/recom_ensemble.py \
    --state NC \
    --size 1000 \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --root ../../iCloud/fileout/rootmaps/NC20C_root_map.csv \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
    --log ../../iCloud/fileout/ensembles/NC20C_log.txt \
    --no-debug

    """

    """
    STEP 3

    Score the plans in the ensemble:

    $ scripts/score_ensemble.py \
    --state NC \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --no-debug

    """

    """
    STEP 4

    Find the frontiers:

    scripts/find_frontiers.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
    --frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
    --verbose \
    --no-debug

    """

    """
    TODO - STEP 5 
    
    Generate push_plan jobs:

    and run them to push the frontiers. 
    
    Collect the results:

    """

    """
    TODO - STEP 6

    Append the pushed plans to a copy of the original ensemble:

    """

    """
    TODO - STEP 7

    Find the new frontiers:

    """

    """
    TODO - STEP 8 <<< Todd?

    Add the plans for any new frontier points to the original ensemble:

    """

    """
    TODO - STEP 9

    ID the notable maps in the augmented ensemble:

    scripts/id_notable_maps.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
    --notables ../../iCloud/fileout/ensembles/NC20C_notable_maps.json \
    --no-debug

    """

    """
    STEP 10

    Make a box plot:

    scripts/make_box_plot.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --focus ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
    --image ../../iCloud/fileout/images/NC20C_10K_boxplot.svg \
    --no-debug

    """

    """
    TODO - STEP 11 <<< Todd: Including pushed points?

    Make a statistics table:

    scripts/make_stats_table.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --output ../../iCloud/fileout/images/NC20C_statistics.csv \
    --no-debug

    """

    """
    STEP 12

    Make a notable maps ratings table:

    scripts/make_ratings_table.py \
    --notables ../../iCloud/fileout/ensembles/NC20C_notable_maps.json \
    --output ../../iCloud/fileout/images/NC20C_notable_maps_ratings.csv \
    --no-debug

    """

    """
    STEP 13

    Make scatter plots w/ pre- & post-push frontiers:

    scripts/make_scatter_plots.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
    --focus ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
    --prefix NC20C \
    --suffix 10K \
    --output ../../iCloud/fileout/images/ \
    --no-debug

    """

    """
    TODO - STEP 14 

    Copy the artifacts to 'docs' subdirectories:

    """

    args: argparse.Namespace = parse_args()

    xx: str = args.state

    pass  # TODO


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate the workflow for a state."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
    )

    # Enable debug/explicit mode
    parser.add_argument("--debug", default=True, action="store_true", help="Debug mode")
    parser.add_argument(
        "--no-debug", dest="debug", action="store_false", help="Explicit mode"
    )

    args: Namespace = parser.parse_args()

    # Default values for args in debug mode
    debug_defaults: Dict[str, Any] = {
        "state": "NC",
        "verbose": True,
    }
    args = require_args(args, args.debug, debug_defaults)

    return args


if __name__ == "__main__":
    main()

### END ###
