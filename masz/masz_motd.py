from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZMotdAPI(Motd):
    def __init__(self, request_handler: MASZRequestHandler, guild_id: Union[str, int]) -> None:
        self.request_handler = request_handler
        self.guild_id = guild_id
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/motd", handle_status_code=False)
        if r.status_code == 200:
            super().__init__(**r.json())

    def delete(self) -> bool:
        self.show_motd = False
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=self.to_dict())
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def set(self, msg: str) -> bool:
        self.message = msg
        self.show_motd = True
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=self.to_dict())
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def activate(self) -> bool:
        self.show_motd = True
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=self.to_dict())
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def toggle(self) -> bool:
        self.show_motd = not self.show_motd
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/motd", json_body=self.to_dict())
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200
