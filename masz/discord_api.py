from typing import Union, List

from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZDiscordAPI:
    def __init__(self, request_handler: MASZRequestHandler) -> None:
        self.request_handler = request_handler
    
    def get_current_user(self) -> AppUser:
        r = self.request_handler.request("GET", "/discord/users/@me")
        return AppUser(**r.json())

    def get_user(self, id: Union[str, int]) -> DiscordUser:
        r = self.request_handler.request("GET", f"/discord/users/{id}")
        return DiscordUser(**r.json())
    
    def get_guild(self, id: Union[str, int]) -> DiscordGuild:
        r = self.request_handler.request("GET", f"/discord/guilds/{id}")
        return DiscordGuild(**r.json())
    
    def get_guildchannels(self, id: Union[str, int]) -> List[DiscordChannel]:
        r = self.request_handler.request("GET", f"/discord/guilds/{id}/channels")
        return [DiscordChannel(**x) for x in r.json()]
    
    def get_guildmembers(self, id: Union[str, int]) -> List[DiscordMember]:
        r = self.request_handler.request("GET", f"/discord/guilds/{id}/members", {'partial': False})
        return [DiscordMember(**x) for x in r.json()]

    def get_partialguildmembers(self, id: Union[str, int]) -> List[DiscordUser]:
        r = self.request_handler.request("GET", f"/discord/guilds/{id}/members", {'partial': True})
        return [DiscordUser(**x) for x in r.json()]
