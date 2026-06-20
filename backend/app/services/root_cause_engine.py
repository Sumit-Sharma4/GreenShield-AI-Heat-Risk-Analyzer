def find_root_causes(
    tree_cover,
    built_up,
    water,
    grass,
    cropland,
    shrub
):

    causes = []

    # Tree Cover
    if tree_cover < 10:
        causes.append("Very Low Tree Cover")

    elif tree_cover < 20:
        causes.append("Low Tree Cover")

    # Grass Cover
    if grass < 5:
        causes.append("Insufficient Urban Green Spaces")

    # Shrub Cover
    if shrub < 3:
        causes.append("Low Shrub and Vegetation Density")

    # Built-up Area
    if built_up > 70:
        causes.append("Excessive Concrete Cover")

    elif built_up > 50:
        causes.append("High Built-up Area")

    # Water
    if water < 2:
        causes.append("Insufficient Water Bodies")

    elif water < 5:
        causes.append("Low Water Availability")

    # Cropland
    if cropland < 10 and built_up > 40:
        causes.append("Limited Green/Open Land")

    return causes