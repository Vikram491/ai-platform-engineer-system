def analyze_cost_latency(latency):

    if latency < 2:

        quality = "High"
        cost = "Medium"

    elif latency < 5:

        quality = "Very High"
        cost = "High"

    else:

        quality = "Maximum"
        cost = "Very High"

    return {
        "estimated_quality": quality,
        "estimated_cost": cost,
        "latency_seconds": round(latency, 2)
    }