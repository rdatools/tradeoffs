"""
MAKE A ONE-ROW SCORECARD FROM A DRA MAP-ANALYTICS.JSON EXPORT
"""

from typing import Any, Dict, List


def cull_partisan_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Cull partisan metrics."""

    partisan_metrics: Dict[str, float] = dict()

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

    minority_metrics: Dict[str, float] = dict()
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

    compactness_metrics: Dict[str, float] = dict()
    compactness_metrics["reock"] = data["compactness"]["reock"]["raw"]
    compactness_metrics["polsby_popper"] = data["compactness"]["polsby"]["raw"]

    return compactness_metrics


def cull_splitting_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Cull county-district splitting metrics."""

    splitting_metrics: Dict[str, float] = dict()
    splitting_metrics["county_splitting"] = data["splitting"]["county"]["raw"]
    splitting_metrics["district_splitting"] = data["splitting"]["district"]["raw"]

    return splitting_metrics


def cull_ratings(data: Dict[str, Any]) -> Dict[str, int]:
    """Cull ratings."""

    ratings: Dict[str, int] = dict()
    ratings["proportionality"] = data["bias"]["score"]
    ratings["competitiveness"] = data["responsiveness"]["score"]
    ratings["minority"] = data["minority"]["score"]
    ratings["compactness"] = data["compactness"]["score"]
    ratings["splitting"] = data["splitting"]["score"]

    return ratings


### END ###
