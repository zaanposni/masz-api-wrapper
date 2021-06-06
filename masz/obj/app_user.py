from .discord_user import DiscordUser

class AppUser:
    def __init__(self, **kwargs) -> None:
        self.discord_user = DiscordUser(**kwargs.get("discordUser"))
        self.is_siteadmin = bool(kwargs.get("isAdmin"))

    def __str__(self) -> str:
        if self.is_siteadmin:
            return f"{self.discord_user.username}#{self.discord_user.discriminator} (siteadmin)"
        return f"{self.discord_user.username}#{self.discord_user.discriminator}"
