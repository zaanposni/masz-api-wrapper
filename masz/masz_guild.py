from typing import Union

from .console import console
from .masz_request import MASZRequestHandler
from .masz_modcase import MASZModcaseAPI
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
            r = self.request_handler.request("DELETE", f"/guilds/{self.guild_id}", {'deleteData': delete_data}, handle_status_code=False)
        except MASZBaseException as e:
            console.verbose(f"Failed to delete guild {e}")
            return False
        return r.status_code == 200

    def update(self, **fields) -> bool:
        try:
            data = {
                "modRoles": fields.get("mod_roles", self.mod_roles),
                "adminRoles": fields.get("admin_roles", self.admin_roles),
                "mutedRoles": fields.get("muted_roles", self.muted_roles),
                "modNotificationDM": fields.get("dm_notification", self.dm_notification),
                "modPublicNotificationWebhook": fields.get("public_webhook", self.public_webhook),
                "modInternalNotificationWebhook": fields.get("internal_webhook", self.internal_webhook),
                "strictModPermissionCheck": fields.get("strict_permission_check", self.strict_permission_check),
                "executeWhoisOnJoin": fields.get("execute_whois_on_join", self.execute_whois_on_join)
            }
            r = self.request_handler.request("PUT", f"/guilds/{self.guild_id}", json_body=data, handle_status_code=False)
        except MASZBaseException as e:
            console.verbose(f"Failed to update guild {e}")
            return False
        return r.status_code == 200

    def get_modcase(self, case_id: Union[str, int]) -> MASZModcaseAPI:
        return MASZModcaseAPI(self.request_handler, self.guild_id, case_id)

    def create_modcase(self, modCase: Modcase, send_notification: bool = True, handle_punishment: bool = True) -> MASZModcaseAPI:
        r = self.request_handler.request(
                "POST",
                f"/modcases/{self.guild_id}",
                json_body=modCase,
                params={"sendNotification": send_notification, "handlePunishment": handle_punishment}
            )
        return self.get_modcase(r.json()["caseid"])
