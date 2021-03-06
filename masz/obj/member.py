from masz.helpers import parse_dt_from_json

from .discord_user import DiscordUser

class DiscordMember:
    def __init__(self, **kwargs) -> None:
        self.user = DiscordUser(**kwargs.get("user"))
        self.nick = kwargs.get("nick")
        self.roles = kwargs.get("roles", [])
        self.joined_at = parse_dt_from_json(kwargs.get("type"))

    def __str__(self) -> str:
        return self.nick if self.nick else f"{self.user.username}#{self.user.discriminator}"
