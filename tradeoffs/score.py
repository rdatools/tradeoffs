"""
SCORING
"""

from typing import Any, Dict, List, Tuple, Optional

from rdabase import Assignment

import rdapy as rda
from rdascore import aggregate_data_by_district, aggregate_shapes_by_district

from .datatypes import DistrictID, GeoID
from .dra_ratings import (
    measure_proportionality,
    measure_competitiveness,
    measure_minority_opportunity,
    measure_compactness,
    measure_reock,
    measure_polsby,
    measure_splitting,
    measure_county_splitting,
    measure_district_splitting,
)


class Scorer:
    """A scorer to rate plans for a set of data & shapes."""

    _data: Dict[str, Dict[str, str | int]]
    _shapes: Dict[str, Any]
    _graph: Dict[GeoID, List[GeoID]]
    _metadata: Dict[str, Any]

    _n_districts: int
    _n_counties: int
    _county_to_index: Dict[str, int]
    _district_to_index: Dict[int | str, int]

    _assignments: List[Assignment]
    _aggregates: Optional[Dict[str, Any]]
    _district_props: Optional[List[Dict[str, Any]]]

    _partisan_metrics: Optional[Dict[str, float]]
    _minority_metrics: Optional[Dict[str, float]]
    _compactness_metrics: Optional[Dict[str, float]]
    _splitting_metrics: Optional[Dict[str, float]]

    _verbose: bool

    def __init__(
        self,
        data: Dict[str, Dict[str, str | int]],
        shapes: Dict[str, Any],
        graph: Dict[GeoID, List[GeoID]],
        metadata: Dict[str, Any],
        *,
        verbose: bool = False,
    ) -> None:
        """Pre-process data & shapes for scoring."""

        self._verbose = verbose

        self._data: Dict[str, Dict[str, str | int]] = data
        self._shapes: Dict[str, Any] = shapes
        self._graph: Dict[GeoID, List[GeoID]] = graph
        self._metadata: Dict[str, Any] = metadata

        self._n_districts: int = metadata["D"]
        self._n_counties: int = metadata["C"]
        self._county_to_index: Dict[str, int] = metadata["county_to_index"]
        self._district_to_index: Dict[int | str, int] = metadata["district_to_index"]

        self._aggregates = None
        self._district_props = None

        self._partisan_metrics = None
        self._minority_metrics = None
        self._compactness_metrics = None
        self._splitting_metrics = None

    def measure_dimensions(
        self,
        assignments: List[Assignment],
        dimensions: Tuple[str, str],
    ) -> Tuple[float, float]:
        """Evaluate a plan on a pair of dimensions."""

        self._aggregates = None
        self._district_props = None

        self._partisan_metrics = None
        self._minority_metrics = None
        self._compactness_metrics = None
        self._splitting_metrics = None

        self._assignments = assignments

        pair: List[float] = []

        for d in dimensions:
            match d:
                case "proportionality":
                    pair.append(self._measure_proportionality())
                case "competitiveness":
                    pair.append(self._measure_competitiveness())
                case "minority":
                    pair.append(self._measure_minority())
                case "compactness":
                    pair.append(self._measure_compactness())
                case "splitting":
                    pair.append(self._measure_splitting())
                case _:
                    raise ValueError(f"Unknown dimension: {d}")

        measurements: Tuple[float, float] = (pair[0], pair[1])

        return measurements

    ### PRIVATE ###

    def _get_aggregates(self) -> Dict[str, Any]:
        if self._aggregates is None:
            self._aggregates = aggregate_data_by_district(
                self._assignments,
                self._data,
                self._n_districts,
                self._n_counties,
                self._county_to_index,
                self._district_to_index,
            )

        return self._aggregates

    def _get_district_props(self) -> List[Dict[str, Any]]:
        if self._district_props is None:
            self._district_props = aggregate_shapes_by_district(
                self._assignments, self._shapes, self._graph, self._n_districts
            )

        return self._district_props

    def _get_partisan_metrics(self) -> Dict[str, float]:
        assert self._aggregates is not None
        if self._partisan_metrics is None:
            self._partisan_metrics = calc_partisan_metrics(
                self._aggregates["total_d_votes"],
                self._aggregates["total_votes"],
                self._aggregates["d_by_district"],
                self._aggregates["tot_by_district"],
            )

        return self._partisan_metrics

    def _get_minority_metrics(self) -> Dict[str, float]:
        assert self._aggregates is not None
        if self._minority_metrics is None:
            self._minority_metrics = calc_minority_metrics(
                self._aggregates["demos_totals"],
                self._aggregates["demos_by_district"],
                self._n_districts,
            )

        return self._minority_metrics

    def _get_compactness_metrics(self) -> Dict[str, float]:
        assert self._district_props is not None
        if self._compactness_metrics is None:
            self._compactness_metrics = calc_compactness_metrics(self._district_props)

        return self._compactness_metrics

    def _get_splitting_metrics(self) -> Dict[str, float]:
        assert self._aggregates is not None
        if self._splitting_metrics is None:
            self._splitting_metrics = calc_splitting_metrics(self._aggregates["CxD"])

        return self._splitting_metrics

    def _measure_proportionality(self) -> float:
        """Measure a plan's proportionality."""

        aggregates: Dict[str, Any] = self._get_aggregates()

        partisan_metrics: Dict[str, float] = self._get_partisan_metrics()
        raw_disproportionality: float = partisan_metrics["pr_deviation"]
        Vf: float = partisan_metrics["estimated_vote_pct"]
        Sf: float = partisan_metrics["estimated_seat_pct"]

        measure: float = measure_proportionality(raw_disproportionality, Vf, Sf)

        return measure

    def _measure_competitiveness(self) -> float:
        """Measure a plan's competitiveness."""

        aggregates: Dict[str, Any] = self._get_aggregates()
        partisan_metrics: Dict[str, float] = self._get_partisan_metrics()

        raw_cdf: float = partisan_metrics["competitive_district_pct"]

        measure: float = measure_competitiveness(raw_cdf)

        return measure

    def _measure_minority(self) -> float:
        """Rate a plan on minority representation."""

        aggregates: Dict[str, Any] = self._get_aggregates()

        minority_metrics: Dict[str, float] = self._get_minority_metrics()
        od: float = minority_metrics["opportunity_districts"]
        pod: float = minority_metrics["proportional_opportunities"]
        cd: float = minority_metrics["coalition_districts"]
        pcd: float = minority_metrics["proportional_coalitions"]

        measure: float = measure_minority_opportunity(od, pod, cd, pcd)

        return measure

    def _measure_compactness(self) -> float:
        """Rate a plan on compactness."""

        district_props: List[Dict[str, Any]] = self._get_district_props()

        compactness_metrics: Dict[str, float] = self._get_compactness_metrics()
        avg_reock: float = compactness_metrics["reock"]
        avg_polsby: float = compactness_metrics["polsby_popper"]

        reock_measure: float = measure_reock(avg_reock)
        polsby_measure: float = measure_polsby(avg_polsby)

        measure: float = measure_compactness(reock_measure, polsby_measure)

        return measure

    def _measure_splitting(self) -> float:
        """Rate a plan on county-district splitting."""

        aggregates: Dict[str, Any] = self._get_aggregates()

        splitting_metrics: Dict[str, float] = self._get_splitting_metrics()

        county_measure: float = measure_county_splitting(
            splitting_metrics["county_splitting"], self._n_counties, self._n_districts
        )
        district_measure: float = measure_district_splitting(
            splitting_metrics["district_splitting"], self._n_counties, self._n_districts
        )

        measure: float = measure_splitting(county_measure, district_measure)

        return measure


