from masz.obj.modcase import Modcase
from typing import Union

from masz.helpers import parse_dt_to_json
from .console import console
from .masz_request import MASZRequestHandler
from .exceptions import *
from .obj import *


class MASZModcaseAPI(Modcase):
    def __init__(self, request_handler: MASZRequestHandler, data: dict) -> None:
        self.request_handler = request_handler
        super().__init__(**data)

    def delete(self, send_notification: bool = True, force_delete: bool = False) -> bool:
        try:
            r = self.request_handler.request("DELETE", f"/modcases/{self.guild_id}/{self.case_id}", {'sendNotification': send_notification, 'forceDelete': force_delete})
        except MASZBaseException as e:
            console.verbose(f"Failed to delete modcase {e}")
            return False
        return r.status_code == 200

    def update(self, handle_punishment: bool = True, send_notification: bool = True, announce_dm: bool = True, **fields) -> bool:
        for k, v in fields.items():
            setattr(self, k, v)
        try:
            r = self.request_handler.request("PUT", f"/modcases/{self.guild_id}/{self.case_id}",
                                                params={'sendNotification': send_notification, 'handlePunishment': handle_punishment, 'announceDm': announce_dm},
                                                json_body=self.to_dict())
        except MASZBaseException as e:
            console.verbose(f"Failed to update modcase {e}")
            return False
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    def post_comment(self, msg: Union[Comment, str]) -> bool:
        data = {
            "message": msg
        }
        if isinstance(msg, Comment):
            data = msg.to_dict()
        try:
            r = self.request_handler.request("POST", f"/modcases/{self.guild_id}/{self.case_id}/comments", json_body=data)
        except MASZBaseException as e:
            console.verbose(f"Failed to post comment {e}")
            return False

        if r.status_code == 201:  # refresh comments
            refresh = self.request_handler.request("GET", f"/modcases/{self.guild_id}/{self.case_id}")
            super().__init__(**refresh.json())

        return r.status_code == 201

    def delete_comment(self, comment: Union[Comment, str, int]) -> bool:
        comment_id = comment
        if isinstance(comment, Comment):
            comment_id = comment.id
        try:
            r = self.request_handler.request("DELETE", f"/modcases/{self.guild_id}/{self.case_id}/comments/{comment_id}")
        except MASZBaseException as e:
            console.verbose(f"Failed to delete comment {e}")
            return False
        if r.status_code == 200:
            self.comments = [x for x in self.comments if str(x.id)!=str(comment_id)]
        return r.status_code == 200

    def lock_comments(self) -> bool:
        r = self.request_handler.request("POST", f"/modcases/{self.guild_id}/{self.case_id}/lock")
        return r.status_code == 200

    def unlock_comments(self) -> bool:
        r = self.request_handler.request("DELETE", f"/modcases/{self.guild_id}/{self.case_id}/lock")
        return r.status_code == 200
    
    def restore(self) -> bool:
        r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}/bin/{self.case_id}/restore")
        return r.status_code == 200

    def delete_from_bin(self) -> bool:
        r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}/bin/{self.case_id}/delete")
        return r.status_code == 200
