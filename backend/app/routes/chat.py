from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_service import ask_gemini

from app.services.geocoder import get_city_coordinates
from app.services.landcover_analyzer import analyze_landcover
from app.services.heat_engine import calculate_heat_risk
from app.services.sustainability_score import (
    calculate_sustainability_score
)

router = APIRouter()


class ChatRequest(BaseModel):
    city: str
    question: str


@router.post("/chat")
def chat_with_ai(request: ChatRequest):

    city = request.city
    question = request.question

    # Get city coordinates
    location = get_city_coordinates(city)

    if "error" in location:
        return {
            "answer": "City not found."
        }

    lat = float(location["lat"])
    lon = float(location["lon"])

    # Analyze city
    landcover = analyze_landcover(
        lat,
        lon,
        radius_km=5
    )

    heat_risk = calculate_heat_risk(
        landcover["tree_cover"],
        landcover["built_up"],
        landcover["water"],
        landcover["grass"],
        landcover["cropland"],
        landcover["shrub"]
    )

    sustainability = (
        calculate_sustainability_score(
            landcover["tree_cover"],
            landcover["built_up"],
            landcover["water"],
            landcover["cropland"],
            landcover["grass"],
            landcover["shrub"]
        )
    )

    city_data = {
        "heat_risk": heat_risk,
        "sustainability": sustainability,
        "landcover": landcover
    }

    answer = ask_gemini(
        city,
        city_data,
        question
    )

    return {
        "city": city,
        "question": question,
        "answer": answer
    }