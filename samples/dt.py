import datetime

from marshmallow import Schema, fields, pre_load, post_load


class Response(Schema):
    time = fields.DateTime(required=True)


if __name__ == '__main__':

    time = datetime.datetime.utcnow()
    print(time)
    print(type(time))
    print(time.isoformat())
    print(type(time.isoformat()))

    request = {
        'time': time.isoformat()
    }
    print(request['time'])
    print(type(request['time']))

    response = Response().load(request)
    print(response)
