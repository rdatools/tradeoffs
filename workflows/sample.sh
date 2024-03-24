# XX workflow:
# --zone: True
# --random: False
# --points: 100
# --pushes: 3
# --delta: 5
# --cores: 28
# --windfall: False

# Generate the data (from 'rdabase')

scripts/preprocess_state.py -s XX

# Set up the state (from 'tradeoffs')

scripts/SETUP.sh XX

# Use the root map in root_maps or
# Approximate a new root map:
# Generate an ensemble of 100 random plans (from 'rdaensemble')

scripts/rmfrsp_ensemble.py \
--state XX \
--size 100 \
--data ../rdabase/data/XX/XX_2020_data.csv \
--shapes ../rdabase/data/XX/XX_2020_shapes_simplified.json \
--graph ../rdabase/data/XX/XX_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_RMfRSP_100_plans.json \
--log ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_RMfRSP_100_log.txt \
--no-debug

# Approximate a root map with them (from 'rdaroot')

scripts/approx_root_map.py \
--state XX \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_RMfRST_100_plans.json \
--data ../rdabase/data/XX/XX_2020_data.csv \
--shapes ../rdabase/data/XX/XX_2020_shapes_simplified.json \
--graph ../rdabase/data/XX/XX_2020_graph.json \
--map ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_rootmap.csv \
--candidates ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_rootcandidates.json \
--log ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_rootlog.txt \
--no-debug

# Copy the result to the root_maps directory as XX20C_root_map.csv

# Generate an ensemble (from 'rdaensemble')

scripts/recom_ensemble.py \
--state XX \
--size 10000 \
--data ../rdabase/data/XX/XX_2020_data.csv \
--graph ../rdabase/data/XX/XX_2020_graph.json \
--root ../tradeoffs/root_maps/XX20C_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_plans.json \
--log ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_log.txt \
--no-debug

# Score the ensemble (from 'rdaensemble')

scripts/score_ensemble.py \
--state XX \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_plans.json \
--data ../rdabase/data/XX/XX_2020_data.csv \
--shapes ../rdabase/data/XX/XX_2020_shapes_simplified.json \
--graph ../rdabase/data/XX/XX_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores.csv \
--no-debug

# Find the ratings frontiers in the ensemble (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_frontiers.json \
--verbose \
--no-debug

# Generate 'push' jobs (from 'tradeoffs')

scripts/make_push_jobs.py \
--state XX \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_plans.json \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores.csv \
--frontier ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_frontiers.json \
--zone \
--delta 5 \
--pin \
--save-at-limit \
--points 100 \
--pushes 3 \
--cores 28 \
--data ../rdabase/data/XX/XX_2020_data.csv \
--shapes ../rdabase/data/XX/XX_2020_shapes_simplified.json \
--graph ../rdabase/data/XX/XX_2020_graph.json \
--output ../../iCloud/fileout/tradeoffs \
--no-debug

# Push the jobs to the cluster (from 'tradeoffs')
# Submit the jobs (on the UA cluster)
# Pull the pushed plans from the cluster (from 'tradeoffs')

# Collect the pushed plans into an ensemble (from 'rdaensemble')

scripts/ensemble_from_plans.py \
--base ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_plans.json \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_plans_pushed.json \
--dir ../../iCloud/fileout/tradeoffs/XX/pushed \
--no-debug

# Score the pushed plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state XX \
--plans ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_plans_pushed.json \
--data ../rdabase/data/XX/XX_2020_data.csv \
--shapes ../rdabase/data/XX/XX_2020_shapes_simplified.json \
--graph ../rdabase/data/XX/XX_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_pushed.csv \
--no-debug

# Combine the original ensemble & pushed plans scores (from 'tradeoffs')

scripts/COMBINE_SCORES.sh XX

# Find the pushed frontiers (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_pushed_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_frontiers_pushed.json \
--no-debug

# ID the notable maps in the augmented ensemble (from 'rdaensemble')

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_metadata.json \
--notables ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_notable_maps.json \
--no-debug

# Make a box plot (from 'tradeoffs')

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_augmented.csv \
--image ../../iCloud/fileout/tradeoffs/XX/docs/assets/images/XX20C_boxplot.svg \
--no-debug

# Make a statistics table (from 'tradeoffs')

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores.csv \
--output ../../iCloud/fileout/tradeoffs/XX/docs/_data/XX20C_statistics.csv \
--no-debug

# Make a notable maps ratings table (from 'tradeoffs')

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_notable_maps.json \
--output ../../iCloud/fileout/tradeoffs/XX/docs/_data/XX20C_notable_maps_ratings.csv \
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
--scores ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores.csv \
--more ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_scores_augmented.csv \
--frontier ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_frontiers.json \
--pushed ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_frontiers_pushed.json \
--notables docs/_data/notable_ratings/XX_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/tradeoffs/XX/ensembles/XX20C_focus_scores.csv \
--prefix XX20C \
--output ../../iCloud/fileout/tradeoffs/XX/docs/assets/images \
--no-debug

# Copy the artifacts to the fileout & then 'docs' subdirectories (from 'tradeoffs')

scripts/DEPLOY.sh XX

# END
