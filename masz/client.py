from requests import Response

from .console import console, MASZLogLevel
from .request_adapter import MASZRequestAdapter
from .exceptions import MASZBaseException, MASZLoginFailure
from .obj import DiscordUser



class MASZClient:
    def __init__(self, url: str, token: str, api_version: int = 1, log_level: MASZLogLevel = MASZLogLevel.INFO) -> None:
        self.url = url
        self.token = token
        self.api_version = api_version
        self.request_adapter = MASZRequestAdapter(self.url, self.token, self.api_version)
        console.log_level = log_level

        try:
            with console.info_status(f"[bold green]Connecting to MASZ at {url} ...") as status:
                service_health = self.request_adapter.get_current_health()
                if service_health.status.lower() == 'ok':
                    if service_health.response_time < 200:
                        console.info(f":white_check_mark: Ping [bright_green]'{service_health.status.upper()}' {service_health.response_time}[/bright_green] ms.")
                    else:
                        console.info(f":white_check_mark: Ping [bright_green]'{service_health.status.upper()}'[/bright_green][bright_yellow] {service_health.response_time}[/bright_yellow] ms.")
                else:
                    console.info(f":white_check_mark: Ping [bright_red]'{service_health.status.upper()}' {service_health.response_time}[/bright_red] ms.")

        except MASZBaseException as e:
            console.critical(f":exclamation: [red]MASZ API at {url} seems to be unhealthy or unreachable.")
            exit(1)
        
        try:
            with console.info_status(f"[bold bright_green]Logging in...") as status:
                self.me = self.request_adapter.get_current_user()
                console.info(f":white_check_mark: [bright_green]Logged in[/bright_green] to MASZ at {self.url} as [bright_blue]{self.me}[/bright_blue].")

        except MASZBaseException as e:
            console.critical(f":exclamation: [red]Failed to login.")
            exit(1)
