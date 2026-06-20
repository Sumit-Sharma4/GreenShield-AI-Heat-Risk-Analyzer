from fastapi import APIRouter
from fastapi.responses import FileResponse
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from app.routes.hotspots import get_hotspots

from app.services.cooling_potential import (
    calculate_cooling_potential
)
from app.services.locality_hotspot_analyzer import (
    analyze_city_localities
)

from app.services.geocoder import get_city_coordinates
from app.services.landcover_analyzer import analyze_landcover
from app.services.heat_engine import calculate_heat_risk
from app.services.tree_calculator import calculate_trees_needed
from app.services.root_cause_engine import find_root_causes
from app.services.recommendation_engine import generate_recommendations
from app.services.plantation_strategy import get_plantation_strategy
from app.services.sustainability_score import (
    calculate_sustainability_score
)

import tempfile

router = APIRouter()


@router.get("/report/{city}")
def generate_report(city: str):

    location = get_city_coordinates(city)

    if "error" in location:
        return location

    lat = float(location["lat"])
    lon = float(location["lon"])

    # 10 km city overview
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
        (landcover["built_up"] * 5)
        - (landcover["tree_cover"] * 3)
        - (landcover["water"] * 2),
        2
    )

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

    sustainability = calculate_sustainability_score(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["grass"],
        landcover["shrub"]
    )

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

    plantation = get_plantation_strategy(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["cropland"],
        trees_needed
    )

    hotspots = analyze_city_localities(city)

    hotspots = sorted(
    hotspots,
    key=lambda x: x["score"],
    reverse=True
    )[:10]

    print("PDF Hotspots:", len(hotspots))

    print("TOTAL HOTSPOTS:", len(hotspots))

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    doc = SimpleDocTemplate(
        temp.name
    )

    styles = getSampleStyleSheet()

    story = []

    # =====================
    # Title
    # =====================

    story.append(
        Paragraph(
            f"<b>GreenShield AI Report - {city}</b>",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 0.2 * inch)
    )

    # =====================
    # Overview
    # =====================

    story.append(
        Paragraph(
            f"Heat Risk: {heat_risk}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Heat Score: {heat_score}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Sustainability Score: "
            f"{sustainability['score']}/100 "
            f"({sustainability['grade']})",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Trees Needed: {trees_needed}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Estimated Cooling: "
            f"{cooling_potential}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Google Maps: "
            f"https://maps.google.com/?q={lat},{lon}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 0.2 * inch)
    )

    # =====================
    # Landcover
    # =====================

    story.append(
        Paragraph(
            "<b>Landcover</b>",
            styles["Heading2"]
        )
    )

    for k, v in landcover.items():

        story.append(
            Paragraph(
                f"{k}: {v}",
                styles["BodyText"]
            )
        )

    # =====================
    # New Page
    # =====================

    story.append(
        PageBreak()
    )

    # =====================
    # Root Causes
    # =====================

    story.append(
        Paragraph(
            "<b>Root Causes</b>",
            styles["Heading2"]
        )
    )

    for c in causes:

        story.append(
            Paragraph(
                f"• {c}",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1, 0.2 * inch)
    )

    # =====================
    # Recommendations
    # =====================

    story.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    for r in recommendations:

        story.append(
            Paragraph(
                f"• {r}",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1, 0.2 * inch)
    )

    # =====================
    # Plantation Strategy
    # =====================

    story.append(
        Paragraph(
            "<b>Plantation Strategy</b>",
            styles["Heading2"]
        )
    )

    for p in plantation:

        story.append(
            Paragraph(
                f"• {p}",
                styles["BodyText"]
            )
        )

    # =====================
    # Hotspots Page
    # =====================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "<b>Top 10 Heat Hotspots</b>",
            styles["Heading1"]
        )
    )

    story.append(
        Spacer(1, 0.2 * inch)
    )

    for h in hotspots[:10]:

        story.append(
            Paragraph(
                f"""
                <b>#{h['rank']} {h['name']}</b><br/>
                Heat Score: {h['score']:.2f}<br/>
                Heat Index: {h['heat_index']}<br/>
                Risk: {h['risk']}<br/>
                Tree Cover: {h['landcover']['tree_cover']}%<br/>
                Trees Needed: {h['trees_needed']}<br/>
                Google Maps:
                {h['google_maps']}
                """,
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 0.15 * inch)
        )

    doc.build(story)

    return FileResponse(
        temp.name,
        filename=f"{city}_Report.pdf",
        media_type="application/pdf"
    )