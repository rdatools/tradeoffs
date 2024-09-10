# Workflow

This page documents the overall workflow for generating the trade-off frontiers for a state.
Most of the steps are a series of shell scripts noted below.
This note describes the manual steps that are required, before and after running those scripts.

These notes assume that you have these `rdatools` repositories cloned to the same parent directory:

* `rdabase`
* `rdaroot`
* `rdaensemble`
* `tradeoffs`

These notes also assume a working directory outside the above repositories not under source control.
I use `fileout/tradeoffs`, for example, and have a subdirectory for each state, such as `fileout/tradeoffs/NC`.

## Extract the data, shapes, and graph for the state

If they are not already extracted into the `rdabase/data/` directory,
preprocess the data, shapes, and contiguity graph for a state using the `rdabase/scripts/preprocess_state.py` script.
For example, to extract North Carolina, run:

```bash
scripts/preprocess_state.py -s NC
```

Note: For states where the shapes aren't properly connected, 
you need to use the `-a` flag and a file of graph modifications.
An example of the graph modifications can be found in the `rdabase/data/NY/NY_2020_vtd_contiguity_mods.csv`.

## Set up the state for trade-off analysis

To start on the trade-off analysis proper, first set up the state,
by running the `SETUP.sh` script from the root of this project.
For example, to set up North Carolina, run:

```bash
scripts/SETUP.sh NC
```

## Create an approximate 'root map'

In addition to the various input "data" files noted above, this workflow needs 
a 'root map' as the starting point for generating an ensemble of plans.
You can take one of three approaches to get a root map:

1. Use the root map in the `tradeoffs/root_maps` directory -- these have already been generated for congressional plans; or
2. Automatically approximate a new root map, using the commands described below; or
3. Construct one by hand, using a map in DRA as a starting point

Note: The map must not split any precincts, and districts should be indexed 1, 2, 3, ... (i.e., not zero-based).

These are the steps to automatically generate an approximate root map, 
using North Carolina, as an example.

First, generate an ensemble of 100 random plans (from the `rdaensemble` root directory).

```bash
scripts/rmfrsp_ensemble.py \
--state NC \
--plantype congress \
--roughlyequal 0.01 \
--size 100 \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--plans temp/NC20_100_plans.json \
--log temp/NC20_100_log.txt \
--no-debug
```

For the `plantype` argument, use `congress`, `upper`, or `lower` as appropriate.
For the `roughlyequal` argument, use `0.01` for Congress and `0.05` for the Upper and Lower Houses.

Then (from `rdaroot` root directory) use that ensemble to approximate a root map.

```bash
scripts/approx_root_map.py \
--state NC \
--plans ../rdaensemble/temp/NC20_100_plans.json \
--data ../rdabase/data/NC/NC_2020_data.csv \
--shapes ../rdabase/data/NC/NC_2020_shapes_simplified.json \
--graph ../rdabase/data/NC/NC_2020_graph.json \
--map temp/root_map.csv \
--candidates temp/NC20C_rootcandidates.json \
--log temp/NC20C_rootlog.txt \
--no-debug
```

Finally, copy the resulting root map to the `tradeoffs/root_maps` directory,
with a file name of the form `NC20C_root_map.csv`
where the capital letter after the `20` is the type of plan (C for Congress, U for Upper, L for Lower).

## Capture the DRA Notable Maps

Another input that this workflow needs is the ratings for DRA Notable Maps for the state and type of plan.

Collect ratings for these maps into a CSV file modeled after `NC_2022_Congress.csv` 
in the `tradeoffs/docs/_data/notable_ratings` directory.
The files should have the suffix `_Congress.csv`, `_Upper.csv`, or `_Lower.csv` as appropriate.
Make sure the maps use these datasets:

* Shapes: 2020 Precincts
* Census: Total Population 2020
* Voting Age: Voting Age Pop 2020, and
* Election: Composite 2016-2020

Sometimes the map automatically selected by DRA as the "Notable Map" is patently not a "reasonable" map,
in the sense that it is clearly gaming DRA filtering and would never be accepted as a real map.
When this occurs, find a replacement and use it as a proxy.
This is the DRA search query for finding alternatives to Notable Maps:

```
cycle:2020
and state:NC
and planType:congress
and districts:14
and (complete: true and contiguous: true and freeofholes: true and equalpopulation: true)
and (proportionality: >= 20 and competitiveness: >= 10 and compactness: >= 20 and splitting: >= 20)
```

Just replace the `state`, `planType`, and number of `districts` as appropriate.

## Create "no splits" versions of the DRA Notable Maps

The workflow also needs is versions of these Notable Maps that do not split any precincts.
Use DRA to duplicate the Notable Maps, and then manually edit them to remove any splits.
Export the precinct-assignment files from DRA.
Rename them to be of the form `NC_2022_Congress_Proportional_NOSPLITS.csv`.
Save them in the `tradeoffs/notable_maps/NC/` directory.

Note: These maps must assign all precincts to districts, even water-only ones, and
they must have 'roughly equal' district populations using the base 2020 census
that are appropriate for the type of plan (< 1% for congressional, < 10% for upper and lower state houses).

## Capture ratings for "focus" plans

The last input required for this workflow is a set of ratings for plans that you want to highlight on the scatter plots.
These are called "focus" plans.
We highlighting the most recent one or two official plans.
Similar to the process for notable maps above, collect the ratings for these maps into a CSV file modeled after `NC20C_focus_scores.csv`
in the `fileout/tradeoffs/NC/ensembles` directory.
As above, the capital letter after the `20` is the type of plan (C for Congress, U for Upper, L for Lower).
(Note: That location is specific to my personal setup; you should adjust as needed.)

## Run the command-line script for the state

With all those inputs prepared, run each of the automatically generated shell scripts 
for the state and type of plan, one at a time.
For example, run the scripts for North Carolina Congress are in this file:

```bash
workflows/NC-congress.sh
```

For each state, there are three such workflows: one for Congress, one for the Upper House, and one for the Lower House.

Move the resulting legend CSV from `fileout/tradeoffs/NC/docs/assets/images` to the `docs/_data` directory.

## Deploy the artifacts

Deploy the resulting artifacts from the working directory to the site,
by running the `DEPLOY.sh` script from the root of this project.
For example, to deploy North Carolina, run:

```bash
scripts/DEPLOY.sh NC
```

Do this once per state, after all types of plans are complete.

## Activate the state in the site

To make the artifacts visible on the site, you need to:

* Create state and plan type pages in the `tradeoffs/docs/_pages` directory, modeled after the existing ones.
* Add a link to state and plan type on the `tradeoffs/docs/index.markdown` page.

That's it!
