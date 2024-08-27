---
layout: default
---

<h2>Trade-offs in Redistricting</h2>

*This is second major iteration of ["Trade-offs in Redistricting"](https://alecramsay.github.io/pg/).
It's still a work in progress.*

The purpose of this revised site is to illuminate some quantitative policy trade-offs in congressional redistricting.
The preliminary results show several things:

1. Pairs of [Dave's Redistricting (DRA) ratings dimensions](https://medium.com/dra-2020/ratings-cc2188dc7dff) in unbiased ensembles of redistricting plans for a state are not correlated as you might expect them to be.
2. Nonetheless, there is a clear trade-off frontier between the pairs of dimensions. Since all DRA ratings are "bigger is better," these Pareto frontiers are to the upper right (north-east) in the scatter plots on state pages.
3. These unbiased frontiers can be automatically "pushed" farther to the north-east, to approximate the trade-offs that people face when drawing maps.
4. The ratings for most human-drawn maps fall near the edge or outside the range of the ratings for unbiased ensembles. Whether for bad or for good, people are intentionally optimizing for something.
5. The most compact human-drawn maps are noticeably more compact than the most compact maps in the "pushed" frontier, because they smooth out district boundaries.

These findings are meant to be directionally illustrative rather than specifically descriptive.

We've enabled three states so far: <a href="{{ site.baseurl }}/states/NC">NC</a>, <a href="{{ site.baseurl }}/states/MD">MD</a>, and <a href="{{ site.baseurl }}/states/PA">PA</a>.
More will follow.

What we do here is different from the first iteration of the site, 
due to limitations that we discovered in that approach.
The methodology we used this go around is summarized on the [Method](./_pages/method.markdown) page.