def generate_assumptions(intent: dict):

    assumptions = []

    # -----------------------------------
    # Missing Auth
    # -----------------------------------

    features = intent.get("features", [])

    if "login" not in features:

        assumptions.append(
            "Assuming email/password authentication"
        )

    # -----------------------------------
    # Missing API Style
    # -----------------------------------

    assumptions.append(
        "Assuming REST API architecture"
    )

    # -----------------------------------
    # Missing Database
    # -----------------------------------

    assumptions.append(
        "Assuming relational database design"
    )

    # -----------------------------------
    # Missing Roles
    # -----------------------------------

    roles = intent.get("roles", [])

    if len(roles) == 0:

        assumptions.append(
            "Assuming default user/admin roles"
        )

    return assumptions