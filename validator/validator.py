from validator.models import FullSchema


def cross_validate(data):

    errors = []

    db_schema = data["db_schema"]
    api_schema = data["api_schema"]["endpoints"]
    ui_schema = data["ui_schema"]["pages"]

    # -----------------------------------
    # API ↔ DB Validation
    # -----------------------------------

    db_fields = []

    for table_fields in db_schema.values():
        db_fields.extend(table_fields)

    for endpoint in api_schema:

        for field in endpoint["request_fields"]:

            if field not in db_fields:

                errors.append(
                    f"API request field '{field}' missing in DB schema"
                )

    # -----------------------------------
    # UI ↔ API Validation
    # -----------------------------------

    api_paths = []

    for endpoint in api_schema:
        api_paths.append(endpoint["path"])

    for page in ui_schema:

        for call in page["api_calls"]:

            if call not in api_paths:

                errors.append(
                    f"UI calls missing API endpoint '{call}'"
                )

    return errors


def validate_all(data):

    errors = []

    try:

        FullSchema(**data)

    except Exception as e:

        errors.append(str(e))

    cross_errors = cross_validate(data)

    errors.extend(cross_errors)

    return len(errors) == 0, errors