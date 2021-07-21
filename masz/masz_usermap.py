from masz.obj.modcase import Modcase
from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZUserMapAPI(UserMap):
    def __init__(self, request_handler: MASZRequestHandler, data: dict) -> None:
        self.request_handler = request_handler
        super().__init__(**data)

    def delete(self) -> bool:
        try:
            r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}/usermap/{self.id}")
        except MASZBaseException as e:
            console.verbose(f"Failed to delete usermap {e}")
            return False
        return r.status_code == 200

    def update(self, **fields) -> bool:
        for k, v in fields.items():
            setattr(self, k, v)
        try:
            r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/usermap",
                                                json_body=self.to_dict())
        except MASZBaseException as e:
            console.verbose(f"Failed to update usermap {e}")
            return False
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200
