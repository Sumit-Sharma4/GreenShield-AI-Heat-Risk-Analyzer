from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import csv
import io

router = APIRouter()

@router.get("/export/hotspots/{city}")
def export_hotspots(city: str):

    # call your hotspot generator here
    hotspots = []  # replace with actual hotspot list

    output = io.StringIO()
    writer = csv.writer(output)

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

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            f"attachment; filename={city}_hotspots.csv"
        }
    )