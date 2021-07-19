from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .masz_modcase import MASZModcaseAPI
from .masz_usernote import MASZUserNoteAPI
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
            r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}", {'deleteData': delete_data}, handle_status_code=False)
        except MASZBaseException as e:
            console.verbose(f"Failed to delete guild {e}")
            return False
        return r.status_code == 200

    def update(self, **fields) -> bool:
        for k, v in fields.items():
            setattr(self, k, v)
        try:
            data = {
                "modRoles": self.mod_roles,
                "adminRoles": self.admin_roles,
                "mutedRoles": self.muted_roles,
                "modNotificationDM": self.dm_notification,
                "modPublicNotificationWebhook": self.public_webhook,
                "modInternalNotificationWebhook": self.internal_webhook,
                "strictModPermissionCheck": self.strict_permission_check,
                "executeWhoisOnJoin": self.execute_whois_on_join
            }
            r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}", json_body=data, handle_status_code=False)
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
    
    def get_modcases(self, start_page=0) -> MASZModcaseAPI:
        r = self.request_handler.request("GET", f"/modcases/{self.guild_id}", {'startPage': start_page})
        return [MASZModcaseAPI(self.request_handler, x) for x in r.json()]

    def create_modcase(self, modCase: Modcase, send_notification: bool = True, handle_punishment: bool = True) -> MASZModcaseAPI:
        r = self.request_handler.request(
                "POST",
                f"/modcases/{self.guild_id}",
                json_body=modCase,
                params={"sendNotification": send_notification, "handlePunishment": handle_punishment}
            )
        return self.get_modcase(r.json()["caseid"])

    # UserNotes
    # =================================================================================================================

    def get_usernote(self, user_id: Union[str, int]) -> MASZUserNoteAPI:
        r = self.request_handler.request("GET", f"/guilds/{self.guild_id}/usernote/{user_id}")
        return MASZUserNoteAPI(self.request_handler, r.json())


