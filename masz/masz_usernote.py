from masz.obj.modcase import Modcase
from typing import Union

from masz.helpers import parse_dt_to_json
from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZUserNoteAPI(UserNote):
    def __init__(self, request_handler: MASZRequestHandler, data: dict) -> None:
        self.request_handler = request_handler
        super().__init__(**data)

    def delete(self) -> bool:
        try:
            r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}/usernote/{self.id}")
        except MASZBaseException as e:
            console.verbose(f"Failed to delete usernote {e}")
            return False
        return r.status_code == 200

    def update(self, handle_punishment: bool = True, send_notification: bool = True, announce_dm: bool = True, **fields) -> bool:
        for k, v in fields.items():
            setattr(self, k, v)
        try:
            data = {
                "description": self.description,
                "userid": self.user_id
            }
            r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/usernote",
                                                json_body=data)
        except MASZBaseException as e:
            console.verbose(f"Failed to update usernote {e}")
            return False
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200
