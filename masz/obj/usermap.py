from masz.helpers import parse_dt_from_json, parse_dt_to_json

class UserMap:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.guild_id = kwargs.get("guildId")
        self.user_a = kwargs.get("userA")
        self.user_b = kwargs.get("userB")
        self.reason = kwargs.get("reason")
        self.creator_id = kwargs.get("creatorUserId")
        self.createdAt = parse_dt_from_json(kwargs.get("createdAt"))

    def __str__(self) -> str:
        return f"{self.user_a} - {self.user_b}: {self.reason}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "guildId": self.guild_id,
            "userA": self.user_a,
            "userB": self.user_b,
            "reason": self.reason,
            "creatorUserId": self.creator_id,
            "createdAt": parse_dt_to_json(self.createdAt)
        }