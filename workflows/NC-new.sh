# NC workflow -- revised for new strategy for approximating the ratings trade-off frontiers

# Set up the state (from 'tradeoffs')

scripts/SETUP.sh NC

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

# NOTE - Copy the result to the tradeoffs/root_maps directory as NC20C_root_map.csv

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

# Score the ensemble (from 'rdaensemble')

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--no-debug

# Find the ratings frontiers in the ensemble (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers.json \
--verbose \
--no-debug

# TODO - Create ensembles optimizing each ratings dimension (from 'rdaensemble')

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

# TODO
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

# TODO
scripts/recom_ensemble_optimized.py \
--state NC \
--size 10000 \
--optimize splitting \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized_splitting.json \
--no-debug

# TODO - Combine the optimized ensembles, e.g., NC20C_plans_optimized.json
#        For now, just copy the compactness one.

# Score the optimized plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_optimized.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_optimized.csv \
--no-debug

# Combine the original ensemble & optimized plans scores (from 'tradeoffs')

scripts/COMBINE_SCORES.sh NC

# Find the optimized frontiers (from 'tradeoffs')

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_optimized_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_optimized.json \
--verbose \
--no-debug

# ID the notable maps in the augmented ensemble (from 'rdaensemble')

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_metadata.json \
--notables ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_notable_maps.json \
--no-debug

# Make a box plot (from 'tradeoffs')

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
--image ../../iCloud/fileout/tradeoffs/NC/docs/assets/images/NC20C_boxplot.svg \
--no-debug

# Make a statistics table (from 'tradeoffs')

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20C_statistics.csv \
--no-debug

# Make a notable maps ratings table (from 'tradeoffs')

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_notable_maps.json \
--output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20C_notable_maps_ratings.csv \
--no-debug

# NOTE - Created focus scores by hand

# Make scatter plots & legend (from 'tradeoffs')

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--more ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_augmented.csv \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers.json \
--pushed ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_optimized.json \
--notables docs/_data/notable_ratings/NC_2022_Congress_ratings.csv \
--focus ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_focus_scores.csv \
--prefix NC20C \
--output ../../iCloud/fileout/tradeoffs/NC/docs/assets/images \
--no-debug

# TODO - Move the legend.CSV from docs/assets/images to the docs/_data directory

# Copy the artifacts to the fileout & then 'docs' subdirectories (from 'tradeoffs')

scripts/DEPLOY.sh NC

# END
