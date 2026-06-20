def get_plantation_strategy(
    tree_cover,
    built_up,
    water,
    cropland,
    trees_needed
):

    strategy = []

    if trees_needed == 0:
        return ["Current tree cover is sufficient"]

    # Dense urban area
    if built_up > 75:

        roadside = int(trees_needed * 0.50)
        pocket = int(trees_needed * 0.30)
        campus = int(trees_needed * 0.20)

        strategy.append(
            f"Roadside Plantation: {roadside} trees"
        )

        strategy.append(
            f"Pocket Parks: {pocket} trees"
        )

        strategy.append(
            f"Schools and Government Campuses: {campus} trees"
        )

    # Moderately urban area
    elif built_up > 50:

        urban_forest = int(trees_needed * 0.40)
        roadside = int(trees_needed * 0.30)
        parks = int(trees_needed * 0.30)

        strategy.append(
            f"Urban Forest: {urban_forest} trees"
        )

        strategy.append(
            f"Roadside Plantation: {roadside} trees"
        )

        strategy.append(
            f"Community Parks: {parks} trees"
        )

    # Semi-urban / peri-urban
    else:

        urban_forest = int(trees_needed * 0.50)
        biodiversity = int(trees_needed * 0.30)
        agroforestry = int(trees_needed * 0.20)

        strategy.append(
            f"Urban Forest: {urban_forest} trees"
        )

        strategy.append(
            f"Biodiversity Corridor: {biodiversity} trees"
        )

        strategy.append(
            f"Agroforestry Plantation: {agroforestry} trees"
        )

    # Water-based greening
    if water < 1:

        strategy.append(
            "Prioritize plantation around ponds, drains and water harvesting structures"
        )

    # Cropland-based greening
    if cropland > 30:

        strategy.append(
            "Promote agroforestry using Neem, Arjun and fruit-bearing trees along farm boundaries"
        )

    return strategy