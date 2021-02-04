# from http import HTTPStatus
# from sanic.request import Request
# from sanic.response import BaseHTTPResponse, json
#
# from configs.config import ApplicationConfig
#
#
# class SanicEndpoint:
#
#     async def __call__(self, *args, **kwargs) -> BaseHTTPResponse:
#         return await self.handler(*args, **kwargs)
#
#     def __init__(self, config: ApplicationConfig, uri: str, methods: list, *args, **kwargs):
#         self.config = config
#         self.uri = uri
#         self.methods = methods
#         self.__name__ = self.__class__.__name__
#
#
# config = ApplicationConfig()
# SanicConfig(config)
# cl = SanicEndpoint(config)
# print(cl.__name__)
# print(SanicEndpoint.__name__)
# print(SanicEndpoint.__class__.__name__)