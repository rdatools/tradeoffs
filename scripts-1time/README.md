# One-Time Scripts

I (Alec) made extensive use of command-line scripts and my role as a
[Dave\'s Redistricting](https://davesredistricting.org/) (DRA) insider
to automate what would otherwise have been a tedious and error-prone process 
of creating the content for this site &#8212; all with permission.

### Metadata

-   I extracted the ids for official maps by state and type of map from state_plans.json 
    which I copied from DRA. 
-   While I collected the ids for congressional notable maps from DRA for the first version of the site some time ago,
    I inferred notable maps for state upper &amp; lower houses &#8212; analogous to how DRA does it &#8212;
    by processing a dump of the DRA map database.
-   I copied the # of districts by state and type of map &#8212; from dra-types/lib/stateinfo.ts.

### CLI Commands

For the first &amp; current versions of this site, I used several CLI capabilities:

-   I duplicated the official &amp; notable maps by id &#8212; 800 maps &cong; (42 congressional maps + 100
    state legislative maps) x 5 ratings dimensions for each.
    In addition, I (re)named, described, labelled, and grouped everyone automatically.
-   I also pulled the ratings for each copy by id.

In the first version of this site, I also used a few other CLI capabilities:

-   I exported a block-assignment file for a map.
-   I imported a CSV, set many map properties, and got the resulting map & access ids.
-   I edited many map settings by id.
-   I saved a map image. In DRA, this is the right-click Chrome hack. 
    This capability is *not* currently exposed at the DRA CLI, but Todd &amp; figured out how to replicate 
    the feature at the command line.
