import dateparser

class Status:
    def __init__(self, response_time: int, **kwargs) -> None:
        self.status = kwargs.get("status", '')
        self.name = kwargs.get("name")
        self.server_time = dateparser.parse(kwargs.get("server_time"))
        self.server_time_utc = dateparser.parse(kwargs.get("server_time_utc"))
        self.response_time = response_time

    def __str__(self) -> str:
        return f"{self.status.upper()} ({self.response_time}ms)"
