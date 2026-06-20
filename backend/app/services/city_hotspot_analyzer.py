from app.services.grid_generator import generate_grids
from app.services.hotspot_analyzer import analyze_hotspot
from app.services.reverse_geocoder import get_area_name
from app.services.smart_recommender import generate_smart_recommendation


def get_hotspots(city, sample_size=50):

    grids = generate_grids(city)

    step = max(1, len(grids) // sample_size)

    sample_grids = grids[::step][:sample_size]

    results = []

    for grid in sample_grids:

        try:

            hotspot = analyze_hotspot(
                grid["lat"],
                grid["lon"]
            )

            # Skip mostly rural locations
            if hotspot["landcover"]["built_up"] < 20:
                continue

            area_name = get_area_name(
                grid["lat"],
                grid["lon"]
            )

            landcover = hotspot["landcover"]

            landcover["heat_risk"] = hotspot["heat_risk"]

            recommendation = generate_smart_recommendation(
                grid["lat"],
                grid["lon"],
                landcover,
                area_name
            )

            recommendation["score"] = hotspot["hotspot_score"]

            # Useful for frontend map markers
            recommendation["lat"] = grid["lat"]
            recommendation["lon"] = grid["lon"]

            results.append(recommendation)

        except Exception as e:
            print("Error:", e)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:10]