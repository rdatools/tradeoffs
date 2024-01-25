"""
DATA TYPES
"""

from typing import TypeAlias, NamedTuple, List, Dict, Tuple, TypedDict

GeoID: TypeAlias = str
DistrictID: TypeAlias = int | str

FeatureOffset: TypeAlias = int
DistrictOffset: TypeAlias = int

Name: TypeAlias = str
Weight: TypeAlias = float


class Feature(NamedTuple):
    id: GeoID
    district: DistrictID
    pop: int


class District(TypedDict):
    id: DistrictID
    features: List[FeatureOffset]
    pop: int


BorderKey: TypeAlias = Tuple[DistrictOffset, DistrictOffset]


class Move(NamedTuple):
    features: List[FeatureOffset]  # One or more features
    from_district: DistrictOffset
    to_district: DistrictOffset


Mutation: TypeAlias = List[
    Move
]  # One or more Moves between a pair of adjacent districts

### END ###
