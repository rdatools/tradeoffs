#!/usr/bin/env python3

"""
GENERATE THE WORKFLOW FOR A STATE

For example:

$ scripts/make_workflow.py \
--state NC \
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
    image_dir: str = f"../../iCloud/fileout/tradeoffs/{xx}/docs/assets/images"
    data_dir: str = f"../../iCloud/fileout/tradeoffs/{xx}/docs/_data"

    """
    # NC workflow
    """

    """
    # Extract the data for the state (from 'rdabase')

    scripts/preprocess_state.py -s NC

    # Re-simplify the shapes, if necessary.

    scripts/extract_shape_data.py -s NC
    """

    print(f"# Extract the data for the state (from 'rdabase')")
    print()
    print(f"scripts/preprocess_state.py -s {xx}")
    print()

    print(f"# Re-simplify the shapes, if necessary.")
    print()
    print(f"scripts/extract_shape_data.py -s {xx}")
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
    # Use the root map in root_maps -or-
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

    # Approximate a root map with them (from 'rdaroot') for use in generating an unbiased ensemble

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

    # Copy the result to the tradeoffs/root_maps directory as NC20C_root_map.csv
    """

    print(f"# Use the root map in root_maps -or-")
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
    print(
        f"# Approximate a root map with them (from 'rdaroot') for use in generating an unbiased ensemble"
    )
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
    # Generate an ensemble of 10,000 plans (from 'rdaensemble')

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

    print(f"# Generate an ensemble of 10,000 plans (from 'rdaensemble')")
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
    --filter \
    --verbose \
    --no-debug
    """

    print(f"# Find the ratings frontiers in the ensemble (from 'tradeoffs')")
    print()
    print(f"scripts/find_frontiers.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores.csv \\")
    print(f"--metadata {output_dir}/{xx}20C_scores_metadata.json \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers.json \\")
    print(f"--filter \\")
    print(f"--verbose \\")
    print(f"--no-debug")
    print()

    """
    # Hand edit "no splits" versions of the DRA Notable Maps. Save them in tradeoffs/notable_maps/MD/.
    # - These maps must assign all precincts to districts, even water-only ones; and
    # - Must have 'roughly equal' district populations using the base 2020 census.
    """

    """
    # Create ensembles optimizing each ratings dimension (from 'rdaensemble')

    scripts/recom_ensemble_optimized.py \
    --state NC \
    --size 10000 \
    --optimize proportionality \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_proportionality.json \
    --no-debug

    scripts/recom_ensemble_optimized.py \
    --state NC \
    --size 10000 \
    --optimize competitiveness \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_competitiveness.json \
    --no-debug

    scripts/recom_ensemble_optimized.py \
    --state NC \
    --size 10000 \
    --optimize minority \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_minority.json \
    --no-debug

    scripts/recom_ensemble_optimized.py \
    --state NC \
    --size 10000 \
    --optimize compactness \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_compactness.json \
    --no-debug

    scripts/recom_ensemble_optimized.py \
    --state NC \
    --size 10000 \
    --optimize splitting \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_splitting.json \
    --no-debug
    """

    print()
    print(f"# Create ensembles optimizing each ratings dimension (from 'rdaensemble')")
    print()
    print(f"scripts/recom_ensemble_optimized.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--optimize proportionality \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(
        f"--plans {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_proportionality.json \\"
    )
    print(f"--no-debug")
    print()
    print(f"scripts/recom_ensemble_optimized.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--optimize competitiveness \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(
        f"--plans {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_competitiveness.json \\"
    )
    print(f"--no-debug")
    print()
    print(f"scripts/recom_ensemble_optimized.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--optimize minority \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(
        f"--plans {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_minority.json \\"
    )
    print(f"--no-debug")
    print()
    print(f"scripts/recom_ensemble_optimized.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--optimize compactness \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(
        f"--plans {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_compactness.json \\"
    )
    print(f"--no-debug")
    print()
    print(f"scripts/recom_ensemble_optimized.py \\")
    print(f"--state {xx} \\")
    print(f"--size 10000 \\")
    print(f"--optimize splitting \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(
        f"--plans {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_splitting.json \\"
    )
    print(f"--no-debug")
    print()

    """
    # Combine the optimized ensembles (from 'rdaensemble')

    scripts/combine_ensembles.py \
    --ensembles ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_proportionality.json \
                ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_competitiveness.json \
                ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_minority.json \
                ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_compactness.json \
                ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_splitting.json \
    --output ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized.json \
    --no-debug
    """

    print(f"# Combine the optimized ensembles (from 'rdaensemble')")
    print()
    print(f"scripts/combine_ensembles.py \\")
    print(
        f"--ensembles {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_proportionality.json \\"
    )
    print(
        f"            {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_competitiveness.json \\"
    )
    print(
        f"            {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_minority.json \\"
    )
    print(
        f"            {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_compactness.json \\"
    )
    print(
        f"            {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized_splitting.json \\"
    )
    print(f"--output {output_dir}/{xx}/ensembles/{xx}20C_plans_optimized.json \\")
    print(f"--no-debug")
    print()

    """
    # Score the optimized plans (from 'rdaensemble')
    
    scripts/score_ensemble.py \
    --state NC \
    --plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized.json \
    --data ../rdabase/data/NC/NC_2020_data.csv \
    --shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
    --graph ../rdabase/data/NC/NC_2020_graph.json \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_optimized.csv \
    --no-debug
    """

    print(f"# Score the optimized plans (from 'rdaensemble')")
    print()
    print(f"scripts/score_ensemble.py \\")
    print(f"--state {xx} \\")
    print(f"--plans {output_dir}/{xx}20C_plans_optimized.json \\")
    print(f"--data {input_dir}/{xx}/{xx}_2020_data.csv \\")
    print(f"--shapes {input_dir}/{xx}/{xx}_2020_shapes_simplified.json \\")
    print(f"--graph {input_dir}/{xx}/{xx}_2020_graph.json \\")
    print(f"--scores {output_dir}/{xx}20C_scores_optimized.csv \\")
    print(f"--no-debug")
    print()

    """
    # Combine the original ensemble & optimized plans scores (from 'tradeoffs')

    scripts/COMBINE_SCORES.sh NC
    """

    print(
        f"# Combine the original ensemble & optimized plans scores (from 'tradeoffs')"
    )
    print()
    print(f"scripts/COMBINE_SCORES.sh {xx}")
    print()

    """
    # Find the optimized frontiers (from 'tradeoffs')

    scripts/find_frontiers.py \
    --scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
    --metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_optimized_metadata.json \
    --frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_optimized.json \
    --verbose \
    --no-debug
    """

    print(f"# Find the optimized frontiers (from 'tradeoffs')")
    print()
    print(f"scripts/find_frontiers.py \\")
    print(f"--scores {output_dir}/{xx}20C_scores_augmented.csv \\")
    print(f"--metadata {output_dir}/{xx}20C_scores_optimized_metadata.json \\")
    print(f"--frontier {output_dir}/{xx}20C_frontiers_optimized.json \\")
    print(f"--verbose \\")
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
    --optimized ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_optimized.json \
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
    print(f"--pushed {output_dir}/{xx}20C_frontiers_optimized.json \\")
    print(f"--notables docs/_data/notable_ratings/{xx}_2022_Congress_ratings.csv \\")
    print(f"--focus {output_dir}/{xx}20C_focus_scores.csv \\")
    print(f"--prefix {xx}20C \\")
    print(f"--output {image_dir} \\")
    print(f"--no-debug")
    print()

    """
    # Move the legend.CSV from docs/assets/images to the docs/_data directory, and
    # Deploy the results (from 'tradeoffs')

    scripts/DEPLOY.sh NC

    """

    print(
        f"# Move the legend.CSV from docs/assets/images to the docs/_data directory, and"
    )
    print(f"# Deploy the results (from 'tradeoffs')")
    print()
    print(f"scripts/DEPLOY.sh {xx}")
    print()

    """
    # Finally:
    # - Add a state page in the docs/_pages/pages directory,
    # - Add a link to the state page in docs/_pages/pages/states.markdown, and
    # - Add the state to the list in docs/index.markdown.

    # END
    """

    print(f"# Finally, activate the state in the site:")
    print(f"# - Add a state page in the docs/_pages/pages directory, and")
    print(f"# - Add a link to the state page in docs/_pages/pages/states.markdown, and")
    print(f"# - Add the state to the list in docs/index.markdown.")
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

    args: Namespace = parser.parse_args()

    return args


if __name__ == "__main__":
    main()

### END ###
