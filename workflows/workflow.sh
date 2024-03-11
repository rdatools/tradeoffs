# TODO - Rationalize file names
# TODO - Approximate the root map

# Generate an ensemble

scripts/recom_ensemble.py \
--state NC \
--size 1000 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--root ../../iCloud/fileout/rootmaps/NC20C_root_map.csv \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--log ../../iCloud/fileout/ensembles/NC20C_log.txt \
--no-debug

# Score the ensemble

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--no-debug

# Find the ratings frontiers in the ensemble

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--verbose \
--no-debug

# Generate 'push' jobs

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

# Push the jobs to the cluster
# Submit the jobs
# Pull the pushed plans from the cluster

# Collected the pushed plans into an ensemble

scripts/ensemble_from_plans.py \
--base ../../iCloud/fileout/ensembles/NC20C_plans.json \
--plans ../../iCloud/fileout/ensembles/NC20C_plans_pushed.json \
--dir ../../iCloud/fileout/hpc_dropbox/NC/pushed \
--no-debug

# Score the pushed plans

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_plans_pushed.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/ensembles/NC20C_scores_pushed.csv \
--no-debug

# Combine the original ensemble & pushed plans scores <<< TODO - Make a script for this

tail -n +2 ../../iCloud/fileout/ensembles/NC20C_scores_pushed.csv > ../../iCloud/fileout/ensembles/scores.tmp && mv ../../iCloud/fileout/ensembles/scores.tmp ../../iCloud/fileout/ensembles/NC20C_scores_pushed.csv
cat ../../iCloud/fileout/ensembles/NC20C_scores.csv ../../iCloud/fileout/ensembles/NC20C_scores_pushed.csv > ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv

# Find the pushed frontiers

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/ensembles/NC20C_scores_pushed_metadata.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json \
--no-debug

# ID the notable maps in the augmented ensemble

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/ensembles/NC20C_scores_metadata.json \
--notables ../../iCloud/fileout/ensembles/NC20C_notable_maps.json \
--no-debug

# Make a box plot

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores_augmented.csv \
--image ../../iCloud/fileout/images/NC20C_boxplot.svg \
--no-debug

# Make a statistics table

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--output ../../iCloud/fileout/_data/NC20C_statistics.csv \
--no-debug

# Make a notable maps ratings table

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/ensembles/NC20C_notable_maps.json \
--output ../../iCloud/fileout/_data/NC20C_notable_maps_ratings.csv \
--no-debug

# Make scatter plots w/ pre- & post-push frontiers

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/ensembles/NC20C_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_frontiers.json \
--pushed ../../iCloud/fileout/ensembles/NC20C_frontiers_pushed.json \
--notables docs/_data/notable_ratings/NC_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/ensembles/NC20C_focus_scores.csv \
--prefix NC20C \
--output ../../iCloud/fileout/images \
--no-debug

# Copy the artifacts to the fileout & then 'docs' subdirectories

scripts/DEPLOY.sh NC
