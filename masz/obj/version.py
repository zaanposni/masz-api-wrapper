from platform import version


class Version:
    def __init__(self, **kwargs) -> None:
        self.masz_version = kwargs.get("version", '')
        self.pre_release = bool(kwargs.get("pre_release"))

    def __str__(self) -> str:
        return self.masz_version
