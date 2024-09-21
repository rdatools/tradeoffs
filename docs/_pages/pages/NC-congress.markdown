---
layout: state
title: North Carolina Congress
permalink: states/NC-congress/

small-radar-width: 300
big-radar-width: 500
map-width: 700

xx: "NC"
plan-type: "Congress"
suffix: "20C"
---

{% assign state = site.data.states | where:"xx", xx | first %}
{% assign plan-lower = plan-type | downcase %}

<p>{{ state["name"] }} has {{ state["counties"] counties }}, TBD {{ plan-lower }} state house districts, and a total population of {{ state["population"] }}. </p>