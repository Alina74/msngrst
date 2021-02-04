from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json


app = Sanic(__name__)


def decorator(application: Sanic, uri, methods):
    def wrapper(handler):
        application.add_route(
            handler=handler,
            uri=uri,
            methods=methods
        )
        return handler
    return wrapper


@decorator(application=app, uri='/', methods=['POST', 'GET'])
async def health_endpoint(request: Request) -> HTTPResponse:

    response = {
        'hello': 'world',
        # 'params': request.query_args,
        # 'smth': request.body
    }

    if 'POST' in request.method:
        response.update(request.json)

    return json(body=response, status=200)


# dec = decorator(application=app, uri='/', methods=['POST', 'GET'])
# dec(health_endpoint)


app.run(
    host='localhost',
    port='8000',
)
