# Extract the data for the state (from 'rdabase')

scripts/preprocess_state.py -s PA

# Re-simplify the shapes, if necessary.

scripts/extract_shape_data.py -s PA

# Set up the state (from 'tradeoffs')

scripts/SETUP.sh PA

# Use the root map in root_maps -or-
# Approximate a new root map:
# Generate an ensemble of 100 random plans (from 'rdaensemble')

scripts/rmfrsp_ensemble.py \
--state PA \
--size 100 \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_RMfRSP_100_plans.json \
--log ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_RMfRSP_100_log.txt \
--no-debug

# Approximate a root map with them (from 'rdaroot') for use in generating an unbiased ensemble

scripts/approx_root_map.py \
--state PA \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_RMfRST_100_plans.json \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--map ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_rootmap.csv \
--candidates ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_rootcandidates.json \
--log ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_rootlog.txt \
--no-debug

# Copy the result to the tradeoffs/root_maps directory as PA20C_root_map.csv

# Generate an ensemble of 10,000 plans (from 'rdaensemble')

scripts/recom_ensemble.py \
--state PA \
--size 10000 \
--data ../rdabase/data/PA/PA_2020_data.csv \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--root ../tradeoffs/root_maps/PA20C_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans.json \
--log ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_log.txt \
--no-debug

## Score the ensemble (from 'rdaensemble')

scripts/score_ensemble.py \
--state PA \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans.json \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores.csv \
--no-debug

# Find the ratings frontiers in the ensemble (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_frontiers.json \
--filter \
--verbose \
--no-debug

# Hand edit "no splits" versions of the DRA Notable Maps. 
# - Save them in tradeoffs/notable_maps/MD/.
# - These maps must assign all precincts to districts, even water-only ones; and
# - Must have 'roughly equal' district populations using the base 2020 census.

# Create ensembles optimizing each ratings dimension (from 'rdaensemble')

scripts/recom_ensemble_optimized.py \
--state PA \
--size 10000 \
--optimize proportionality \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_proportionality.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state PA \
--size 10000 \
--optimize competitiveness \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_competitiveness.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state PA \
--size 10000 \
--optimize minority \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_minority.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state PA \
--size 10000 \
--optimize compactness \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_compactness.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state PA \
--size 10000 \
--optimize splitting \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_splitting.json \
--no-debug

# Combine the optimized ensembles (from 'rdaensemble')

scripts/combine_ensembles.py \
--ensembles ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_proportionality.json \
            ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_competitiveness.json \
            ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_minority.json \
            ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_compactness.json \
            ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized_splitting.json \
--output ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized.json \
--no-debug

# Score the optimized plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state PA \
--plans ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_plans_optimized.json \
--data ../rdabase/data/PA/PA_2020_data.csv \
--shapes ../rdabase/data/PA/PA_2020_shapes_simplified.json \
--graph ../rdabase/data/PA/PA_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_optimized.csv \
--no-debug

# Combine the original ensemble & optimized plans scores (from 'tradeoffs')

scripts/COMBINE_SCORES.sh PA

# Find the optimized frontiers (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_optimized_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_frontiers_optimized.json \
--verbose \
--no-debug

# ID the notable maps in the augmented ensemble (from 'rdaensemble')

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_metadata.json \
--notables ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_notable_maps.json \
--no-debug

# Make a box plot (from 'tradeoffs')

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_augmented.csv \
--image ../../iCloud/fileout/tradeoffs/PA/docs/assets/images/PA20C_boxplot.svg \
--no-debug

# Make a statistics table (from 'tradeoffs')

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores.csv \
--output ../../iCloud/fileout/tradeoffs/PA/docs/_data/PA20C_statistics.csv \
--no-debug

# Make a notable maps ratings table (from 'tradeoffs')

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_notable_maps.json \
--output ../../iCloud/fileout/tradeoffs/PA/docs/_data/PA20C_notable_maps_ratings.csv \
--no-debug

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

# Make scatter plots (from 'tradeoffs')

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores.csv \
--more ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_scores_augmented.csv \
--frontier ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_frontiers.json \
--pushed ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_frontiers_optimized.json \
--notables docs/_data/notable_ratings/PA_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/tradeoffs/PA/ensembles/PA20C_focus_scores.csv \
--prefix PA20C \
--output ../../iCloud/fileout/tradeoffs/PA/docs/assets/images \
--no-debug

# Move the legend.CSV from docs/assets/images to the docs/_data directory, and
# Deploy the results (from 'tradeoffs')

scripts/DEPLOY.sh PA

# Finally, activate the state in the site:
# - Add a state page in the docs/_pages/pages directory, and
# - Add a link to the state page in docs/_pages/pages/states.markdown, and
# - Add the state to the list in docs/index.markdown.

# END
