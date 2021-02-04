from marshmallow import fields, Schema, post_load

from api.base import RequestDto
from helpers.password import generate_hash


class RequestCreateEmployeeDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    position = fields.Str(missing=None)
    department = fields.Str(missing=None)

    @post_load
    def hash_password(self, data: dict, **kwargs) -> dict:
        password = data['password']
        hashed_password = generate_hash(password)
        data['password'] = hashed_password

        return data


class RequestCreateEmployeeDto(RequestDto):
    __schema__ = RequestCreateEmployeeDtoSchema

