def calculate_heat_risk(
    tree_cover,
    built_up,
    water,
    grass,
    cropland,
    shrub
):

    score = 0

    green_score = (
        tree_cover * 1.0
        +
        grass * 0.6
        +
        cropland * 0.5
        +
        shrub * 0.4
    )

    # Green cover impact
    if green_score < 15:
        score += 40

    elif green_score < 30:
        score += 20

    # Built-up impact
    if built_up > 70:
        score += 40

    elif built_up > 50:
        score += 20

    # Water impact
    if water < 2:
        score += 20

    elif water < 5:
        score += 10

    if score >= 80:
        return "Very High"

    elif score >= 60:
        return "High"

    elif score >= 40:
        return "Medium"

    return "Low"