def calculate_cooling_potential(trees_needed):

    # Approximate cooling effect:
    # 10,000 trees ≈ 0.1 °C reduction

    cooling = round(
        (trees_needed / 10000) * 0.1,
        2
    )

    return f"≈ {cooling} °C reduction"