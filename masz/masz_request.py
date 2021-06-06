from requests import Response
import requests
from requests.exceptions import URLRequired

class MASZRequestHandler:
    def __init__(self, url: str, token: str, api_version: int, header: str, header_prefix: str) -> None:
        self.url = url.rstrip('/')
        self.token = token
        self.api_version = api_version
        self.header = header
        self.header_prefix = header_prefix
        self.headers = {self.header: f"{self.header_prefix}{self.token}"}

    def get(self, resource: str, params: dict = dict(), headers: dict = dict()) -> Response:
        final_headers = {**headers, **self.headers}
        return requests.get(f"{self.url}/api/v{self.api_version}/{resource.lstrip('/')}", headers=final_headers, params=params)
