#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py \
--state NC \
--zone \
--points 100 \
--pushes 3 \
--delta 5 \
--cores 28 \
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
    - DRA notable map BAF's from pg/data to notable_maps/xx, and
    - DRA notable maps ratings tables from pg/docs/_data to docs/_data/notable_ratings

    Also the root maps from the 'baseline' repo en masse on 03/11/24.
    """

    args: argparse.Namespace = parse_args()

    xx: str = args.state
    data_dir: str = "../rdabase/data"
    output_dir: str = "../../iCloud/fileout/ensembles"

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
    --plans ../../iCloud/fileout/ensembles/NC20C_RMfRSP_100_plans.json \
    --log ../../iCloud/fileout/ensembles/NC20C_RMfRSP_100_log.txt \
    --no-debug
    
    # Approximate a root map with them (from 'rdaroot')

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

    # Copy the result to the root_maps directory as NC20C_root_map.csv

    """

    print(f"# Use the root map in root_maps or")
    print(f"# Approximate a new root map:")
    print(f"# Generate an ensemble of 100 random plans (from 'rdaensemble')")
    print()
    print(f"scripts/rmfrsp_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--size 100 \\")
    print(f"--data {data_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {data_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {data_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--plans {output_dir}/{xx}20C_RMfRSP_100_plans.json \\")
    print(f"--log {output_dir}/{xx}20C_RMfRSP_100_log.txt \\")
    print(f"--no-debug")
    print()
    print(f"# Approximate a root map with them (from 'rdaroot')")
    print()
    print(f"scripts/approx_root_map.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_RMfRST_100_plans.json \\")
    print(f"--data {data_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {data_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {data_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--map ../../iCloud/fileout/rootmaps/{xx}20C_rootmap.csv \\")
    print(f"--candidates ../../iCloud/fileout/rootmaps/{xx}20C_rootcandidates.json \\")
    print(f"--log ../../iCloud/fileout/rootmaps/{xx}20C_rootlog.txt \\")
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
    --root root_maps/NC20C_root_map.csv \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
    --log ../../iCloud/fileout/ensembles/NC20C_log.txt \
    --no-debug
    """

    print(f"scripts/recom_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--data {data_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--graph {data_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--root root_maps/{xx}20C_root_map.csv \\")
    print(f"--plans {output_dir}/{xx}20C_plans.json \\")
    print(f"--log {output_dir}/{xx}20C_log.txt \\")
    print(f"--no-debug")
    print()

    """
    # Score the ensemble (from 'rdaensemble')

    scripts/score_ensemble.py \
    --state NC \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --no-debug

    """

    print(f"# Score the ensemble (from 'rdaensemble')")
    print()
    print(f"scripts/score_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans.json \\")
    print(f"--data {data_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {data_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {data_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--no-debug")
    print()

    """
    # Find the ratings frontiers in the ensemble (from 'tradeoffs')

    scripts/find_frontiers.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
    --frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
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

    scripts/SETUP.sh NC

    scripts/make_push_jobs.py \
    --state NC \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
    --zone \
    --points 100 \
    --pushes 3 \
    --cores 28 \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --output ../../iCloud/fileout/hpc_dropbox \
    --no-debug

    """

    print(f"# Generate 'push' jobs (from 'tradeoffs')")
    print()
    print(f"scripts/SETUP.sh {xx}")
    print()
    print(f"scripts/make_push_jobs.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans.json \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers.json \\")
    if args.zone:
        print(f"--zone \\")
    if args.random:
        print(f"--random \\")
    print(f"--points {args.points} \\")
    print(f"--pushes {args.pushes} \\")
    print(f"--delta {args.delta} \\")
    print(f"--cores {args.cores} \\")
    print(f"--data {data_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {data_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {data_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--output ../../iCloud/fileout/hpc_dropbox \\")
    print(f"--no-debug")
    print()

    """
    # Push the jobs to the cluster (from 'tradeoffs')
    # Submit the jobs (on the UA cluster)
    # Pull the pushed plans from the cluster (from 'tradeoffs')

    """

    print(f"# Push the jobs to the cluster (from 'tradeoffs')")
    print(f"# Submit the jobs (on the UA cluster)")
    print(f"# Pull the pushed plans from the cluster (from 'tradeoffs')")
    print()

    """
    # Collect the pushed plans into an ensemble (from 'rdaensemble')

    scripts/ensemble_from_plans.py \
    --base ../../iCloud/fileout/ensembles/NC20C_plans.json \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans_pushed.json \
    --dir ../../iCloud/fileout/hpc_dropbox/NC/pushed \
    --no-debug

    """

    print(f"# Collect the pushed plans into an ensemble (from 'rdaensemble')")
    print()
    print(f"scripts/ensemble_from_plans.py \\")
    print(f"--base {output_dir}/{xx}20C_plans.json \\")
    print(f"--plans {output_dir}/{xx}20C_plans_pushed.json \\")
    print(f"--dir ../../iCloud/fileout/hpc_dropbox/{xx}/pushed \\")
    print(f"--no-debug")
    print()

    """
    # Score the pushed plans (from 'rdaensemble')

    scripts/score_ensemble.py \
    --state NC \
    --plans ../../iCloud/fileout/ensembles/NC20C_plans_pushed.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores_pushed.csv \
    --no-debug

    """

    print(f"# Score the pushed plans (from 'rdaensemble')")
    print()
    print(f"scripts/score_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans_pushed.json \\")
    print(f"--data {data_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {data_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {data_dir}/{xx}/{xx}_2020_graph.json \\")
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
    --scores ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv \
    --metadata ../../iCloud/fileout/ensembles/NC20C_scores_pushed_metadata.json \
    --frontier ../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json \
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
    --scores ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv \
    --metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
    --notables ../../iCloud/fileout/ensembles/NC20C_notable_maps.json \
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
    --scores ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv \
    --image ../../iCloud/fileout/images/NC20C_boxplot.svg \
    --no-debug

    """

    print(f"# Make a box plot (from 'tradeoffs')")
    print()
    print(f"scripts/make_box_plot.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores_augmented.csv \\")
    print(f"--image ../../iCloud/fileout/images/{xx}20C_boxplot.svg \\")
    print(f"--no-debug")
    print()

    """
    # Make a statistics table (from 'tradeoffs')

    scripts/make_stats_table.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --output ../../iCloud/fileout/_data/NC20C_statistics.csv \
    --no-debug

    """

    print(f"# Make a statistics table (from 'tradeoffs')")
    print()
    print(f"scripts/make_stats_table.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--output ../../iCloud/fileout/_data/{xx}20C_statistics.csv \\")
    print(f"--no-debug")
    print()

    """
    # Make a notable maps ratings table (from 'tradeoffs')

    scripts/make_ratings_table.py \
    --notables ../../iCloud/fileout/ensembles/NC20C_notable_maps.json \
    --output ../../iCloud/fileout/_data/NC20C_notable_maps_ratings.csv \
    --no-debug

    """

    print(f"# Make a notable maps ratings table (from 'tradeoffs')")
    print()
    print(f"scripts/make_ratings_table.py \\")
    print(f"--notables {output_dir}/{xx}20C_notable_maps.json \\")
    print(f"--output ../../iCloud/fileout/_data/{xx}20C_notable_maps_ratings.csv \\")
    print(f"--no-debug")
    print()

    """
    # Make scatter plots (from 'tradeoffs')

    scripts/make_scatter_plots.py \
    --scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
    --frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
    --pushed ../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json \
    --notables docs/_data/notable_ratings/NC_2022_Congress_ratings.csv \
    --focus ../../iCloud/fileout/ensembles/NC20C_focus_scores.csv \
    --prefix NC20C \
    --output ../../iCloud/fileout/images \
    --no-debug

    """

    print(f"# Make scatter plots (from 'tradeoffs')")
    print()
    print(f"scripts/make_scatter_plots.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers.json \\")
    print(f"--pushed {output_dir}/{xx}20C_frontiers_pushed.json \\")
    print(f"--notables docs/_data/notable_ratings/{xx}_2022_Congress_ratings.csv \\")
    print(f"--focus {output_dir}/{xx}20C_focus_scores.csv \\")
    print(f"--prefix {xx}20C \\")
    print(f"--output ../../iCloud/fileout/images \\")
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
    # END
    """

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
    # TODO - These are mutually exclusive options, but I'm not defining them as such yet.
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
        "--delta",
        type=int,
        default=5,
        help="How much ratings can differ for a point to be considered 'near' a frontier point",
    )

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