### HELPERS ###


def is_realistic(ratings: Tuple[int, int, int, int, int]) -> bool:
    """
    Do a set of ratings meet DRA's 'realistic' thresholds?

    See 'Realistic' @ https://medium.com/dra-2020/notable-maps-66d744933a48
    """

    thresholds: Tuple[int, int, int, int, int] = (20, 10, 0, 20, 20)

    return all(r >= t for r, t in zip(ratings, thresholds))


def calc_partisan_metrics(
    total_d_votes: int,
    total_votes: int,
    d_by_district: Dict[int, int],
    tot_by_district: Dict[int, int],
) -> Dict[str, float]:
    """Calulate *select* partisan metrics.

    NOTE - This is a subset of the metrics in the rdascore package.
    """

    partisan_metrics: Dict[str, float] = {}

    Vf: float = total_d_votes / total_votes
    Vf_array: List[float] = [
        d / tot for d, tot in zip(d_by_district.values(), tot_by_district.values())
    ]
    partisan_metrics["estimated_vote_pct"] = Vf

    N: int = len(Vf_array)

    estS: float = rda.est_seats(Vf_array)
    estSf: float = estS / N
    partisan_metrics["estimated_seat_pct"] = estSf

    bestS: int = rda.calc_best_seats(N, Vf)
    bestSf: float = bestS / N

    deviation: float = rda.calc_disproportionality_from_best(
        estSf, bestSf
    )  # This is the dis-proportionality

    cD: float = rda.est_competitive_districts(Vf_array)
    cDf: float = cD / N

    partisan_metrics["pr_deviation"] = deviation
    partisan_metrics["competitive_district_pct"] = cDf

    return partisan_metrics


