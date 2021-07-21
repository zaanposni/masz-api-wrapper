from masz.helpers import parse_dt_from_json, parse_dt_to_json

class UserNote:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.guild_id = kwargs.get("guildId")
        self.user_id = kwargs.get("userId")
        self.description = kwargs.get("description")
        self.creator_id = kwargs.get("creatorId")
        self.updated_at = parse_dt_from_json(kwargs.get("updatedAt"))

    def __str__(self) -> str:
        return f"{self.user_id}: {self.description}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "guildId": self.guild_id,
            "userId": self.user_a,
            "description": self.description,
            "creatorId": self.creator_id,
            "updatedAt": parse_dt_to_json(self.createdAt)
        }
