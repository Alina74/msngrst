from marshmallow import Schema, fields, ValidationError, EXCLUDE
from sanic.exceptions import SanicException


class ApiValidationException(SanicException):
    status = 400


class ApiResponseValidationException(SanicException):
    status = 500


class RequestCreateEmployeeDtoSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)


class RequestDto:
    __schema__: Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiValidationException(error.messages)
        except Exception:
            pass # write to log file if error that we dont know
        else:
            self._import(valid_data)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, field)

    def set(self, key, value):
        setattr(self, key, value)


class RequestCreateEmployeeDto(RequestDto):
    __schema__ = RequestCreateEmployeeDtoSchema


class ResponseGetEmployeeDtoSchema(Schema):
    eid = fields.Int(required=True, allow_none=False)


class ResponseDto:
    __schema__: Schema

    def __init__(self, obj: object):
        # properties = {}
        # for prop in dir(obj):
        #     if not prop.startswith('_') and not prop.endswith('_'):
        #         attr = getattr(obj, prop)
        #         if not callable(attr):
        #             valid_data['prop'] = attr
        #
        # self._data = valid_data
        properties = {
            prop: value
            for prop in dir(obj)
            if not prop.startswith('_')
               and not prop.endswith('_')
               and not callable(value := getattr(obj, prop))
        }

        try:
            self._data = self.__schema__(unknown=EXCLUDE).load(properties)
        except ValidationError as error:
            raise ApiResponseValidationException(error.messages)

    def dump(self) -> dict:
        return self._data


class ResponseGetEmployeeDto(ResponseDto, ResponseGetEmployeeDtoSchema):
    __schema__ = ResponseGetEmployeeDtoSchema


if __name__ == '__main__':
    # body = {'first_name': 'Andrew', 'last_name': 'Zakharov'}
    body = {'first_name': 'Andrew', 'last_name': 'Zakharov', 'second_name': 'Vladimirovich'}
    # body = {'first_name': 'Andrew',}

    # schema = RequestCreateEmployeeDtoSchema().load(body)
    # schema = RequestCreateEmployeeDtoSchema(unknown=EXCLUDE).load(body)

    # try:
    #     schema = RequestCreateEmployeeDtoSchema().load(body)
    # except ValidationError as error:
    #     print(error.messages)
    #     print(type(error.messages))
    # finally:
    #     pass

    # print(sc,")

    dto = RequestCreateEmployeeDto(data=body)
    dto.set('eid', 1)

    response = ResponseGetEmployeeDto(dto)

    # print(dto)
    print(dto.first_name)
    # print(response.eid)
    print(response.dump())





