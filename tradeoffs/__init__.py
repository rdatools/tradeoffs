# tradeoffs/__init__.py

from .frontiers import (
    find_frontiers,
    is_pareto_efficient_cost,
    is_pareto_efficient_value,
)
from .notable_maps import id_most_notable_maps
from .plots import *
from .scores import (
    cull_partisan_metrics,
    cull_minority_metrics,
    cull_compactness_metrics,
    cull_splitting_metrics,
    cull_ratings,
)
from .plan import *  # TODO - be specific
from .readwrite import *
from .datatypes import *

name: str = "tradeoffs"
