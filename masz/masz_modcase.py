from masz.obj.modcase import Modcase
from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZModcaseAPI(Modcase):
    def __init__(self, request_handler: MASZRequestHandler, guild_id: Union[str, int], case_id: Union[str, int]) -> None:
        self.request_handler = request_handler
        self.guild_id = guild_id
        self.case_id = case_id
        r = self.request_handler.request("GET", f"/modcases/{guild_id}/{case_id}")
        super().__init__(**r.json())

    def delete(self, send_notification: bool = True, force_delete: bool = False) -> bool:
        try:
            r = self.request_handler.request("DELETE", f"/modcases/{self.guild_id}/{self.case_id}", {'sendNotification': send_notification, 'forceDelete': force_delete}, handle_status_code=False)
        except MASZBaseException as e:
            console.verbose(f"Failed to delete modcase {e}")
            return False
        return r.status_code == 200

    def update(self, **fields) -> bool:
        pass

    def post_comment(self, msg: str) -> bool:
        data = {
            "message": msg
        }
        try:
            r = self.request_handler.request("POST", f"/modcases/{self.guild_id}/{self.case_id}/comments", handle_status_code=False, json_body=data)
        except MASZBaseException as e:
            console.verbose(f"Failed to post comment {e}")
            return False

        if r.status_code == 201:  # refresh comments
            refresh = self.request_handler.request("GET", f"/modcases/{self.guild_id}/{self.case_id}")
            super().__init__(**refresh.json())

        return r.status_code == 201
