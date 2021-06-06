class DiscordUser:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.username = kwargs.get("username")
        self.discriminator = kwargs.get("discriminator")
        self.avatar = kwargs.get("avatar")
        self.bot = kwargs.get("bot", False)
        self.image_url = kwargs.get("imageUrl", "https://cdn.discordapp.com/embed/avatars/0.png")

    def __str__(self) -> str:
        return f"{self.username}#{self.discriminator}"
