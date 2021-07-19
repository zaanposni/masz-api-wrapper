from typing import List
from datetime import datetime

from masz.helpers import parse_dt_from_json
from .discord_user import DiscordUser
from ..exceptions import MASZInvalidResponse

class Motd:
    creator: DiscordUser

    def __init__(self, **kwargs) -> None:
        if "creator" in kwargs:  # may be null on PUT
            self.creator = DiscordUser(**kwargs["creator"])

        try:
            if "motd" in kwargs:
                motd = kwargs["motd"]
            elif "guildId" in kwargs:
                motd = kwargs
            else:
                raise KeyError("Invalid response")
        except KeyError as e:
            raise MASZInvalidResponse(e)
        
        self.id = motd.get("id")
        self.guild_id = motd.get("guildId")
        self.user_id = motd.get("userId")
        self.created_at = parse_dt_from_json(motd.get("createdAt"))
        self.message = motd.get("message")
        self.show_motd = motd.get("showMotd", False)

    def __str__(self) -> str:
        return f"{self.creator.username}#{self.creator.discriminator}: {self.message}" if self.show_motd else "Motd disabled"