# Definitions copied from rdascore package

census_fields: List[str] = [
    "TOTAL_POP",
    "TOTAL_VAP",
    "WHITE_VAP",
    "HISPANIC_VAP",
    "BLACK_VAP",
    "NATIVE_VAP",
    "ASIAN_VAP",
    "PACIFIC_VAP",
    "MINORITY_VAP",
]

total_pop_field: str = census_fields[0]
total_vap_field: str = census_fields[1]


def calc_minority_metrics(
    demos_totals: Dict[str, int],
    demos_by_district: List[Dict[str, int]],
    n_districts: int,
) -> Dict[str, float]:
    """Calculate minority metrics.

    NOTE - This is a copy of the function in the rdascore package.
    """

    statewide_demos: Dict[str, float] = {}
    for demo in census_fields[2:]:  # Skip total population & total VAP
        simple_demo: str = demo.split("_")[0].lower()
        statewide_demos[simple_demo] = (
            demos_totals[demo] / demos_totals[total_vap_field]
        )

    by_district: List[Dict[str, float]] = []
    for i in range(1, n_districts + 1):
        district_demos: Dict[str, float] = {}
        for demo in census_fields[2:]:  # Skip total population & total VAP
            simple_demo: str = demo.split("_")[0].lower()
            district_demos[simple_demo] = (
                demos_by_district[i][demo] / demos_by_district[i][total_vap_field]
            )

        by_district.append(district_demos)

    minority_metrics: Dict[str, float] = rda.calc_minority_opportunity(
        statewide_demos, by_district
    )

    return minority_metrics


def calc_compactness_metrics(
    district_props: List[Dict[str, float]]
) -> Dict[str, float]:
    """Calculate compactness metrics using implied district props.

    NOTE - This is a copy of the function in the rdascore package.
    """

    tot_reock: float = 0
    tot_polsby: float = 0

    for i, d in enumerate(district_props):
        reock: float = rda.reock_formula(d["area"], d["diameter"] / 2)
        polsby: float = rda.polsby_formula(d["area"], d["perimeter"])

        tot_reock += reock
        tot_polsby += polsby

    avg_reock: float = tot_reock / len(district_props)
    avg_polsby: float = tot_polsby / len(district_props)

    compactness_metrics: Dict[str, float] = {}
    compactness_metrics["reock"] = avg_reock
    compactness_metrics["polsby_popper"] = avg_polsby

    return compactness_metrics


def calc_splitting_metrics(CxD: List[List[float]]) -> Dict[str, float]:
    """Calculate county-district splitting metrics.

    NOTE - This is a copy of the function in the rdascore package.
    """

    all_results: Dict[str, float] = rda.calc_county_district_splitting(CxD)

    splitting_metrics: Dict[str, float] = {}
    splitting_metrics["county_splitting"] = all_results["county"]
    splitting_metrics["district_splitting"] = all_results["district"]

    # NOTE - The simple # of counties split unexpectedly is computed in dra2020/district-analytics,
    # i.e., not in dra2020/dra-analytics in the analytics proper.

    return splitting_metrics


### MAKE A ONE-ROW SCORECARD FROM A DRA MAP-ANALYTICS.JSON EXPORT ###


