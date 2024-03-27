#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py \
--state NC \
--zone \
--pin \
--save-at-limit \
--points 100 \
--pushes 3 \
--delta 5 \
--cores 28 \
--batch-size 50 \
> workflows/NC.sh

For documentation, type:

$ scripts/make_workflow.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace

from typing import Dict, Any

from rdabase import require_args


def main() -> None:
    """Generate the workflow for a state.

    Note, I copied some V1 artifacts from the 'pg' repo en masse on 02/20/24:
    - DRA notable map BAF's from pg/data to notable_maps/xx, and
    - DRA notable maps ratings tables from pg/docs/_data to docs/_data/notable_ratings

    Also the root maps from the 'baseline' repo en masse on 03/11/24.
    """

    args: argparse.Namespace = parse_args()

    xx: str = args.state
    input_dir: str = "../rdabase/data"
    output_dir: str = f"../../iCloud/fileout/tradeoffs/{xx}/ensembles"
    pushed_dir: str = f"../../iCloud/fileout/tradeoffs/{xx}/pushed"
    image_dir: str = f"../../iCloud/fileout/tradeoffs/{xx}/docs/assets/images"
    data_dir: str = f"../../iCloud/fileout/tradeoffs/{xx}/docs/_data"

    # Push mode -- frontiers only, zone, or random

    assert not (args.zone and args.random), "Cannot use both --zone and --random"

    """
    # NC workflow

    """

    print(f"# {xx} workflow:")
    print(f"# --zone: {args.zone}")
    print(f"# --random: {args.random}")
    print(f"# --points: {args.points}")
    print(f"# --pushes: {args.pushes}")
    print(f"# --delta: {args.delta}")
    print(f"# --cores: {args.cores}")
    print(f"# --windfall: {args.windfall}")
    print()

    """
    # Generate the data (from 'rdabase')

    scripts/preprocess_state.py -s NC
    
    """

    print(f"# Generate the data (from 'rdabase')")
    print()
    print(f"scripts/preprocess_state.py -s {xx}")
    print()

    """
    # Set up the state (from 'tradeoffs')

    scripts/SETUP.sh NC

    """

    print(f"# Set up the state (from 'tradeoffs')")
    print()
    print(f"scripts/SETUP.sh {xx}")
    print()

    """
    # Use the root map in root_maps or
    # Approximate a new root map:
    # Generate an ensemble of 100 random plans (from 'rdaensemble')

    scripts/rmfrsp_ensemble.py \
    --state NC \
    --size 100 \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_RMfRSP_100_plans.json \
    --log ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_RMfRSP_100_log.txt \
    --no-debug

    # Approximate a root map with them (from 'rdaroot')

    scripts/approx_root_map.py \
    --state NC \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_RMfRST_100_plans.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --map ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_rootmap.csv \
    --candidates ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_rootcandidates.json \
    --log ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_rootlog.txt \
    --no-debug

    # NOTE - Copy the result to the tradeoffs/root_maps directory as NC20C_root_map.csv

    """

    print(f"# Use the root map in root_maps or")
    print(f"# Approximate a new root map:")
    print(f"# Generate an ensemble of 100 random plans (from 'rdaensemble')")
    print()
    print(f"scripts/rmfrsp_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--size 100 \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--plans {output_dir}/{xx}20C_RMfRSP_100_plans.json \\")
    print(f"--log {output_dir}/{xx}20C_RMfRSP_100_log.txt \\")
    print(f"--no-debug")
    print()
    print(f"# Approximate a root map with them (from 'rdaroot')")
    print()
    print(f"scripts/approx_root_map.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_RMfRST_100_plans.json \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--map {output_dir}/{xx}20C_rootmap.csv \\")
    print(f"--candidates {output_dir}/{xx}20C_rootcandidates.json \\")
    print(f"--log {output_dir}/{xx}20C_rootlog.txt \\")
    print(f"--no-debug")
    print()
    print(f"# Copy the result to the root_maps directory as {xx}20C_root_map.csv")
    print()

    """
    # Generate an ensemble (from 'rdaensemble')

    scripts/recom_ensemble.py \
    --state NC \
    --size 10000 \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --root ../tradeoffs/root_maps/NC20C_root_map.csv \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
    --log ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_log.txt \
    --no-debug

    """

    print(f"# Generate an ensemble (from 'rdaensemble')")
    print()
    print(f"scripts/recom_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--root ../tradeoffs/root_maps/{xx}20C_root_map.csv \\")
    print(f"--plans {output_dir}/{xx}20C_plans.json \\")
    print(f"--log {output_dir}/{xx}20C_log.txt \\")
    print(f"--no-debug")
    print()

    """
    # Score the ensemble (from 'rdaensemble')

    scripts/score_ensemble.py \
    --state NC \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
    --no-debug

    """

    print(f"# Score the ensemble (from 'rdaensemble')")
    print()
    print(f"scripts/score_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans.json \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--no-debug")
    print()

    """
    # Find the ratings frontiers in the ensemble (from 'tradeoffs')

    scripts/find_frontiers.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
    --metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_metadata.json \
    --frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers.json \
    --verbose \
    --no-debug

    """

    print(f"# Find the ratings frontiers in the ensemble (from 'tradeoffs')")
    print()
    print(f"scripts/find_frontiers.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--metadata {output_dir}/{xx}20C_scores_metadata.json \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers.json \\")
    print(f"--verbose \\")
    print(f"--no-debug")
    print()

    """
    # Generate 'push' jobs (from 'tradeoffs')

    scripts/make_push_jobs.py \
    --state NC \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
    --frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers.json \
    --zone \
    --pin \
    --save-at-limit \
    --points 100 \
    --pushes 3 \
    --delta 5 \
    --cores 28 \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --output ../../iCloud/fileout/tradeoffs \
    --verbose \
    --no-debug

    """

    print(f"# Generate 'push' jobs (from 'tradeoffs')")
    print()
    print(f"scripts/make_push_jobs.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans.json \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers.json \\")
    if args.zone:
        print(f"--zone \\")
        print(f"--delta 5 \\")
    if args.random:
        print(f"--random \\")
    if args.pin:
        print(f"--pin \\")
    if args.save_at_limit:
        print(f"--save-at-limit \\")
    print(f"--points {args.points} \\")
    print(f"--pushes {args.pushes} \\")
    print(f"--cores {args.cores} \\")
    print(f"--batch-size {args.batch_size} \\")
    if args.windfall:
        print(f"--windfall \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--output ../../iCloud/fileout/tradeoffs \\")
    print(f"--verbose \\")
    print(f"--no-debug")
    print()

    """
    # Push the jobs to the cluster (from 'tradeoffs')
    # Submit the jobs (on the UA cluster)
    # Pull the pushed plans from the cluster (from 'tradeoffs')

    scripts/COMBINE_LOGS.sh ../../iCloud/fileout/tradeoffs/NC/pushed/*.log > ../../iCloud/fileout/tradeoffs/NC/jobs_logs.csv

    """

    print(f"# Push the jobs to the cluster (from 'tradeoffs')")
    print(f"# Submit the jobs (on the UA cluster)")
    print(f"# Pull the pushed plans from the cluster (from 'tradeoffs')")
    print()
    print(
        f"scripts/COMBINE_LOGS.sh ../../iCloud/fileout/tradeoffs/{xx}/pushed/*.log > ../../iCloud/fileout/tradeoffs/{xx}/jobs_logs.csv"
    )
    print()

    """
    # Collect the pushed plans into an ensemble (from 'rdaensemble')

    scripts/ensemble_from_plans.py \
    --base ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_pushed.json \
    --dir ../../iCloud/fileout/tradeoffs/NC/pushed \
    --no-debug

    """

    print(f"# Collect the pushed plans into an ensemble (from 'rdaensemble')")
    print()
    print(f"scripts/ensemble_from_plans.py \\")
    print(f"--base {output_dir}/{xx}20C_plans.json \\")
    print(f"--plans {output_dir}/{xx}20C_plans_pushed.json \\")
    print(f"--dir {pushed_dir} \\")
    print(f"--no-debug")
    print()

    """
    # Score the pushed plans (from 'rdaensemble')
    
    scripts/score_ensemble.py \
    --state NC \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_pushed.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_pushed.csv \
    --no-debug

    """

    print(f"# Score the pushed plans (from 'rdaensemble')")
    print()
    print(f"scripts/score_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans_pushed.json \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--scores {output_dir}/{xx}20C_scores_pushed.csv \\")
    print(f"--no-debug")
    print()

    """
    # Combine the original ensemble & pushed plans scores (from 'tradeoffs')

    scripts/COMBINE_SCORES.sh NC

    """

    print(f"# Combine the original ensemble & pushed plans scores (from 'tradeoffs')")
    print()
    print(f"scripts/COMBINE_SCORES.sh {xx}")
    print()

    """
    # Find the pushed frontiers (from 'tradeoffs')

    scripts/find_frontiers.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
    --metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_pushed_metadata.json \
    --frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_pushed.json \
    --no-debug

    """

    print(f"# Find the pushed frontiers (from 'tradeoffs')")
    print()
    print(f"scripts/find_frontiers.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores_augmented.csv \\")
    print(f"--metadata {output_dir}/{xx}20C_scores_pushed_metadata.json \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers_pushed.json \\")
    print(f"--no-debug")
    print()

    """
    # ID the notable maps in the augmented ensemble (from 'rdaensemble')

    scripts/id_notable_maps.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
    --metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_metadata.json \
    --notables ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_notable_maps.json \
    --no-debug

    """

    print(f"# ID the notable maps in the augmented ensemble (from 'rdaensemble')")
    print()
    print(f"scripts/id_notable_maps.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores_augmented.csv \\")
    print(f"--metadata {output_dir}/{xx}20C_scores_metadata.json \\")
    print(f"--notables {output_dir}/{xx}20C_notable_maps.json \\")
    print(f"--no-debug")
    print()

    """
    # Make a box plot (from 'tradeoffs')

    scripts/make_box_plot.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
    --image ../../iCloud/fileout/tradeoffs/NC/docs/assets/images/NC20C_boxplot.svg \
    --no-debug

    """

    print(f"# Make a box plot (from 'tradeoffs')")
    print()
    print(f"scripts/make_box_plot.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores_augmented.csv \\")
    print(f"--image {image_dir}/{xx}20C_boxplot.svg \\")
    print(f"--no-debug")
    print()

    """
    # Make a statistics table (from 'tradeoffs')

    scripts/make_stats_table.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
    --output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20C_statistics.csv \
    --no-debug

    """

    print(f"# Make a statistics table (from 'tradeoffs')")
    print()
    print(f"scripts/make_stats_table.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--output {data_dir}/{xx}20C_statistics.csv \\")
    print(f"--no-debug")
    print()

    """
    # Make a notable maps ratings table (from 'tradeoffs')

    scripts/make_ratings_table.py \
    --notables ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_notable_maps.json \
    --output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20C_notable_maps_ratings.csv \
    --no-debug

    """

    print(f"# Make a notable maps ratings table (from 'tradeoffs')")
    print()
    print(f"scripts/make_ratings_table.py \\")
    print(f"--notables {output_dir}/{xx}20C_notable_maps.json \\")
    print(f"--output {data_dir}/{xx}20C_notable_maps_ratings.csv \\")
    print(f"--no-debug")
    print()

    """
    # If you want to highlight a map or a few on the scatter plots,
    # use this process which lets the maps split precincts.
    
    # For each focus map:
    # - Open the map in DRA
    # - Verify the choices in Data Selector (2020 Census, 2016-2020 Election Composite)
    # - Export the Map Analytics JSON
    # - Rename it, e.g., NC-2022-Congressional-map-analytics.json
    # - Move it to fileout/tradeoffs/NC/ensembles
    # - Use backslashes to escape spaces in the name

    scripts/flatten_scorecard.py \
    --export ../../iCloud/fileout/tradeoffs/NC/ensembles/NC-2022-Congressional-map-analytics.json \
    --name Official \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC-2022-Congressional_scores.csv \
    --no-debug

    # Combine the names & ratings into a CSV that looks like this:

    Map,Proportionality,Competitiveness,Minority,Compactness,Splitting
    2024 Official,0,24,65,43,41
    2020 Official,94,30,60,61,57

    # and save it in ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_focus_scores.csv
    # Use the --focus flag when making the scatter plots.

    """

    print("# If you want to highlight a map or a few on the scatter plots,")
    print("# use this process which lets the maps split precincts.")
    print()

    print(f"# For each focus map:")
    print(f"# - Open the map in DRA")
    print(
        f"# - Verify the choices in Data Selector (2020 Census, 2016-2020 Election Composite)"
    )
    print(f"# - Export the Map Analytics JSON")
    print(f"# - Rename it, e.g., NC-2022-Congressional-map-analytics.json")
    print(f"# - Move it to fileout/tradeoffs/NC/ensembles")
    print(f"# - Use backslashes to escape spaces in the name")
    print()
    print(f"scripts/flatten_scorecard.py \\")
    print(
        f"--export ../../iCloud/fileout/tradeoffs/NC/ensembles/NC-2022-Congressional-map-analytics.json \\"
    )
    print(f"--name Official \\")
    print(
        f"--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC-2022-Congressional_scores.csv \\"
    )
    print(f"--no-debug")
    print()
    print(f"# Combine the names & ratings into a CSV that looks like this:")
    print()
    print(f"Map,Proportionality,Competitiveness,Minority,Compactness,Splitting")
    print(f"2024 Official,0,24,65,43,41")
    print(f"2020 Official,94,30,60,61,57")
    print()
    print(
        f"# and save it in ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_focus_scores.csv"
    )
    print(f"# Use the --focus flag when making the scatter plots.")
    print()

    """
    # Make scatter plots (from 'tradeoffs')

    scripts/make_scatter_plots.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
    --more ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
    --frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers.json \
    --pushed ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_pushed.json \
    --notables docs/_data/notable_ratings/NC_2022_Congress_ratings.csv \
    --focus ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_focus_scores.csv \
    --prefix NC20C \
    --output ../../iCloud/fileout/tradeoffs/NC/docs/assets/images \
    --no-debug

    """

    print(f"# Make scatter plots (from 'tradeoffs')")
    print()
    print(f"scripts/make_scatter_plots.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--more {output_dir}/{xx}20C_scores_augmented.csv \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers.json \\")
    print(f"--pushed {output_dir}/{xx}20C_frontiers_pushed.json \\")
    print(f"--notables docs/_data/notable_ratings/{xx}_2022_Congress_ratings.csv \\")
    print(f"--focus {output_dir}/{xx}20C_focus_scores.csv \\")
    print(f"--prefix {xx}20C \\")
    print(f"--output {image_dir} \\")
    print(f"--no-debug")
    print()

    """
    # Copy the artifacts to the fileout & then 'docs' subdirectories (from 'tradeoffs')

    scripts/DEPLOY.sh NC

    """

    print(
        f"# Copy the artifacts to the fileout & then 'docs' subdirectories (from 'tradeoffs')"
    )
    print()
    print(f"scripts/DEPLOY.sh {xx}")
    print()

    """
    # Finally:
    # - Add a state page in the docs/_pages/pages directory, and
    # - Add a link to the state page in docs/_pages/pages/states.markdown.

    # END
    """

    print(f"# Finally:")
    print(f"# - Add a state page in the docs/_pages/pages directory, and")
    print(f"# - Add a link to the state page in docs/_pages/pages/states.markdown.")
    print()
    print(f"# END")


