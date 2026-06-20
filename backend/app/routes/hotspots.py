from fastapi import APIRouter

from app.services.locality_hotspot_analyzer import analyze_city_localities

router = APIRouter()


@router.get("/hotspots/{city}")
def get_hotspots(city: str):

    results = analyze_city_localities(city)

    return {
        "city": city,
        "total_localities": len(results),
        "hotspots": results[:10]
    }