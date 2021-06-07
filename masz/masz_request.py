from requests import Response
import requests
from requests.exceptions import URLRequired

from .console import console
from .exceptions import *


class MASZRequestHandler:
    def __init__(self, url: str, token: str, api_version: int, header: str, header_prefix: str) -> None:
        self.url = url.rstrip('/')
        self.token = token
        self.api_version = api_version
        self.header = header
        self.header_prefix = header_prefix
        self.headers = {self.header: f"{self.header_prefix}{self.token}"}

    def request(self, method: str, resource: str, params: dict = dict(), headers: dict = dict()) -> Response:
        try:
            if method == "GET":
                r = self.__get(resource, params, headers)
            if method == "GETSTATIC":
                r = self.__get_static(resource, params, headers)
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
            raise MASZRequestFailure(f"Response code indicates {r.status_code}", r.text)
        return r

    def __get(self, resource: str, params: dict = dict(), headers: dict = dict()) -> Response:
        final_headers = {**headers, **self.headers}
        return requests.get(f"{self.url}/api/v{self.api_version}/{resource.lstrip('/')}", headers=final_headers, params=params)

    def __get_static(self, resource: str, params: dict = dict(), headers: dict = dict()) -> Response:
        final_headers = {**headers, **self.headers}
        return requests.get(f"{self.url}/{resource.lstrip('/')}", headers=final_headers, params=params)
    
    def __post(self, resource: str, body: dict, params: dict = dict(), headers: dict = dict()) -> Response:
        final_headers = {**headers, **self.headers}
        return requests.post(f"{self.url}/api/v{self.api_version}/{resource.lstrip('/')}", json=body, headers=final_headers, params=params)
    
    def __put(self, resource: str, body: dict, params: dict = dict(), headers: dict = dict()) -> Response:
        final_headers = {**headers, **self.headers}
        return requests.put(f"{self.url}/api/v{self.api_version}/{resource.lstrip('/')}", json=body, headers=final_headers, params=params)

    def __delete(self, resource: str, params: dict = dict(), headers: dict = dict()) -> Response:
        final_headers = {**headers, **self.headers}
        return requests.delete(f"{self.url}/api/v{self.api_version}/{resource.lstrip('/')}", headers=final_headers, params=params)
