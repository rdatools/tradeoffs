### MD workflow for congress (8 districts) ###

# From 'rdaensemble'
# Generate an unbiased ensemble, score it, and find the pairwise ratings frontiers.

scripts/recom_ensemble.py \
--state MD \
--size 10000 \
--roughlyequal 0.01 \
--data ../rdabase/data/MD/MD_2020_data.csv \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--root ../tradeoffs/root_maps/MD20C_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans.json \
--log ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_log.txt \
--no-debug

scripts/score_ensemble.py \
--state MD \
--plantype congress \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans.json \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores.csv \
--no-debug

# From 'tradeoffs'
scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_frontiers.json \
--roughlyequal 0.01 \
--verbose \
--no-debug

# From 'rdaensemble'
# Optimize along each ratings dimension, combine the better plans into another ensemble, and score it.
# Combine the unbiased and optimized ratings, and find the new pairwise ratings frontiers.
# Finally, identify the notable maps in the augmented ensemble.

scripts/recom_ensemble_optimized.py \
--state MD \
--size 10000 \
--optimize proportionality \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_proportionality.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state MD \
--size 10000 \
--optimize competitiveness \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_competitiveness.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state MD \
--size 10000 \
--optimize minority \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_minority.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state MD \
--size 10000 \
--optimize compactness \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_compactness.json \
--no-debug

scripts/recom_ensemble_optimized.py \
--state MD \
--size 10000 \
--optimize splitting \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_splitting.json \
--no-debug

scripts/combine_ensembles.py \
--ensembles ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_proportionality.json \
            ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_competitiveness.json \
            ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_minority.json \
            ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_compactness.json \
            ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized_splitting.json \
--output ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized.json \
--no-debug

scripts/score_ensemble.py \
--state MD \
--plans ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_plans_optimized.json \
--data ../rdabase/data/MD/MD_2020_data.csv \
--shapes ../rdabase/data/MD/MD_2020_shapes_simplified.json \
--graph ../rdabase/data/MD/MD_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_optimized.csv \
--no-debug

scripts/COMBINE_SCORES.sh MD C 

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_metadata.json \
--notables ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_notable_maps.json \
--no-debug

# From 'tradeoffs'
scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_augmented.csv \
--metadata ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_optimized_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_frontiers_optimized.json \
--roughlyequal 0.01 \
--verbose \
--no-debug

# From 'tradeoffs'
# Generate the artifacts for the website: a box plot, a table of statistics,
# a ratings table for the notable maps, pairwise scatter plots, and a legend.

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_augmented.csv \
--roughlyequal 0.01 \
--image ../../iCloud/fileout/tradeoffs/MD/docs/assets/images/MD20C_boxplot.svg \
--no-debug

scripts/make_stats_table.py \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores.csv \
--roughlyequal 0.01 \
--output ../../iCloud/fileout/tradeoffs/MD/docs/_data/MD20C_statistics.csv \
--no-debug

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_notable_maps.json \
--output ../../iCloud/fileout/tradeoffs/MD/docs/_data/MD20C_notable_maps_ratings.csv \
--no-debug

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores.csv \
--more ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_scores_augmented.csv \
--frontier ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_frontiers.json \
--pushed ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_frontiers_optimized.json \
--notables docs/_data/notable_ratings/MD_2022_Upper_ratings.csv \
--focus ../../iCloud/fileout/tradeoffs/MD/ensembles/MD20C_focus_scores.csv \
--roughlyequal 0.01 \
--prefix MD20C \
--output ../../iCloud/fileout/tradeoffs/MD/docs/assets/images \
--no-debug

### END ###
