# tradeoffs/__init__.py

from .readwrite import *
from .frontiers import (
    find_frontiers,
    is_pareto_efficient_cost,
    is_pareto_efficient_value,
    line_segment_hull,
    is_near,
    is_near_any,
)
from .notable_maps import id_most_notable_maps
from .plots import bgcolor, plot_width, plot_height, buttons

name: str = "tradeoffs"
