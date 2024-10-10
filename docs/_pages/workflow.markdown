---
layout: page
title: Workflow
permalink: workflow/
---

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

## Step 1 - Extract the data, shapes, and graph for the state

If they are not already extracted into the `rdabase/data/` directory,
preprocess the data, shapes, and contiguity graph for a state using the `rdabase/scripts/preprocess_state.py` script.
For example, to extract North Carolina, run:

```bash
scripts/preprocess_state.py -s NC
```

Note: For states where the shapes aren't properly connected, 
you need to use the `-a` flag and a file of graph modifications.
An example of the graph modifications can be found in the `rdabase/data/NY/NY_2020_vtd_contiguity_mods.csv`.

## Step 2 - Set up the state for trade-off analysis

To start on the trade-off analysis proper, first set up the state,
by running the `SETUP.sh` script from the root of this project.
For example, to set up North Carolina, run:

```bash
scripts/setup_state.sh NC
```

## Step 3 - Manual Steps

There are two manual steps.

### Verify the notable maps from DRA

Notable and official maps and their ratings have been pull from DRA automatically.

But for each notable map for the state and type of plan, verify that the a map looks realistic.
This means making sure that it is not obviously gaming the DRA notable map filtering
would never be accepted as a real map.
One way people do this is by using long, thin, water-only river precincts to connect disparate parts of a state.
Another is by splitting precincts and constructing a similar "bridge" with a thin line of blocks.

When this occurs, find a replacement map and use it as a proxy for the notable map:

*   Find an alternative map that meets the criteria
*   Duplicate it 
*   Rename the copy using the form `{xx} 2022 {plan_type} - {dimension}` -- 
    where `{xx}` is the state abbreviation, `{plan_type}` is `Congress`, `Upper`, or `Lower`, 
    and `{dimension}` is the notable dimension, `Proportional`, `Competitive`, `Minority`, `Compact`, or `Splitting`
*   Tag it with the `PG-NOTABLE` label, and add it to the `Trade-offs` group
*   Update the ratings in the CSV file named like `NC_2022_Congress.csv`
    in the `tradeoffs/docs/_data/notable_ratings` directory.
    The files have the suffix `_Congress.csv`, `_Upper.csv`, or `_Lower.csv` as appropriate.

This is the DRA search query for finding alternatives to notable maps:

```
cycle:2020
and state:NC
and planType:congress
and districts:14
and (complete: true and contiguous: true and freeofholes: true and equalpopulation: true)
and (proportionality: >= 20 and competitiveness: >= 10 and compactness: >= 20 and splitting: >= 20)
```

Just replace the `state`, `planType`, and number of `districts` as appropriate, and
try to find the next highest rated realistic map.

Before opening the notable map (or proxy) in the *Analyze* tab to get the ratings, 
make sure it uses these datasets:

* Shapes: 2020 Precincts
* Census: Total Population 2020 (or adjusted)
* Voting Age: Voting Age Pop 2020, and
* Election: Composite 2016-2020

Capture those ratings into the CSV file.

### Create a no-split-precincts proxy of the official map

In DRA create a proxy of the official map that doesn't any split precincts.

*   Copy the id of the official proxy map
*   Add it to the OFFICIAL_MAP_PROXIES constant
*   Combine split precincts
*   Make sure all precincts are assigned to districts, even if they are water only / zero population
*   Export the precinct-assignment file
*   Rename it to have a name of the form `{xx}_2022_{plan_type}_Official_Proxy.csv`, and
*   Finally, move it to the tradeoffs/official_maps directory.

## Steps 4, 5, 6, and 7 - Run the command-line scripts for the state

With all those inputs in hand, run each of the three automatically generated shell scripts 
for the state and type of plan, one at a time.
For example, the scripts for North Carolina are in these files:

```
workflows/NC-congress.txt
workflows/NC-upper.txt
workflows/NC-lower.txt
```

Move the resulting legend CSVs from `fileout/tradeoffs/NC/docs/assets/images` to the `docs/_data` directory.

## Step 8 - Deploy the artifacts

Deploy the resulting artifacts from the working directory to the site,
by running the `DEPLOY.sh` script from the root of this project.
For example, to deploy North Carolina, run:

```bash
scripts/deploy_state.sh NC
```

Do this once per state, after all types of plans are complete.

## Step 9 - Activate the state in the site

Finally, to make the artifacts visible on the site, you need to:

* Create a state and plan type page in the `tradeoffs/docs/_pages` directory, modeled after the existing ones.
* Add a link to state and plan type on the `tradeoffs/docs/index.markdown` page.

That's it!
