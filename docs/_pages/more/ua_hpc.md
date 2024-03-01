# University of Arizona High-Performance Cluster

One job.sh per point, multiple push_point calls per job

-----

### Locally

$ scripts/make_push_jobs.py \
--state {xx} \
--plans ../../iCloud/fileout/ensembles/{xx}20C_plans.json \
--frontier ../../iCloud/fileout/ensembles/{xx}20C_frontiers.json \
--multiplier 10 \
--data ../rdabase/data/{xx}/{xx}_2020_data.csv \
--shapes ../rdabase/data/{xx}/{xx}_2020_shapes_simplified.json \
--graph ../rdabase/data/{xx}/{xx}_2020_graph.json \
--output ../../iCloud/fileout/hpc_batch \
--no-debug

$ chmod 755 {xx}/jobs/*.sh

### Connect to the HPC

$ ssh alecr@hpc.arizona.edu


### On the HPC


$ exit