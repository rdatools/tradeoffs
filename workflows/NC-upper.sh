### NC workflow for the upper state house (50 districts) ###

# From 'rdaensemble'
# Generate an unbiased ensemble, score it, and find the pairwise ratings frontiers.

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

scripts/score_ensemble.py \
--state NC \
--plantype upper \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--no-debug

# From 'tradeoffs'
scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_frontiers.json \
--roughlyequal 0.05 \
--verbose \
--no-debug

# From 'rdaensemble'
# Optimize along each ratings dimension, combine the better plans into another ensemble, and score it.
# Combine the unbiased and optimized ratings, and find the new pairwise ratings frontiers.
# Finally, identify the notable maps in the augmented ensemble.

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

scripts/combine_ensembles.py \
--ensembles ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_proportionality.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_competitiveness.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_minority.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_compactness.json \
            ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized_splitting.json \
--output ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized.json \
--no-debug

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_plans_optimized.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_optimized.csv \
--no-debug

scripts/COMBINE_SCORES.sh NC U -upper

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_metadata.json \
--notables ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_notable_maps.json \
--no-debug

# From 'tradeoffs'
scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_optimized_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_frontiers_optimized.json \
--roughlyequal 0.05 \
--verbose \
--no-debug

# From 'tradeoffs'
# Generate the artifacts for the website: a box plot, a table of statistics,
# a ratings table for the notable maps, pairwise scatter plots, and a legend.

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores_augmented.csv \
--roughlyequal 0.05 \
--image ../../iCloud/fileout/tradeoffs/NC/docs/assets/images/NC20U_boxplot.svg \
--no-debug

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_scores.csv \
--roughlyequal 0.05 \
--output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20U_statistics.csv \
--no-debug

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/tradeoffs/NC/ensembles-upper/NC20U_notable_maps.json \
--output ../../iCloud/fileout/tradeoffs/NC/docs/_data/NC20U_notable_maps_ratings.csv \
--no-debug

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

### END ###