def cull_partisan_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Cull partisan metrics."""

    partisan_metrics: Dict[str, float] = {}

    # partisan_metrics["estimated_vote_pct"] = Vf # Not exported

    all_results: Dict = data

    partisan_metrics["pr_deviation"] = all_results["bias"]["deviation"]
    partisan_metrics["pr_seats"] = all_results["bias"]["bestS"]
    partisan_metrics["pr_pct"] = all_results["bias"]["bestSf"]
    partisan_metrics["estimated_seats"] = all_results["bias"]["estS"]
    partisan_metrics["estimated_seat_pct"] = all_results["bias"]["estSf"]
    partisan_metrics["fptp_seats"] = all_results["bias"]["fptpS"]

    partisan_metrics["disproportionality"] = all_results["bias"]["prop"]
    partisan_metrics["efficiency_gap"] = all_results["bias"]["eG"]
    partisan_metrics["gamma"] = all_results["bias"]["gamma"]

    partisan_metrics["seats_bias"] = all_results["bias"]["bS50"]
    partisan_metrics["votes_bias"] = all_results["bias"]["bV50"]
    partisan_metrics["geometric_seats_bias"] = all_results["bias"]["bSV"]
    partisan_metrics["global_symmetry"] = all_results["bias"]["gSym"]

    partisan_metrics["declination"] = all_results["bias"]["decl"]
    partisan_metrics["mean_median_statewide"] = all_results["bias"]["mMs"]
    partisan_metrics["mean_median_average_district"] = all_results["bias"]["mMd"]
    partisan_metrics["turnout_bias"] = all_results["bias"]["tOf"]
    partisan_metrics["lopsided_outcomes"] = all_results["bias"]["lO"]

    partisan_metrics["competitive_districts"] = all_results["responsiveness"]["cD"]
    partisan_metrics["competitive_district_pct"] = all_results["responsiveness"]["cDf"]

    partisan_metrics["responsiveness"] = all_results["responsiveness"]["littleR"]
    partisan_metrics["responsive_districts"] = all_results["responsiveness"]["rD"]
    partisan_metrics["responsive_district_pct"] = all_results["responsiveness"]["rDf"]
    partisan_metrics["overall_responsiveness"] = all_results["responsiveness"][
        "bigR"
    ]  # BIG 'R': Defined in Footnote 22 on P. 10
    # partisan_metrics["minimal_inverse_responsiveness"] = all_results[
    #     "responsiveness"
    # ][
    #     "mIR"
    # ]  # zeta = (1 / r) - (1 / r_sub_max) : Eq. 5.2.1

    # partisan_metrics["avg_dem_win_pct"] = all_results["averageDVf"] # Not exported
    # partisan_metrics["avg_rep_win_pct"] = (                         # Not exported
    #     1.0 - all_results["averageRVf"]
    # )  # Invert the D % to get the R %.

    return partisan_metrics


def cull_minority_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Cull minority metrics."""

    minority_metrics: Dict[str, float] = {}
    minority_metrics["opportunity_districts"] = data["minority"]["opportunityDistricts"]
    minority_metrics["proportional_opportunities"] = data["minority"][
        "proportionalOpportunities"
    ]
    minority_metrics["coalition_districts"] = data["minority"]["coalitionDistricts"]
    minority_metrics["proportionalCoalitions"] = data["minority"][
        "proportionalCoalitions"
    ]

    return minority_metrics


def cull_compactness_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Cull compactness metrics."""

    compactness_metrics: Dict[str, float] = {}
    compactness_metrics["reock"] = data["compactness"]["reock"]["raw"]
    compactness_metrics["polsby_popper"] = data["compactness"]["polsby"]["raw"]

    return compactness_metrics


def cull_splitting_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Cull county-district splitting metrics."""

    splitting_metrics: Dict[str, float] = {}
    splitting_metrics["county_splitting"] = data["splitting"]["county"]["raw"]
    splitting_metrics["district_splitting"] = data["splitting"]["district"]["raw"]

    return splitting_metrics


def cull_ratings(data: Dict[str, Any]) -> Dict[str, int]:
    """Cull ratings."""

    ratings: Dict[str, int] = {}
    ratings["proportionality"] = data["bias"]["score"]
    ratings["competitiveness"] = data["responsiveness"]["score"]
    ratings["minority"] = data["minority"]["score"]
    ratings["compactness"] = data["compactness"]["score"]
    ratings["splitting"] = data["splitting"]["score"]

    return ratings


### END ###
