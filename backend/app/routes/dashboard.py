from fastapi import APIRouter

from app.services.locality_hotspot_analyzer import analyze_city_localities

router = APIRouter()


@router.get("/dashboard/{city}")
def city_dashboard(city: str):

    hotspots = analyze_city_localities(city)

    very_high = 0
    high = 0
    medium = 0
    low = 0

    total_trees_needed = 0

    for hotspot in hotspots:

        total_trees_needed += hotspot["trees_needed"]

        risk = hotspot["risk"]

        if risk == "Very High":
            very_high += 1

        elif risk == "High":
            high += 1

        elif risk == "Medium":
            medium += 1

        else:
            low += 1

    top_hotspot = hotspots[0] if hotspots else None

    return {

        "city": city,

        "total_localities": len(hotspots),

        "risk_distribution": {
            "very_high": very_high,
            "high": high,
            "medium": medium,
            "low": low
        },

        "trees_needed_total": total_trees_needed,

        "top_hotspot": top_hotspot

    }