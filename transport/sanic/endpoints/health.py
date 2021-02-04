from sanic.request import Request
from sanic.response import BaseHTTPResponse, text

from transport.sanic.base import SanicEndpoint


class HealthEndpoint(SanicEndpoint):
    async def method_get(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        # return text(body="<html>"
        #                  "<body><h1>Hello, " + request.args["name"][0] + "!</h1></body>"
        #                  "</html>", content_type="text/html; charset=utf-8")
        response = {
            'hello': 'world'
        }
        return await self.make_response_json(body=response, status=200)

    async def method_post(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(body=body, status=200)

    async def method_get_txt(self, request: Request, body: dict, *args, **kwargs):
        pass


# async def health_endpoint(request: Request) -> HTTPResponse:
#
#     response = {
#         'hello': 'world'
#     }
#
#     if 'POST' in request.method:
#         response.update(request.json)
#
#     return json(body=response, status=200)
