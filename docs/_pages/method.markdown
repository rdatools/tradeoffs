---
layout: page
title: Methodology
permalink: method/
---

In the [first iteration of this analysis](https://alecramsay.github.io/pg/),
we introduced the notion of a "root map"&#8212;the 
most [population compact](https://alecramsay.github.io/pg/glossary/) map for a state.
Unforunately, we found that the root map was not a good reference point for comparing human-drawn maps,
because it can't be computed definitively (only approximated) and
small changes in the approximation yielded wildly different ratings.
To use the metaphor of a landscape, rather than getting deeper and deeper into the valley containing the global minimum,
successive approximations were flipping between different valleys with local minima and very different characteristics.

In this iteration, we've taken a different approach.
In outline:

1.  We generated an unbiased ensemble of 10,000 congressional plans for a state,
    using the ReCom algorithm implemented in [GerryChain](https://gerrychain.readthedocs.io/en/latest/).
    These plans all use whole precincts, i.e., don't split precincts with subsets of blocks in different districts.
2.  Then we scored each plan in the ensemble on the five ratings dimensions in [Dave's Redistricting's](https://davesredistricting.org/) (DRA), 
    using [a high-volume offline scoring service](https://github.com/rdatools/rdascore)
    which wraps [the Python clone of DRA analytics](https://github.com/dra2020/rdapy).
    Note: We removed the clipping of minority VAP percentages below 37% that DRA's minority rating does,
    because this was causing a discontinuity (discernible gaps) in the ratings.
3.  Next we found the Pareto frontier of the ensemble.
4.  Then we exported [the Notable Maps](https://medium.com/dra-2020/notable-maps-66d744933a48) for the state from DRA and pulled their ratings.
    If necessary, we made close-cousin clones of these maps that didn't split any precincts for use below.
5.  These human-drawn plans each optimize for one of the five rating dimension, and we used them as seeds to GerryChain's [SingleMetricOptimizer and Gingelator exploratory (biased) chain algorithms](https://mggg.org/posts/gerrysuite).
6.  We used each as the starting point for seeking better-rated plans on each of the five dimensions, one at a time,
    using proxy metrics for the ratings dimensions as opposed to the actual DRA ratings.
    We used 2,000 iterations for each optimization run which generated another 10,000 plans for each seed.
    However, we only retained interim plans that improved the metric for which we were optimizing.
7.  To understand this visually, think of a pair ratings dimensions, say proprtionality and compactness.
    Think of a scatter plot of proportionality (y-axis) vs. compactness (x-axis).
    The most proportional map will plot somewhere in the upper left of the plot;
    the most compact map will plot somewhere in the lower right.
    By using those starting points and optimizing *away* from them along the other ratings dimensions,
    we, in essence, searched for conforming plans upper-left to lower-right and vice versa.
8.  We collected those plans into a new optimized ensemble and scored them.
9.  We combined the unbiased ensemble and the optimized ensemble into a single ensemble and found the new Pareto frontier.
10.  Finally, we generated all the artifacts that you see and described on the state pages, e.g., for <a href="{{ site.baseurl }}/states/NC">NC</a>.

Besides the two GitHub repositories mentioned above, the main code and data for this workflow is in three repositories: [rdabase](https://github.com/rdatools/rdabase), [rdaensemble](https://github.com/rdatools/rdaensemble), and [tradeoffs](https://github.com/rdatools/tradeoffs), 
the last being where this site is hosted.
Two more repositories&#8212;[rdadccvt](https://github.com/rdatools/rdadccvt) and [rdaroot](https://github.com/rdatools/rdaroot)&#8212;package up our work on root maps, which we use as seeds to the unbiased ensembles here.