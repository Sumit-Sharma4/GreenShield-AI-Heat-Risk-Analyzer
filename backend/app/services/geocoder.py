import requests


def get_city_coordinates(city):

    url = (
        "https://nominatim.openstreetmap.org/search"
        f"?q={city}"
        "&format=json"
        "&limit=1"
    )

    try:

        response = requests.get(
            url,
            headers={"User-Agent": "GreenShieldAI"},
            timeout=30
        )

        data = response.json()

        if not data:
            return {"error": "City not found"}

        return {
            "city": city,
            "lat": float(data[0]["lat"]),
            "lon": float(data[0]["lon"])
        }

    except Exception as e:

        return {
            "error": str(e)
        }