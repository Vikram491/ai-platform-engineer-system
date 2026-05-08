def calculate_confidence(
    validation_errors,
    runtime_report,
    assumptions
):

    score = 100

    # -----------------------------------
    # Penalize Validation Errors
    # -----------------------------------

    score -= len(validation_errors) * 15

    # -----------------------------------
    # Penalize Runtime Issues
    # -----------------------------------

    if not runtime_report["runtime_ready"]:

        score -= 30

    # -----------------------------------
    # Penalize Excessive Assumptions
    # -----------------------------------

    score -= len(assumptions) * 5

    # -----------------------------------
    # Clamp Score
    # -----------------------------------

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score