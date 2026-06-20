def calculate_sustainability_score(
    tree_cover,
    built_up,
    water,
    grass,
    shrub,
    cropland
):

    score = (
        tree_cover * 2.5
        + water * 3
        + grass * 1.5
        + cropland * 1
        + shrub * 1
        - built_up * 0.5
    )

    score = max(0, min(100, round(score)))

    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    elif score >= 20:
        grade = "D"
    else:
        grade = "F"

    return {
        "score": score,
        "grade": grade
    }