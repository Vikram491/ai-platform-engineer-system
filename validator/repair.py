def repair(data: dict, errors: list):

    print("Repairing Errors:", errors)

    if "api_schema" not in data:
        data["api_schema"] = {
            "endpoints": []
        }

    return data