from masz.helpers import parse_dt_from_json

class Comment:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.message = kwargs.get("message")
        self.user_id = kwargs.get("userId")
        self.created_at = parse_dt_from_json(kwargs.get("createdAt"))

    def __str__(self) -> str:
        return self.message
