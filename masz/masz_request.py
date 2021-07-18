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

    def request(self, method: str, resource: str, params: dict = dict(), headers: dict = dict(), handle_status_code: bool = True, json_body: dict = dict()) -> Response:
        try:
            if method == "GET":
                r = self.__get(resource, params, headers)
            if method == "GETSTATIC":
                r = self.__get_static(resource, params, headers)
            if method == "PUT":
                r = self.__put(resource, json_body, params, headers)
            if method == "POST":
                r = self.__post(resource, json_body, params, headers)
            if method == "DELETE":
                r = self.__delete(resource, params, headers)
            if r.status_code not in [200, 201]:
                console.verbose(f"[bright_red]{r.status_code}[/bright_red] [bright_cyan]{r.request.method}[/bright_cyan] [bright_magenta] /{resource.lstrip('/')}[/bright_magenta]")
            else:
                console.verbose(f"[bright_green]{r.status_code}[/bright_green][bright_magenta] [bright_cyan]{r.request.method}[/bright_cyan] /{resource.lstrip('/')}[/bright_magenta]")
        except Exception as e:
            raise MASZRequestFailure("Request failed", e)
        if r.status_code == 401 and handle_status_code:
            console.verbose(f"[bright_red]{r.status_code}[/bright_red][bright_magenta] {r.text}[/bright_magenta]")
            raise MASZLoginFailure("Unauthorized", r.text)
        if r.status_code not in [200, 201] and handle_status_code:
            console.verbose(f"[bright_red]{r.status_code}[/bright_red][bright_magenta] {r.text}[/bright_magenta]")
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
