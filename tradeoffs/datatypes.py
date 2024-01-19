"""
DATA TYPES
"""

from typing import TypeAlias, NamedTuple, List, Dict, TypedDict

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


BorderSegment: TypeAlias = Dict[
    DistrictOffset, List[FeatureOffset]
]  # Two: one for each side/district


class Move(NamedTuple):
    features: List[FeatureOffset]
    from_district: DistrictOffset
    to_district: DistrictOffset


### END ###
