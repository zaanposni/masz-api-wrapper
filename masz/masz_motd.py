from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZMotdAPI(Motd):
    def __init__(self, request_handler: MASZRequestHandler, guild_id: Union[str, int]) -> None:
        self.request_handler = request_handler
        self.guild_id = guild_id
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/motd")
        super().__init__(**r.json())        

    def delete(self) -> bool:
        data = {
            "message": self.message,
            "showMotd": False
        }
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=data)
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def set(self, msg: str) -> bool:
        data = {
            "message": msg,
            "showMotd": True
        }
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=data)
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def activate(self) -> bool:
        data = {
            "message": self.message,
            "showMotd": True
        }
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=data)
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def toggle(self) -> bool:
        data = {
            "message": self.message,
            "showMotd": not self.show_motd
        }
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=data)
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200
