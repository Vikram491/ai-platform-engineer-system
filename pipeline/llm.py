import json


# -----------------------------------
# MOCK MODE GENERATION
# -----------------------------------

def generate_json(system_prompt, user_prompt):

    # -----------------------------------
    # INTENT STAGE
    # -----------------------------------

    if "extracts structured software requirements" in system_prompt:

        return {
            "app_name": "CRM Platform",

            "features": [
                "login",
                "contacts",
                "dashboard",
                "payments"
            ],

            "roles": [
                "admin",
                "user"
            ]
        }

    # -----------------------------------
    # DESIGN STAGE
    # -----------------------------------

    elif "software architect" in system_prompt:

        return {

            "architecture": "microservices",

            "services": [
                "auth-service",
                "dashboard-service",
                "payment-service"
            ]
        }

    # -----------------------------------
    # SCHEMA STAGE
    # -----------------------------------

    elif "platform compiler" in system_prompt:

        return {

            "db_schema": {

                "users": [
                    "id",
                    "email",
                    "password"
                ],

                "contacts": [
                    "id",
                    "name",
                    "phone"
                ]
            },

            "api_schema": {

                "endpoints": [

                    {
                        "path": "/login",

                        "method": "POST",

                        "request_fields": [
                            "email",
                            "password"
                        ],

                        "response_fields": [
                            "token"
                        ]
                    }
                ]
            },

            "ui_schema": {

                "pages": [

                    {
                        "name": "Dashboard",

                        "components": [
                            "Navbar",
                            "Sidebar"
                        ],

                        "api_calls": [
                            "/login"
                        ]
                    }
                ]
            },

            "auth_schema": {

                "roles": {

                    "admin": [
                        "all"
                    ],

                    "user": [
                        "read"
                    ]
                }
            }
        }

    # -----------------------------------
    # REPAIR STAGE
    # -----------------------------------

    else:

        return {
            "repair": "completed"
        }