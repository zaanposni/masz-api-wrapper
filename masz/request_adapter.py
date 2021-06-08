import time
from typing import Union

from .masz_guild import MASZGuildAPI
from .masz_request import MASZRequestHandler
from .discord_api import MASZDiscordAPI
from .exceptions import *
from .obj import *


class MASZRequestAdapter:
    def __init__(self, url: str, token: str, api_version: int = 1, header: str = "Authorization", header_prefix: str = "Bearer ") -> None:
        self.request_handler = MASZRequestHandler(url, token, api_version, header, header_prefix)
        self.discord = MASZDiscordAPI(self.request_handler)

    def get_current_user(self) -> AppUser:
        return self.discord.get_current_user()

    def get_current_health(self) -> Status:
        start = time.perf_counter()
        r = self.request_handler.request("GET", "/health", dict(), {'Accept': 'application/json'})
        request_time = time.perf_counter() - start
        return Status(round(request_time*1000, 2) , **r.json())

    def get_version(self) -> Version:
        r = self.request_handler.request("GETSTATIC", "/static/version.json")
        return Version(**r.json())

    def get_adminstats(self) -> Adminstats:
        r = self.request_handler.request("GET", "/meta/adminstats")
        return Adminstats(**r.json())

    def get_guild(self, guild_id: Union[str, int]) -> MASZGuildAPI:
        return MASZGuildAPI(self.request_handler, guild_id)
