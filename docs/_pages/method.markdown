---
layout: page
title: Methodology
permalink: method/
---

In the [first iteration of this analysus](https://alecramsay.github.io/pg/),
we introduced the notion of a "root map"&#8212;
the most [population compact](https://alecramsay.github.io/pg/glossary/) map for a state.
Unforunately, we found that the root map was not a good reference point for comparing human-drawn maps,
because it can't be computed definitively (only approximated) and
small changes in the approximation yielded wildly different ratings.
To use the metaphor of a landscape, rather than getting deeper and deeper into the valley containing the global minimum,
successive approximations were flipping between different valleys with local minima and very different characteristics.

In this iteration, we've taken a different approach.
In outline:

1.  We generate an unbiased ensemble of 10,000 plans for a state,
    using the ReCom algorithm implemented in [GerryChain](https://gerrychain.readthedocs.io/en/latest/).
    These plans all use whole precincts, i.e., don't split precincts with subsets of blocks in different districts.
2.  Then we score each plan in the ensemble on the five ratings dimensions in [Dave's Redistricting's](https://davesredistricting.org/) (DRA), 
    using [a high-volume offline scoring service](https://github.com/rdatools/rdascore)
    which wraps [the Python clone of DRA analytics](https://github.com/dra2020/rdapy).
3.  Next we find the Pareto frontier of the ensemble.
4.  Then we export [the Notable Maps](https://medium.com/dra-2020/notable-maps-66d744933a48) for the state from DRA and pull their ratings.
    If necessary, we make close-cousin clones of these maps that don't split any precincts for use below.
5.  We use those plans as seeds to GerryChain's [SingleMetricOptimizer and Gingelator exploratory (biased) chain algorithms](https://mggg.org/posts/gerrysuite).
    Specifically, we use the best rated map on each dimension as the starting point for the optimizer optimizing on each of the five dimensions.
    To understand this visually, think of a pair ratings dimensions, say proprtionality and compactness.
    Think of a scatter plot of proportionality (y-axis) vs. compactness (x-axis).
    The most proportional map will plot somewhere in the upper left of the plot;
    the most compact map will plot somewhere in the lower right.
    By more-or-less using those as starting points and optimizing *away* from along the other ratings dimensions,
    we're searching upper-left to lower-right and vice versa.
    We use 2,000 iterations for each optimization, so another 10,000 plans for each seed,
    but we only retain interim plans that improve the metric for which we're optimizing.
6.  We collect those plans into a new optimized ensemble and score them.
7.  We combine the unbiased ensemble and the optimized ensemble into a single ensemble and find the new Pareto frontier.
8.  Finally, we generate all the artifacts that you see and described on the state pages, e.g., for <a href="{{ site.baseurl }}/states/NC">NC</a>.

Besides the two GitHub repositories mentioned above, the main code and data for this workflow is in three repositories: [rdabase](https://github.com/rdatools/rdabase), [rdaensemble](https://github.com/rdatools/rdaensemble), and [tradeoffs](https://github.com/rdatools/tradeoffs), 
the last being where this site is hosted.
Two more repositories&#8212;[rdadccvt](https://github.com/rdatools/rdadccvt) and [rdaroot](https://github.com/rdatools/rdaroot)&#8212;package up our work on root maps, which we use as seeds to the unbiased ensembles here.