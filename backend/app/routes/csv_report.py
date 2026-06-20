from fastapi import APIRouter
from fastapi.responses import FileResponse
import csv
import tempfile

from app.services.locality_hotspot_analyzer import (
    analyze_city_localities
)

router = APIRouter()


@router.get("/hotspot-csv/{city}")
def download_hotspot_csv(city: str):

    hotspots = analyze_city_localities(city)

    hotspots = sorted(
        hotspots,
        key=lambda x: x["score"],
        reverse=True
    )[:10]

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv",
        mode="w",
        newline="",
        encoding="utf-8"
    )

    writer = csv.writer(temp)

    writer.writerow([
        "Rank",
        "Locality",
        "Heat Score",
        "Heat Index",
        "Risk",
        "Tree Cover",
        "Trees Needed"
    ])

    for h in hotspots:

        writer.writerow([
            h["rank"],
            h["name"],
            h["score"],
            h["heat_index"],
            h["risk"],
            h["landcover"]["tree_cover"],
            h["trees_needed"]
        ])

    temp.close()

    return FileResponse(
        temp.name,
        filename=f"{city}_hotspots.csv",
        media_type="text/csv"
    )