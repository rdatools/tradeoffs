# ... approximate the root map ...

scripts/recom_ensemble.py \
--state NC \
--size 1000 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--root ../../iCloud/fileout/rootmaps/NC20C_root_map.csv \
--plans ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_plans.json \
--log ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_log.txt \
--no-debug

scripts/score_ensemble.py \
--state NC \
--plans ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--no-debug

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--metadata ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores_metadata.json \
--frontier ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_frontiers.json \
--verbose \
--no-debug

...

scripts/push_plan.py \
--state NC \
--plan ../../iCloud/fileout/intermediate/NC20C_0804_map.csv \
--dimensions proportionality competitiveness \
--seed 518 \
--multiplier 1 \
--prefix NC20C_proportionality_competitiveness_00 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--output ../../iCloud/fileout/temp \
--log ../../iCloud/fileout/temp/NC20C_0804_log.txt \
--verbose \
--no-debug

...

scripts/flatten_scorecard.py \
--export ../../iCloud/fileout/ensembles/NC_2024_Congressional_analytics.json \
--name NC_2024_Congressional \
--scores ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
--no-debug

scripts/make_box_plot.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--focus ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
--image ../../iCloud/fileout/artifacts/NC20C_1K_boxplot.png \
--no-debug

scripts/make_scatter_plots.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--frontier ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_frontiers.json \
--focus ../../iCloud/fileout/ensembles/NC_2024_Congressional_scores.csv \
--prefix NC20C \
--suffix 1K \
--output ../../iCloud/fileout/artifacts/ \
--no-debug

scripts/id_notable_maps.py \
--scores ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores.csv \
--metadata ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_scores_metadata.json \
--notables ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_notables_maps.json \
--no-debug

scripts/make_ratings_table.py \
--notables ../../iCloud/fileout/ensembles/NC20C_ReCom_1K_notables_maps.json \
--output ../../iCloud/fileout/artifacts/NC20C_ReCom_1K_notables_maps_ratings.csv \
--no-debug
