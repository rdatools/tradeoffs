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

    def __repr__(self) -> str:
        return (
            f"Feature geoid {self.id}: {self.pop} people in district id {self.district}"
        )


class District(TypedDict):
    id: DistrictID
    features: List[FeatureOffset]
    pop: int

    def __repr__(self) -> str:
        return f"District id {self.id}: {self.pop} people with {len(self.features)} features (sum: {sum(self.features)})"


BorderKey: TypeAlias = Tuple[DistrictOffset, DistrictOffset]


class Move(NamedTuple):
    features: List[FeatureOffset]  # One or more features
    from_district: DistrictOffset
    to_district: DistrictOffset

    def __repr__(self) -> str:
        return f"Features {self.features} {self.from_district} -> {self.to_district}"


Mutation: TypeAlias = List[
    Move
]  # One or more Moves between a pair of adjacent districts

### END ###
