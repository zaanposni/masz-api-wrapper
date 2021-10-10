from .console import console, MASZLogLevel
from .request_adapter import MASZRequestAdapter
from .exceptions import MASZBaseException


SUPPORTED_API_VERSION = 3

class MASZClient(MASZRequestAdapter):
    def __init__(self, url: str, token: str, api_version: int = 1, log_level: MASZLogLevel = MASZLogLevel.INFO) -> None:
        super().__init__(url, token, api_version)
        self._url = url
        self._token = token
        self._api_version = api_version
        console.log_level = log_level

        try:
            with console.info_status(f"[bold green]Connecting to MASZ at {url} ...") as status:
                self.server_health = self.get_current_health()
                if self.server_health.status.lower() == 'ok':
                    if self.server_health.response_time < 200:
                        console.info(f":white_check_mark: Ping [bright_green]'{self.server_health.status.upper()}' {self.server_health.response_time}[/bright_green] ms.")
                    else:
                        console.info(f":white_check_mark: Ping [bright_green]'{self.server_health.status.upper()}'[/bright_green][bright_yellow] {self.server_health.response_time}[/bright_yellow] ms.")
                else:
                    console.info(f":white_check_mark: Ping [bright_red]'{self.server_health.status.upper()}' {self.server_health.response_time}[/bright_red] ms.")

        except MASZBaseException as e:
            console.critical(f":exclamation: [red]MASZ API at {url} seems to be unhealthy or unreachable.")
            exit(1)

        try:
            with console.info_status(f"[bold green]Checking API version...") as status:
                self.server_version = self.get_version()
                if self.server_version.wrapper_version is None:
                    console.critical(f":exclamation: This API [red]may not be compatible[/red]. You need to use MASZ v1.12.1 or newer!")
                else:
                    if SUPPORTED_API_VERSION >= self.server_version.wrapper_version:
                        console.info(f":white_check_mark: API version {self.server_version.wrapper_version} is [bright_green]compatible[/bright_green].")
                    else:
                        console.critical(f":exclamation: API version {self.server_version.wrapper_version} [red]may not be compatible[/red]. This package only supports versions until {SUPPORTED_API_VERSION}. Try to upgrade this python package.")

        except MASZBaseException as e:
            console.critical(f":exclamation: [red]Failed to fetch API version.")

        try:
            with console.info_status(f"[bold bright_green]Logging in...") as status:
                self.me = self.get_current_user()
                console.info(f":white_check_mark: [bright_green]Logged in[/bright_green] to MASZ at {url} as [bright_blue]{self.me}[/bright_blue].")

        except MASZBaseException as e:
            console.critical(f":exclamation: [red]Failed to login.")
            exit(1)

    def __str__(self) -> str:
        return f"MASZ at {self._url} | {self.server_health}\n{self.server_version}"
