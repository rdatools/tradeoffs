---
layout: page
title: DRA CLI
permalink: dra-cli/
---

This page describes the DRA capabilities that I (Alec) took advantage of in developing the content for this site.

### Metadata

-   I extracted the GUIDs for official maps by state and type of map &#8212; from data/state_plans.json 
    which I copied from DRA. 
-   I collected GUIDs for notable maps by state and type of map &#8212; by hand.
    I collected the GUIDs for congressional maps for the first version of the site some time ago.
    I collected the GUIDs for state legislative maps for the current version of the site on TODO: mm-dd-yy.
-   I copied the # of districts by state and type of map &#8212; from dra-types/lib/stateinfo.ts.

### CLI Commands

I used these CLI capabilities in the workflow for the current verison of this site:

-   I duplicated maps by GUID &#8212; I duplicated all of the official & notable maps *en masse* [(1 + 5) x 42 => 252],
    for congressional plans.
    TODO: upper and lower state legislative plans.
-   Pull ratings for a map by GUID &#8212; I pulled ratings for each map at the CLI [(7 + 6) x 42 => 546].
    TODO: upper and lower state legislative plans.

I used these capabilities in the workflow for the first version of this site:

-   Export a block-assignment file for a map at the CLI, using a little known feature. 
    TODO: What is the feature?!?
-   Import a CSV, setting many map properties, and getting the resulting map & access GUIDs.
-   Edit map settings by GUID.
-   Save a map image &#8212; this is the right-click Chrome hack. 
    This capability is *not* currently exposed at the DRA CLI, but we figured out how to replicate the feature at the command line.
