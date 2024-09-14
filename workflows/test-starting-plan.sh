# Scripts to to compare how the starting plan for ReCom affects the resulting ensemble.

scripts/recom_ensemble.py \
--state NC \
--size 10000 \
--roughlyequal 0.01 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--root ../tradeoffs/root_maps/NC20C_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
--log ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_log.txt \
--no-debug

scripts/score_ensemble.py \
--state NC \
--plantype upper \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--no-debug

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_metadata.json \
#--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_alt.json \
--frontier temp/NC20C_frontiers.json \
--roughlyequal 0.01 \
--verbose \
--no-debug

### RANDOM STARTING POINT ###

scripts/recom_ensemble.py \
--state NC \
--size 10000 \
--roughlyequal 0.01 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--root ../tradeoffs/root_maps/NC20C_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_alt.json \
--log ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_log_alt.txt \
--randomstart \
--no-debug

scripts/score_ensemble.py \
--state NC \
--plantype congress \
--plans ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_plans_alt.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_alt.csv \
--no-debug

scripts/find_frontiers.py \
--scores ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_alt.csv \
--metadata ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_scores_alt_metadata.json \
--frontier ../../iCloud/fileout/tradeoffs/NC/ensembles/NC20C_frontiers_alt.json \
--roughlyequal 0.01 \
--verbose \
--no-debug

# END
