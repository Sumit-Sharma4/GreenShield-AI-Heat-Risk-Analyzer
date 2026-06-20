def estimate_cooling(trees_needed, area_km2):

    trees_per_km2 = trees_needed / area_km2

    if trees_per_km2 >= 2000:
        cooling = "2.5°C - 4.0°C"
    elif trees_per_km2 >= 1000:
        cooling = "1.5°C - 2.5°C"
    elif trees_per_km2 >= 500:
        cooling = "0.5°C - 1.5°C"
    else:
        cooling = "< 0.5°C"

    return cooling