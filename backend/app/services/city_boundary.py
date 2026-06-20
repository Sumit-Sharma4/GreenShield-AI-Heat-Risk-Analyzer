import requests


def get_city_boundary(city):

    url = (
        f"https://nominatim.openstreetmap.org/search?"
        f"q={city}&format=jsonv2&polygon_geojson=1"
    )

    response = requests.get(
        url,
        headers={"User-Agent": "GreenShieldAI"}
    )

    data = response.json()

    if not data:
        return None

    # Find administrative city boundary
    for item in data:

        geojson = item.get("geojson", {})

        if geojson.get("type") in [
            "Polygon",
            "MultiPolygon"
        ]:
            return item

    return None