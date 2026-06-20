def generate_recommendations(
    tree_cover,
    built_up,
    water,
    grass,
    cropland,
    shrub
):

    recommendations = []

    # Extreme Urban Heat Hotspot
    if built_up > 75 and tree_cover < 2:

        recommendations.append(
            "High Priority: Implement cool roofs on commercial and residential buildings"
        )

        recommendations.append(
            "High Priority: Develop roadside plantation corridors using Neem, Arjun and Jamun trees"
        )

        recommendations.append(
            "Medium Priority: Install vertical gardens on large buildings and boundary walls"
        )

    # Moderate Urban Heat Zone
    elif built_up > 50 and tree_cover < 5:

        recommendations.append(
            "High Priority: Develop urban forests and community parks"
        )

        recommendations.append(
            "Medium Priority: Increase plantation in open public spaces"
        )

    # Low Tree Cover
    elif tree_cover < 10:

        recommendations.append(
            "Increase tree plantation in available open spaces"
        )

    # Grass Cover
    if grass < 5:

        recommendations.append(
            "Develop urban lawns, roadside grass strips and green medians"
        )

    # Shrub Cover
    if shrub < 3:

        recommendations.append(
            "Plant native shrubs and hedges to improve micro-climate and biodiversity"
        )

    # Cropland
    if cropland < 10 and built_up > 40:

        recommendations.append(
            "Promote community gardens and urban agriculture in available spaces"
        )

    # Water Recommendations
    if water < 1:

        recommendations.append(
            "High Priority: Restore water bodies and construct rainwater retention ponds"
        )

        recommendations.append(
            "Implement rainwater harvesting systems in public buildings"
        )

    elif water < 2:

        recommendations.append(
            "Improve groundwater recharge through recharge pits and permeable surfaces"
        )

    # Built-up Recommendations
    if built_up > 80:

        recommendations.append(
            "Convert vacant plots into pocket parks and green spaces"
        )

    elif built_up > 60:

        recommendations.append(
            "Develop green corridors along major roads and transport routes"
        )

    recommendations.append(
        "Monitor land-cover changes annually using satellite imagery"
    )

    return recommendations