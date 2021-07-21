from masz.helpers import parse_dt_from_json, parse_dt_to_json

class Comment:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.message = kwargs.get("message")
        self.user_id = kwargs.get("userId")
        self.created_at = parse_dt_from_json(kwargs.get("createdAt"))

    def __str__(self) -> str:
        return self.message

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "message": self.message,
            "userId": self.user_id,
            "createdAt": parse_dt_to_json(self.created_at)
        }
