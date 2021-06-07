class DiscordChannel:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.type = kwargs.get("type")

    def __str__(self) -> str:
        return self.name
