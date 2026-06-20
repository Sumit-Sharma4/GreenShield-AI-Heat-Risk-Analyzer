import ee

ee.Initialize(project="greenshield-ai")


def get_land_cover(lat, lon):

    point = ee.Geometry.Point([float(lon), float(lat)])

    image = (
        ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")
        .filterBounds(point)
        .sort("system:time_start", False)
        .first()
    )

    return image.getInfo()