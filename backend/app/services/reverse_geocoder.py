import requests


def get_area_name(lat, lon):

    url = (
        f"https://nominatim.openstreetmap.org/reverse?"
        f"lat={lat}&lon={lon}&format=json"
    )

    try:

        response = requests.get(
            url,
            headers={"User-Agent": "GreenShieldAI"},
            timeout=30
        )

        data = response.json()

        address = data.get("address", {})

        return (
            address.get("suburb")
            or address.get("neighbourhood")
            or address.get("city_district")
            or address.get("quarter")
            or address.get("village")
            or address.get("town")
            or address.get("city")
            or address.get("county")
            or "Unknown Area"
        )

    except Exception:

        return "Unknown Area"