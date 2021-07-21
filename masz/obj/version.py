from platform import version


class Version:
    def __init__(self, **kwargs) -> None:
        self.masz_version = kwargs.get("version", '')
        self.wrapper_version = kwargs.get("wrapper_version", None)
        self.pre_release = bool(kwargs.get("pre_release"))

    def __str__(self) -> str:
        return f"API: {self.masz_version} | Wrapper: {self.wrapper_version}"
