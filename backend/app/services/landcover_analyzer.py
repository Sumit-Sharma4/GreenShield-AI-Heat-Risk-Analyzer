import ee
from datetime import datetime

ee.Initialize(project="greenshield-ai")


# ----------------------------------
# Locality / Hotspot Analysis
# ----------------------------------

def analyze_landcover(lat, lon, radius_km=1):

    point = ee.Geometry.Point([float(lon), float(lat)])

    area = point.buffer(radius_km * 1000)

    current_year = datetime.now().year

    collection = (
    ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")
    .filterBounds(area)
    .filterDate(
        f"{current_year}-01-01",
        f"{current_year}-12-31"
        )
     )
    label = collection.select("label").mode()
    


    total_pixels = (
        label.reduceRegion(
            reducer=ee.Reducer.count(),
            geometry=area,
            scale=10,
            maxPixels=1e9
        )
        .get("label")
        .getInfo()
    )

    def class_percentage(class_id):

        pixels = (
            label.eq(class_id)
            .reduceRegion(
                reducer=ee.Reducer.sum(),
                geometry=area,
                scale=10,
                maxPixels=1e9
            )
            .get("label")
            .getInfo()
        )

        if not pixels or not total_pixels:
            return 0

        return round((pixels / total_pixels) * 100, 2)

    tree_cover = class_percentage(1)
    water = class_percentage(0)
    grass = class_percentage(2)
    cropland = class_percentage(4)
    shrub = class_percentage(5)
    built_up = class_percentage(6)

    return {
        "tree_cover": tree_cover,
        "water": water,
        "grass": grass,
        "cropland": cropland,
        "shrub": shrub,
        "built_up": built_up,
        "radius_km": radius_km,
        "analysis_type": "locality"
    }


# ----------------------------------
# Whole City Boundary Analysis
# ----------------------------------

def analyze_landcover_polygon(geojson):
    print("GeoJSON Type:", geojson["type"])
    geometry = ee.Geometry(geojson)

    image = (
        ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")
        .filterBounds(geometry)
        .sort("system:time_start", False)
        .first()
    )

    label = image.select("label")

    total_pixels = (
        label.reduceRegion(
            reducer=ee.Reducer.count(),
            geometry=geometry,
            scale=10,
            maxPixels=1e10
        )
        .get("label")
        .getInfo()
    )

    def class_percentage(class_id):

        pixels = (
            label.eq(class_id)
            .reduceRegion(
                reducer=ee.Reducer.sum(),
                geometry=geometry,
                scale=10,
                maxPixels=1e10
            )
            .get("label")
            .getInfo()
        )

        if not pixels or not total_pixels:
            return 0

        return round((pixels / total_pixels) * 100, 2)

    tree_cover = class_percentage(1)
    water = class_percentage(0)
    grass = class_percentage(2)
    cropland = class_percentage(4)
    shrub = class_percentage(5)
    built_up = class_percentage(6)

    return {
        "tree_cover": tree_cover,
        "water": water,
        "grass": grass,
        "cropland": cropland,
        "shrub": shrub,
        "built_up": built_up,
        "analysis_type": "city_boundary"
    }