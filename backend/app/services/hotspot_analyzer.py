from app.services.landcover_analyzer import analyze_landcover
from app.services.heat_engine import calculate_heat_risk


def analyze_hotspot(lat, lon):

    landcover = analyze_landcover(lat, lon)

    risk = calculate_heat_risk(
    landcover["tree_cover"],
    landcover["built_up"],
    landcover["water"],
    landcover["grass"],
    landcover["cropland"],
    landcover["shrub"]
    )

    # Green cooling score
    green_score = (
        landcover["tree_cover"] * 1.0
        +
        landcover["grass"] * 0.6
        +
        landcover["cropland"] * 0.5
        +
        landcover["shrub"] * 0.4
    )

    # Heat hotspot score
    score = (
        (landcover["built_up"] * 4)
        +
        ((100 - green_score) * 1.5)
        +
        ((10 - min(landcover["water"], 10)) * 8)
    )

    # Penalize non-urban areas
    if landcover["built_up"] < 20:
        score *= 0.6

    return {
        "landcover": landcover,
        "heat_risk": risk,
        "hotspot_score": round(score, 2)
    }