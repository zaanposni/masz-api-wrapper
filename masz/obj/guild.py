from .role import DiscordRole

class DiscordGuild:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.icon = kwargs.get("icon")
        self.roles = []
        for role in kwargs.get("roles", []):
            self.roles.append(DiscordRole(**role))
        self.image_url = f"https://cdn.discordapp.com/icons/{self.id}/{self.icon}.png" if self.icon else None

    def __str__(self) -> str:
        return self.name
