import dateparser

class Comment:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.message = kwargs.get("message")
        self.user_id = kwargs.get("userId")
        self.created_at = dateparser.parse(kwargs.get("createdAt"))

    def __str__(self) -> str:
        return self.message
