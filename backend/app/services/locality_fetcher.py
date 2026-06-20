import requests


def get_city_localities(city):

    query = f"""
[out:json][timeout:120];

area["name"="{city}"]->.searchArea;

(
  node["place"~"suburb|neighbourhood|quarter|locality"](area.searchArea);
  way["place"~"suburb|neighbourhood|quarter|locality"](area.searchArea);
  relation["place"~"suburb|neighbourhood|quarter|locality"](area.searchArea);

  way["name"]["landuse"="residential"](area.searchArea);
  relation["name"]["landuse"="residential"](area.searchArea);

  node["name"]["place"="residential"](area.searchArea);

  way["name"]["landuse"="commercial"](area.searchArea);
  relation["name"]["landuse"="commercial"](area.searchArea);

  way["name"]["landuse"="industrial"](area.searchArea);
  relation["name"]["landuse"="industrial"](area.searchArea);
);

out center;
"""

    response = requests.get(
        "https://overpass-api.de/api/interpreter",
        params={"data": query},
        headers={"User-Agent": "GreenShieldAI"}
    )

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print(response.text[:500])
        return []

    data = response.json()

    localities = []

    bad_words = [
    "school",
    "college",
    "hospital",
    "office",
    "hotel",
    "play ground",
    "apartment",
    "apartments",
    "building",
    "factory",
    "depot",
    "ashram"
          ]

    for item in data.get("elements", []):

        name = item.get("tags", {}).get("name")

        if not name:
            continue

        if any(word in name.lower() for word in bad_words):
            continue

        # Node
        if "lat" in item:
            lat = item["lat"]
            lon = item["lon"]

        # Way or Relation
        elif "center" in item:
            lat = item["center"]["lat"]
            lon = item["center"]["lon"]

        else:
            continue


        localities.append({
            "name": name.strip(),
            "lat": lat,
            "lon": lon
        })

    # Remove duplicates
    seen = set()
    filtered = []

    for loc in localities:

        key = loc["name"].strip().lower()

        if key in seen:
            continue

        seen.add(key)
        filtered.append(loc)

    print("Raw Localities:", len(localities))
    print("Unique Localities:", len(filtered))
    print("City:", city)
    for loc in filtered:
      print(loc["name"])
    return filtered