def parse_args():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate the workflow for a state."
    )

    parser.add_argument(
        "--state",
        help="The two-character state code (e.g., NC)",
        type=str,
    )
    # --zone and --randome are mutually exclusive options, enforced after parse_args
    parser.add_argument(
        "-z",
        "--zone",
        dest="zone",
        action="store_true",
        help="Push a 'zone' of points near the frontier and the frontier",
    )
    parser.add_argument(
        "-r",
        "--random",
        dest="random",
        action="store_true",
        help="Push a selection of random plans and the frontier",
    )
    parser.add_argument("--pin", dest="pin", action="store_true", help="Pin mode")
    parser.add_argument(
        "--save-at-limit",
        dest="save_at_limit",
        action="store_true",
        help="Save the in-progress plan at the limit",
    )
    parser.add_argument(
        "--points",
        type=int,
        default=100,
        help="The *maximum* number of points to push for each frontier.",
    )
    parser.add_argument(
        "--pushes",
        type=int,
        default=3,
        help="How many times to push each point.",
    )
    parser.add_argument("--cores", type=int, help="The number of core per node.")
    parser.add_argument(
        "--batch-size",
        dest="batch_size",
        type=int,
        help="The number of commands per job.",
    )
    parser.add_argument(
        "--delta",
        type=int,
        default=5,
        help="How much ratings can differ for a point to be considered 'near' a frontier point",
    )
    parser.add_argument(
        "-w", "--windfall", dest="windfall", action="store_true", help="Windfall mode"
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
