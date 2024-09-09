# NC workflow for the upper state house (50 districts)

#@ Update
# Set up the state (from 'tradeoffs'), once per state

#@ Update - alt. ensemble directories
scripts/SETUP.sh NC

# Extract the data for the state (from 'rdabase')
# Re-simplify the shapes, if necessary.

#@ Update
# Get a root map:
# - Use the root map in root_maps -or-
# - Approximate a new root map (next) -or-
# - Construct one by hand, using a map in DRA as a starting point
# Note: Districts should be indexed [1, 2, 3, ...]!

# Generate an ensemble of 100 random plans (from 'rdaensemble')

#@ Update - plan_type; roughlyequal; temp directory
scripts/rmfrsp_ensemble.py \
--state NC \
--plantype upper \
--roughlyequal 0.10 \
--size 100 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans temp/NC20U_RMfRSP_100_plans.json \
--log temp/NC20U_RMfRSP_100_log.txt \
--no-debug

# Approximate a root map with them (from 'rdaroot') for use in generating an unbiased ensemble

#@ Update - plans name; temp directory; root_map
scripts/approx_root_map.py \
--state NC \
--plans ../rdaensemble/temp/NC20U_RMfRSP_100_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--map temp/NC20U_root_map.csv \
--candidates temp/NC20U_rootcandidates.json \
--log temp/NC20U_rootlog.txt \
--no-debug

# Copy the result to the tradeoffs/root_maps directory as NC20U_root_map.csv

# Generate an ensemble of 10,000 plans (from 'rdaensemble')

#@ Update - roughlyequal
scripts/recom_ensemble.py \
--state NC \
--size 10000 \
--roughlyequal 0.10 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--root ../tradeoffs/root_maps/NC20U_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans.json \
--log ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_log.txt \
--no-debug

# Score the ensemble (from 'rdaensemble')

scripts/score_ensemble.py \
--state NC \
--plantype upper \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--no-debug

# Find the ratings frontiers in the ensemble (from 'tradeoffs')

#@ Update - filter; roughlyequal
scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_frontiers.json \
--roughlyequal 0.05 \
--verbose \
--no-debug

# MANUAL - Hand edit "no splits" versions of the DRA Notable Maps. Save them in tradeoffs/notable_maps/NC/.
# - These maps must assign all precincts to districts, even water-only ones; and
# - Must have 'roughly equal' district populations using the base 2020 census.

# Create ensembles optimizing each ratings dimension (from 'rdaensemble')

scripts/recom_ensemble_optimized.py \
--state NC \
--size 10000 \
--optimize proportionality \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_proportionality.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state NC \
--size 10000 \
--optimize competitiveness \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_competitiveness.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state NC \
--size 10000 \
--optimize minority \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_minority.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state NC \
--size 10000 \
--optimize compactness \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_compactness.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state NC \
--size 10000 \
--optimize splitting \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_splitting.json \
--no-debug

# Combine the optimized ensembles (from 'rdaensemble')

scripts/combine_ensembles.py \
--ensembles ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_proportionality.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_competitiveness.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_minority.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_compactness.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_splitting.json \
--output ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized.json \
--no-debug

# Score the optimized plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_optimized.csv \
--no-debug

# Combine the original ensemble & optimized plans scores (from 'tradeoffs')

#@ Update
scripts/COMBINE_SCORES.sh NC U -upper

# Find the optimized frontiers (from 'tradeoffs')

#@ Update - filter; roughlyequal
scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_optimized_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_frontiers_optimized.json \
--roughlyequal 0.05 \
--verbose \
--no-debug

# ID the notable maps in the augmented ensemble (from 'rdaensemble')

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_metadata.json \
--notables ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_notable_maps.json \
--no-debug

# Make a box plot (from 'tradeoffs')

#@ Update - roughlyequal
scripts/make_box_plot.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--roughlyequal 0.05 \
--image ../../iCloud/fileout/tradeoffs/NC/docs/assets/images/NC20U_boxplot.svg \
--no-debug

# Make a statistics table (from 'tradeoffs')

#@ Update - roughlyequal
scripts/make_stats_table.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--roughlyequal 0.05 \
--output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20U_statistics.csv \
--no-debug

# Make a notable maps ratings table (from 'tradeoffs')

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_notable_maps.json \
--output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20U_notable_maps_ratings.csv \
--no-debug

# MANUAL - Collect ratings for DRA Notable Maps by hand, and save them in the tradeoffs/docs/_data/notable_ratings directory.
# MANUAL - Create focus scores by hand, and save them in the fileout/tradeoffs/NC/ensembles-upper directory.

# Make scatter plots & legend (from 'tradeoffs')

#@ Update - roughlyequal
scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--more ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_frontiers.json \
--pushed ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_frontiers_optimized.json \
--notables docs/_data/notable_ratings/NC_2022_Upper_ratings.csv \
--focus ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_focus_scores.csv \
--roughlyequal 0.05 \
--prefix NC20U \
--output ../../iCloud/fileout/tradeoffs/NC/docs/assets/images \
--no-debug

# MANUAL - Move the legend.CSV from docs/assets/images to the docs/_data directory.

#@ - TODO
# Deploy the results (from 'tradeoffs')

scripts/DEPLOY.sh NC

# MANUAL - Activate the state in the site:
# - Uncomment out the <div> for the state in docs/_pages/states.markdown
# - Add the state to the list in docs/index.markdown

# END
