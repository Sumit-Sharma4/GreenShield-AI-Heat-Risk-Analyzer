from app.services.city_boundary import get_city_boundary

def generate_grids(city, step=0.01):

    city_data = get_city_boundary(city)

    bbox = city_data["boundingbox"]

    south = float(bbox[0])
    north = float(bbox[1])
    west = float(bbox[2])
    east = float(bbox[3])

    grids = []

    lat = south

    grid_id = 1

    while lat <= north:

        lon = west

        while lon <= east:

            grids.append({
                "grid_id": f"G{grid_id}",
                "lat": round(lat, 6),
                "lon": round(lon, 6)
            })

            grid_id += 1
            lon += step

        lat += step

    return grids