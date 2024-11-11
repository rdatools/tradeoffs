#!/bin/bash

# AN ALTERNATE VERSION OF make_artifacts.sh THAT DOES NOT SHOW THE FRONTIERS

# Default values
STATE=""
PLAN_TYPE=""

# Function to print usage
usage() {
    echo "Usage: $0 --state <STATE> --plantype <PLAN_TYPE>"
    echo "  --state     : State abbreviation (e.g., NC)"
    echo "  --plantype : Plan type (e.g., congress, upper, lower)"
    exit 1
}

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --state) STATE="$2"; shift ;;
        --plantype) PLAN_TYPE="$2"; shift ;;
        *) echo "Unknown parameter: $1"; usage ;;
    esac
    shift
done

# Check if all required parameters are provided
if [ -z "$STATE" ] || [ -z "$PLAN_TYPE" ]; then
    echo "Error: Missing required parameters."
    usage
fi

# Derive additional values

ENSEMBLES_DIR="ensembles-${PLAN_TYPE}"
if [ "$PLAN_TYPE" = "congress" ]; then
    ENSEMBLES_DIR="ensembles"
fi

LETTER="${PLAN_TYPE:0:1}"
SUFFIX=`echo "${LETTER}" | tr '[a-z]' '[A-Z]'`
PREFIX="${STATE}20${SUFFIX}"

ROUGHLY_EQUAL=0.01
if [ "$PLAN_TYPE" = "upper" ] || [ "$PLAN_TYPE" = "lower" ]; then
    ROUGHLY_EQUAL=0.10
fi

# From 'tradeoffs'
# Generate the artifacts for the website: a box plot, a table of statistics,
# a ratings table for the notable maps, pairwise scatter plots, and a legend.

# echo "Finding unbiased frontiers ..."
# scripts/find_frontiers.py \
# --scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores.csv \
# --metadata ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores_metadata.json \
# --frontier ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_frontiers.json \
# --roughlyequal $ROUGHLY_EQUAL \
# --verbose \
# --no-debug

# echo "Finding optimized frontiers ..."
# scripts/find_frontiers.py \
# --scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores_augmented.csv \
# --metadata ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores_optimized_metadata.json \
# --frontier ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_frontiers_optimized.json \
# --roughlyequal $ROUGHLY_EQUAL \
# --verbose \
# --no-debug

echo "Making box plot ..."
scripts/make_box_plot.py \
--scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores.csv \
--roughlyequal $ROUGHLY_EQUAL \
--image ../../temp/tradeoffs/${STATE}/docs/assets/images/${PREFIX}_boxplot.svg \
--no-debug
# scripts/make_box_plot.py \
# --scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores_augmented.csv \
# --roughlyequal $ROUGHLY_EQUAL \
# --image ../../temp/tradeoffs/${STATE}/docs/assets/images/${PREFIX}_boxplot.svg \
# --no-debug

echo "Making statistics table ..."
scripts/make_stats_table.py \
--scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores.csv \
--roughlyequal $ROUGHLY_EQUAL \
--output ../../temp/tradeoffs/${STATE}/docs/_data/${PREFIX}_statistics.csv \
--no-debug

echo "Making notable maps ratings table ..."
scripts/make_ratings_table.py \
--notables ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_notable_maps.json \
--output ../../temp/tradeoffs/${STATE}/docs/_data/${PREFIX}_notable_maps_ratings.csv \
--no-debug

# TODO: Add the notable maps to the scatter plots.
echo "Making scatter plots ..."
scripts/make_scatter_plots.py \
--scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_scores.csv \
--frontier ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/${PREFIX}_frontiers.json \
--focus docs/_data/focus_ratings/${PREFIX}_focus_scores.csv \
--roughlyequal $ROUGHLY_EQUAL \
--prefix $PREFIX \
--output ../../temp/tradeoffs/${STATE}/docs/assets/images \
--no-debug
# TODO: Regenerate the scatter plots with notable maps.
# scripts/make_scatter_plots.py \
# --scores ../../temp/tradeoffs/${STATE}/$ENSEMBLES_DIR/XX20C_scores.csv \
# --frontier ../../temp/tradeoffs/XX/ensembles/XX20C_frontiers.json \
# --focus docs/_data/focus_ratings/XX20C_focus_scores.csv \
# --notables docs/_data/notable_ratings/XX_2022_Congress_ratings.csv \
# --roughlyequal 0.01 \
# --prefix XX20C \
# --output ../../temp/tradeoffs/XX/docs/assets/images \
# --no-debug

echo "Done!"
echo "Now move the resulting legend the docs/_data directory."
echo 

### END ###
