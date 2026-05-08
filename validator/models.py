from pydantic import BaseModel
from typing import List, Dict


class Endpoint(BaseModel):
    path: str
    method: str
    request_fields: List[str]
    response_fields: List[str]


class APIModel(BaseModel):
    endpoints: List[Endpoint]


class UIPage(BaseModel):
    name: str
    components: List[str]
    api_calls: List[str]


class UIModel(BaseModel):
    pages: List[UIPage]


class AuthModel(BaseModel):
    roles: Dict[str, List[str]]


class FullSchema(BaseModel):
    db_schema: Dict[str, List[str]]
    api_schema: APIModel
    ui_schema: UIModel
    auth_schema: AuthModel