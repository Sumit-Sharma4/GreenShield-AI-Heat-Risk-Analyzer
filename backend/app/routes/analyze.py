from fastapi import APIRouter
from app.services.cooling_potential import (
    calculate_cooling_potential
)

from app.services.sustainability_score import (
    calculate_sustainability_score
)
from app.services.city_boundary import get_city_boundary
from app.services.landcover_analyzer import (
    analyze_landcover_polygon
)
from app.services.geocoder import get_city_coordinates
from app.services.landcover_analyzer import analyze_landcover
from app.services.heat_engine import calculate_heat_risk
from app.services.root_cause_engine import find_root_causes
from app.services.recommendation_engine import generate_recommendations
from app.services.tree_calculator import calculate_trees_needed
from app.services.plantation_strategy import get_plantation_strategy

router = APIRouter()


@router.get("/analyze/{city}")
def analyze_city(city: str):

    location = get_city_coordinates(city)

    if "error" in location:
        return location

    lat = float(location["lat"])
    lon = float(location["lon"])

    # City overview analysis (10 km radius)
    landcover = analyze_landcover(
        lat,
        lon,
        radius_km=10
    )

    heat_risk = calculate_heat_risk(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["grass"],
        landcover["cropland"],
        landcover["shrub"]
    )

    heat_score = round(
    min(
        100,
        (
            landcover["built_up"] * 1.5
            - landcover["tree_cover"]
            - landcover["water"] * 0.5
        )
    ),
    2
 )

    heat_score = max(0, heat_score)

    causes = find_root_causes(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["grass"],
        landcover["cropland"],
        landcover["shrub"]
    )

    recommendations = generate_recommendations(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["grass"],
        landcover["cropland"],
        landcover["shrub"]
    )

    # Area covered by 5 km radius
    area_km2 = 3.14 * 10 * 10

    trees_needed = calculate_trees_needed(
        landcover["tree_cover"],
        landcover["built_up"],
        target_tree_cover=15,
        area_km2=area_km2
    )

    cooling_potential = calculate_cooling_potential(
    trees_needed
    )

    plantation_strategy = get_plantation_strategy(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["cropland"],
        trees_needed
    )

    sustainability = calculate_sustainability_score(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["cropland"],
        landcover["grass"],
        landcover["shrub"]
    )

    return {

        "city": city,

        "coordinates": {
            "lat": lat,
            "lon": lon
        },

        "google_maps":
        f"https://maps.google.com/?q={lat},{lon}",

        "analysis_type": "10km_city_overview",

        "landcover": landcover,

        "heat_risk": heat_risk,

        "heat_score": heat_score,

        "root_causes": causes,

        "trees_needed": trees_needed,

        "cooling_potential": cooling_potential,

        "plantation_strategy": plantation_strategy,

        "recommendations": recommendations,

        "sustainability": sustainability
    }