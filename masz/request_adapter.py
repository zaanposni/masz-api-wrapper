import time
from requests import Response

from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *

class MASZRequestAdapter:
    def __init__(self, url: str, token: str, api_version: int = 1, header: str = "Authorization", header_prefix: str = "Bearer ") -> None:
        self.request_handler = MASZRequestHandler(url, token, api_version, header, header_prefix)

    def __request(self, method: str, resource: str, params: dict = dict(), headers: dict = dict()) -> Response:
        try:
            if method == "GET":
                r = self.request_handler.get(resource, params, headers)
            if method == "GETSTATIC":
                r = self.request_handler.get_static(resource, params, headers)
            if method == "PUT":
                pass
            if method == "POST":
                pass
            if method == "DELETE":
                pass
            if r.status_code not in [200, 201]:
                console.verbose(f"[bright_red]{r.status_code}[bright_magenta] /{resource.lstrip('/')}")
            else:
                console.verbose(f"[bright_green]{r.status_code}[bright_magenta] /{resource.lstrip('/')}")
        except Exception as e:
            raise MASZRequestFailure("Request failed", e)
        if r.status_code == 401:
            raise MASZLoginFailure("Unauthorized", r.text)
        if r.status_code != 200:
            raise MASZRequestFailure(f"Invalid response code {r.status_code}", r.text)
        return r

    def get_current_user(self) -> AppUser:
        r = self.__request("GET", "/discord/users/@me")
        return AppUser(**r.json())


    def get_current_health(self) -> Status:
        start = time.perf_counter()
        r = self.__request("GET", "/health", dict(), {'Accept': 'application/json'})
        request_time = time.perf_counter() - start
        return Status(round(request_time*1000, 2) , **r.json())

    def get_version(self) -> Version:
        r = self.__request("GETSTATIC", "/static/version.json")
        return Version(**r.json())
