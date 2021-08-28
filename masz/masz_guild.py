from typing import Union, List

from .console import console
from .masz_request import MASZRequestHandler
from .masz_modcase import MASZModcaseAPI
from .masz_usernote import MASZUserNoteAPI
from .masz_usermap import MASZUserMapAPI
from .masz_motd import MASZMotdAPI
from .exceptions import *
from .obj import *


class MASZGuildAPI(GuildConfig):
    motd: MASZMotdAPI = None
    def __init__(self, request_handler: MASZRequestHandler, guild_id: Union[str, int]) -> None:
        self.request_handler = request_handler
        self.guild_id = guild_id
        r = self.request_handler.request("GET", f"/guilds/{guild_id}")
        super().__init__(**r.json())
        self.motd = MASZMotdAPI(request_handler, guild_id)

    def delete(self, delete_data: bool = False) -> bool:
        try:
            r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}", {'deleteData': delete_data})
        except MASZBaseException as e:
            console.verbose(f"Failed to delete guild {e}")
            return False
        return r.status_code == 200

    def update(self, **fields) -> bool:
        for k, v in fields.items():
            setattr(self, k, v)
        try:
            r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}", json_body=self.to_dict())
        except MASZBaseException as e:
            console.verbose(f"Failed to update guild {e}")
            return False
        if r.status_code == 200:
            super().__init__(**r.json())
        return r.status_code == 200

    # Modcases
    # =================================================================================================================

    def get_modcase(self, case_id: Union[str, int]) -> MASZModcaseAPI:
        r = self.request_handler.request("GET", f"/modcases/{self.guild_id}/{case_id}")
        return MASZModcaseAPI(self.request_handler, r.json())

    def get_modcases_paginated(self, start_page=0) -> List[MASZModcaseAPI]:
        r = self.request_handler.request("GET", f"/modcases/{self.guild_id}", params={'startPage': start_page})
        return [MASZModcaseAPI(self.request_handler, x) for x in r.json()]

    def get_modcases(self) -> List[MASZModcaseAPI]:
        count = 0
        all_cases = []
        while True:
            new_cases = self.get_modcases_paginated(count)
            count += 1
            all_cases += new_cases
            if not len(new_cases):
                break
        return all_cases

    def create_modcase(self, modcase: Modcase, send_notification: bool = True, handle_punishment: bool = True, announce_dm: bool = True) -> MASZModcaseAPI:
        r = self.request_handler.request(
                "POST",
                f"/modcases/{self.guild_id}",
                json_body=modcase.to_dict(),
                params={"sendNotification": send_notification, "handlePunishment": handle_punishment, "announceDm": announce_dm}
            )
        return MASZModcaseAPI(self.request_handler, r.json())

    def delete_modcase(self, case_id: Union[str, int], send_notification: bool = True, force_delete: bool = False) -> bool:
        r = self.request_handler.request("DELETE", f"/modcases/{self.guild_id}/{case_id}",
                                            params={'sendNotification': send_notification, 'forceDelete': force_delete})
        return r.status_code == 200

    # UserNotes
    # =================================================================================================================

    def get_usernote(self, user_id: Union[str, int]) -> MASZUserNoteAPI:
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/usernote/{user_id}")
        return MASZUserNoteAPI(self.request_handler, r.json())

    def get_usernotes(self) -> List[MASZUserNoteAPI]:
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/usernote")
        return [MASZUserNoteAPI(self.request_handler, x) for x in r.json()]

    def create_usernote(self, usernote: UserNote) -> MASZUserNoteAPI:
        r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}/usernote", json_body=usernote.to_dict())
        return MASZUserNoteAPI(self.request_handler, r.json())

    def delete_usernote(self, user_id: Union[str, int]) -> bool:
        r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}/usernote/{user_id}")
        return r.status_code == 200

    # UserMap
    # =================================================================================================================

    def get_usermaps_by_user(self, user_id: Union[str, int]) -> List[MASZUserMapAPI]:
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/usermap/{user_id}")
        return [MASZUserMapAPI(self.request_handler, x) for x in r.json()]

    def get_usermaps(self) -> List[MASZUserMapAPI]:
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/usermap")
        return [MASZUserMapAPI(self.request_handler, x) for x in r.json()]

    def create_usermap(self, usermap: UserMap) -> MASZUserMapAPI:
        usermap.guild_id = self.guild_id
        r = self.request_handler.request("POST", f"/guilds/{self.guild_id}/usermap", json_body=usermap.to_dict())
        console.log(r.json())
        return MASZUserMapAPI(self.request_handler, r.json())

    def delete_usermap(self, map_id: Union[str, int]) -> bool:
        r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}/usernote/{map_id}")
        return r.status_code == 200
