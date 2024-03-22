# MD workflow:
# --zone: True
# --random: False
# --points: 100
# --pushes: 3
# --delta: 5
# --cores: 28
# --windfall: False

# Set up the state (from 'tradeoffs')

scripts/SETUP.sh MD

# Use the root map in root_maps or
# Approximate a new root map:
# Generate an ensemble of 100 random plans (from 'rdaensemble')

scripts/rmfrsp_ensemble.py \
--state MD \
--size 100 \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--plans ../../iCloud/fileout/ensembles/MD20C_RMfRSP_100_plans.json \
--log ../../iCloud/fileout/ensembles/MD20C_RMfRSP_100_log.txt \
--no-debug

# Approximate a root map with them (from 'rdaroot')

scripts/approx_root_map.py \
--state MD \
--plans ../../iCloud/fileout/ensembles/MD20C_RMfRST_100_plans.json \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--map ../../iCloud/fileout/rootmaps/MD20C_rootmap.csv \
--candidates ../../iCloud/fileout/rootmaps/MD20C_rootcandidates.json \
--log ../../iCloud/fileout/rootmaps/MD20C_rootlog.txt \
--no-debug

# Copy the result to the root_maps directory as MD20C_root_map.csv

scripts/recom_ensemble.py \
--state MD \
--size 10000 \
--data ../rdabase/data/MD/MD_2020_data.csv \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--root root_maps/MD20C_root_map.csv \
--plans ../../iCloud/fileout/ensembles/MD20C_plans.json \
--log ../../iCloud/fileout/ensembles/MD20C_log.txt \
--no-debug

# Score the ensemble (from 'rdaensemble')

scripts/score_ensemble.py \
--state MD \
--plans ../../iCloud/fileout/ensembles/MD20C_plans.json \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--scores ../../iCloud/fileout/ensembles/MD20C_scores.csv \
--no-debug

# Find the ratings frontiers in the ensemble (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/ensembles/MD20C_scores.csv \
--metadata ../../iCloud/fileout/ensembles/MD20C_scores_metadata.json \
--frontier ../../iCloud/fileout/ensembles/MD20C_frontiers.json \
--verbose \
--no-debug

# Generate 'push' jobs (from 'tradeoffs')

scripts/make_push_jobs.py \
--state MD \
--plans ../../iCloud/fileout/ensembles/MD20C_plans.json \
--scores ../../iCloud/fileout/ensembles/MD20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/MD20C_frontiers.json \
--zone \
--pin \
--save-at-limit \
--points 100 \
--pushes 3 \
--delta 5 \
--cores 28 \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--output ../../iCloud/fileout/hpc_dropbox \
--no-debug

# Push the jobs to the cluster (from 'tradeoffs')
# Submit the jobs (on the UA cluster)
# Pull the pushed plans from the cluster (from 'tradeoffs')

# Collect the pushed plans into an ensemble (from 'rdaensemble')

scripts/ensemble_from_plans.py \
--base ../../iCloud/fileout/ensembles/MD20C_plans.json \
--plans ../../iCloud/fileout/ensembles/MD20C_plans_pushed.json \
--dir ../../iCloud/fileout/hpc_dropbox/MD/pushed \
--no-debug

# Score the pushed plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state MD \
--plans ../../iCloud/fileout/ensembles/MD20C_plans_pushed.json \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--scores ../../iCloud/fileout/ensembles/MD20C_scores_pushed.csv \
--no-debug

# Combine the original ensemble & pushed plans scores (from 'tradeoffs')

scripts/COMBINE_SCORES.sh MD

# Find the pushed frontiers (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/ensembles/MD20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/ensembles/MD20C_scores_pushed_metadata.json \
--frontier ../../iCloud/fileout/ensembles/MD20C_frontiers_pushed.json \
--no-debug

# ID the notable maps in the augmented ensemble (from 'rdaensemble')

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/ensembles/MD20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/ensembles/MD20C_scores_metadata.json \
--notables ../../iCloud/fileout/ensembles/MD20C_notable_maps.json \
--no-debug

# Make a box plot (from 'tradeoffs')

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/ensembles/MD20C_scores_augmented.csv \
--image ../../iCloud/fileout/images/MD20C_boxplot.svg \
--no-debug

# Make a statistics table (from 'tradeoffs')

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/ensembles/MD20C_scores.csv \
--output ../../iCloud/fileout/_data/MD20C_statistics.csv \
--no-debug

# Make a notable maps ratings table (from 'tradeoffs')

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/ensembles/MD20C_notable_maps.json \
--output ../../iCloud/fileout/_data/MD20C_notable_maps_ratings.csv \
--no-debug

# Make scatter plots (from 'tradeoffs')

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/ensembles/MD20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/MD20C_frontiers.json \
--pushed ../../iCloud/fileout/ensembles/MD20C_frontiers_pushed.json \
--notables docs/_data/notable_ratings/MD_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/ensembles/MD20C_focus_scores.csv \
--prefix MD20C \
--output ../../iCloud/fileout/images \
--no-debug

# Copy the artifacts to the fileout & then 'docs' subdirectories (from 'tradeoffs')

scripts/DEPLOY.sh MD

# END
