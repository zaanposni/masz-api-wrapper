class DiscordRole:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.color = kwargs.get("color")
        self.position = kwargs.get("position")
        self.permissions = kwargs.get("permissions")

    def __str__(self) -> str:
        return self.name
