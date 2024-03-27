# SC special push workflow
# Disproportionality for the contested 2022 Official map is 27.17%.

# After setting up & running SC ...

# Generate the special SC push commands (from 'tradeoffs')

scripts/special_south_carolina.py

# Push the jobs to the cluster (from 'tradeoffs')
# Submit the jobs (on the UA cluster)
# Pull the pushed plans from the cluster (from 'tradeoffs')

# Generate an empty ensemble (from 'rdaensemble')

scripts/recom_ensemble.py \
--state SC \
--size 1 \
--data ../rdabase/data/SC/SC_2020_data.csv \
--graph ../rdabase/data/SC/SC_2020_graph.json \
--root ../tradeoffs/root_maps/SC20C_root_map.csv \
--plans ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_null_plans.json \
--log ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_null_log.txt \
--no-debug

# Remove the one plan by hand

# Collect the pushed plans into an ensemble (from 'rdaensemble')

scripts/ensemble_from_plans.py \
--base ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_null_plans.json \
--plans ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_plans_special.json \
--dir ../../iCloud/fileout/tradeoffs/SC-alt/pushed \
--no-debug

# Score the pushed plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state SC \
--plans ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_plans_special.json \
--data ../rdabase/data/SC/SC_2020_data.csv \
--shapes ../rdabase/data/SC/SC_2020_shapes_simplified.json \
--graph ../rdabase/data/SC/SC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_scores_special.csv \
--no-debug

## 

# Stair step push select initial plans

scripts/special_south_carolina_2.py

# Collect the pushed plans into an ensemble (from 'rdaensemble')

scripts/ensemble_from_plans.py \
--base ../../iCloud/fileout/tradeoffs/SC-alt/ensembles/SC20C_null_plans.json \
--plans ../../iCloud/fileout/tradeoffs/SC-alt2/ensembles/SC20C_plans_special.json \
--dir ../../iCloud/fileout/tradeoffs/SC-alt2/pushed \
--no-debug

# Score the pushed plans (from 'rdaensemble')

scripts/score_ensemble.py \
--state SC \
--plans ../../iCloud/fileout/tradeoffs/SC-alt2/ensembles/SC20C_plans_special.json \
--data ../rdabase/data/SC/SC_2020_data.csv \
--shapes ../rdabase/data/SC/SC_2020_shapes_simplified.json \
--graph ../rdabase/data/SC/SC_2020_graph.json \
--scores ../../iCloud/fileout/tradeoffs/SC-alt2/ensembles/SC20C_scores_special.csv \
--no-debug

# END
