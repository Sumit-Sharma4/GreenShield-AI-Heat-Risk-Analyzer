from app.services.root_cause_engine import find_root_causes
from app.services.recommendation_engine import generate_recommendations
from app.services.tree_calculator import calculate_trees_needed
from app.services.plantation_strategy import get_plantation_strategy


def generate_smart_recommendation(
    lat,
    lon,
    landcover,
    location_name
):

    trees_needed = calculate_trees_needed(
        landcover["tree_cover"],
        landcover["built_up"]
    )

    plantation_strategy = get_plantation_strategy(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["cropland"],
        trees_needed
    )

    return {

        "location_name": location_name,

        "latitude": lat,
        "longitude": lon,

        "google_maps":
        f"https://maps.google.com/?q={lat},{lon}",

        "heat_risk": landcover["heat_risk"],

        "landcover": {
            "tree_cover": landcover["tree_cover"],
            "grass": landcover["grass"],
            "shrub": landcover["shrub"],
            "cropland": landcover["cropland"],
            "built_up": landcover["built_up"],
            "water": landcover["water"]
        },

        "root_causes": find_root_causes(
            landcover["tree_cover"],
            landcover["built_up"],
            landcover["water"],
            landcover["grass"],
            landcover["cropland"],
            landcover["shrub"]
        ),

        "trees_needed": trees_needed,

        "plantation_strategy": plantation_strategy,

        "recommendations": generate_recommendations(
            landcover["tree_cover"],
            landcover["built_up"],
            landcover["water"],
            landcover["grass"],
            landcover["cropland"],
            landcover["shrub"]
        )
    }