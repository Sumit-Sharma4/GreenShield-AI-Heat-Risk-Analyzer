from fastapi import APIRouter
from fastapi.responses import FileResponse
import tempfile
import csv

from app.services.root_cause_engine import find_root_causes
from app.services.recommendation_engine import generate_recommendations
from app.services.plantation_strategy import (
    get_plantation_strategy
)

router = APIRouter()


@router.get("/hotspot-csv")
def download_hotspot_csv(
    name: str,
    score: float,
    heat_index: float,
    risk: str,
    tree_cover: float,
    built_up: float,
    water: float,
    grass: float,
    cropland: float,
    shrub: float,
    trees_needed: int
):

    # Generate Root Causes
    root_causes = find_root_causes(
        tree_cover,
        built_up,
        water,
        grass,
        cropland,
        shrub
    )

    # Generate Recommendations
    recommendations = generate_recommendations(
        tree_cover,
        built_up,
        water,
        grass,
        cropland,
        shrub
    )

    # Generate Plantation Strategy
    plantation_strategy = get_plantation_strategy(
        tree_cover,
        built_up,
        water,
        cropland,
        trees_needed
    )

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv",
        mode="w",
        newline="",
        encoding="utf-8"
    )

    writer = csv.writer(temp)

    # Title
    writer.writerow([
        f"{name} - 1 km Hotspot Analysis"
    ])

    writer.writerow([])

    # Basic Information
    writer.writerow([
        "Parameter",
        "Value"
    ])

    writer.writerow([
        "Locality",
        name
    ])

    writer.writerow([
        "Radius",
        "1 km"
    ])

    writer.writerow([
        "Heat Score",
        score
    ])

    writer.writerow([
        "Heat Index",
        heat_index
    ])

    writer.writerow([
        "Risk",
        risk
    ])

    writer.writerow([
        "Tree Cover (%)",
        tree_cover
    ])

    writer.writerow([
        "Built Up (%)",
        built_up
    ])

    writer.writerow([
        "Water (%)",
        water
    ])

    writer.writerow([
        "Grass (%)",
        grass
    ])

    writer.writerow([
        "Cropland (%)",
        cropland
    ])

    writer.writerow([
        "Shrub (%)",
        shrub
    ])

    writer.writerow([
        "Trees Needed",
        trees_needed
    ])

    writer.writerow([])

    # Root Causes
    writer.writerow([
        "ROOT CAUSES"
    ])

    for cause in root_causes:

        writer.writerow([
            "Cause",
            cause
        ])

    writer.writerow([])

    # Plantation Strategy
    writer.writerow([
        "PLANTATION STRATEGY"
    ])

    for item in plantation_strategy:

        writer.writerow([
            "Strategy",
            item
        ])

    writer.writerow([])

    # Recommendations
    writer.writerow([
        "RECOMMENDATIONS"
    ])

    for item in recommendations:

        writer.writerow([
            "Recommendation",
            item
        ])

    temp.close()

    filename = (
        name.replace(" ", "_")
        .replace("/", "_")
        + "_1km.csv"
    )

    return FileResponse(
        temp.name,
        filename=filename,
        media_type="text/csv"
    )