from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZGuildAPI(GuildConfig):
    def __init__(self, request_handler: MASZRequestHandler, guild_id: Union[str, int]) -> None:
        self.request_handler = request_handler
        self.guild_id = guild_id
        r = self.request_handler.request("GET", f"/guilds/{guild_id}")
        super().__init__(**r.json())

    def delete(self, delete_data: bool = False) -> bool:
        try:
            r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}", {'deleteData': delete_data})
        except MASZBaseException as e:
            console.verbose(f"Failed to delete guild {e}")
            return False
        return r.status_code == 200
