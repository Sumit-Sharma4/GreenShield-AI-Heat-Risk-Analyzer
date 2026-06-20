def calculate_trees_needed(
    tree_cover,
    built_up,
    target_tree_cover=15,
    area_km2=3.14
):

    if tree_cover >= target_tree_cover:
        return 0

    deficit = target_tree_cover - tree_cover

    factor = 150

    if built_up > 80:
        factor = 180
    elif built_up > 60:
        factor = 165

    trees_needed = deficit * area_km2 * factor

    return int(trees_needed)