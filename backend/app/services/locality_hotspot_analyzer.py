from app.services.locality_fetcher import get_city_localities
from app.services.hotspot_analyzer import analyze_hotspot
from app.services.smart_recommender import generate_smart_recommendation


def analyze_city_localities(city):

    localities = get_city_localities(city)

    results = []

    for i, locality in enumerate(localities, start=1):

        print(
            f"[{i}/{len(localities)}] Analyzing {locality['name']}..."
        )

        try:

            hotspot = analyze_hotspot(
                locality["lat"],
                locality["lon"]
            )

            landcover = hotspot["landcover"]

            # Needed by smart recommender
            landcover["heat_risk"] = hotspot["heat_risk"]

            recommendation = generate_smart_recommendation(
                locality["lat"],
                locality["lon"],
                landcover,
                locality["name"]
            )

            score = hotspot["hotspot_score"]

            results.append({

                "name": locality["name"],

                "lat": locality["lat"],
                "lon": locality["lon"],

                "google_maps":
                f"https://maps.google.com/?q={locality['lat']},{locality['lon']}",

                "score": score,

                "heat_index":
                min(100, round(score / 6, 2)),

                "risk": hotspot["heat_risk"],

                "landcover": hotspot["landcover"],

                "root_causes":
                recommendation["root_causes"],

                "trees_needed":
                recommendation["trees_needed"],

                "plantation_strategy":
                recommendation["plantation_strategy"],

                "recommendations":
                recommendation["recommendations"]

            })

        except Exception as e:

            print(
                f"Error analyzing {locality['name']}: {e}"
            )

    # Sort by hotspot score
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Add hotspot rank
    for rank, item in enumerate(results, start=1):

        item["rank"] = rank

    return results