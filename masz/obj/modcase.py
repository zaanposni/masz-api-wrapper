from typing import List
from datetime import datetime

from masz.helpers import parse_dt_from_json, parse_dt_to_json, parse_enum_to_json
from .punishment_type import PunishmentType
from .creation_type import CreationType
from .comment import Comment

class Modcase:
    comments: List[Comment]

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.case_id = kwargs.get("caseId")
        self.guild_id = kwargs.get("guildId")
        self.title = kwargs.get("title")
        self.description = kwargs.get("description")
        self.user_id = kwargs.get("userId")
        self.username = kwargs.get("username")
        self.discriminator = kwargs.get("discriminator")
        self.nickname = kwargs.get("nickname")
        self.mod_id = kwargs.get("modId")
        self.created_at = parse_dt_from_json(kwargs.get("createdAt"))
        self.occured_at = parse_dt_from_json(kwargs.get("occuredAt"))
        self.last_edited_at = parse_dt_from_json(kwargs.get("lastEditedAt"))
        self.last_edited_by_mod_id = kwargs.get("lastEditedByModId")
        self.punishment = kwargs.get("punishment")
        self.labels = kwargs.get("labels", [])
        self.others = kwargs.get("others")
        self.valid = kwargs.get("valid", False)
        self.creation_type = kwargs.get("creationType", CreationType.DEFAULT)
        self.punishment_type = kwargs.get("punishmentType", PunishmentType.NONE)
        self.punished_until = parse_dt_from_json(kwargs.get("punishedUntil"))
        self.punishment_active = kwargs.get("punishmentActive", False)
        self.allow_comments = kwargs.get("allowComments", False)
        self.locked_by_user_id = kwargs.get("lockedByUserId")
        self.locked_at = parse_dt_from_json(kwargs.get("lockedAt"))
        self.marked_to_delete_at = parse_dt_from_json(kwargs.get("markedToDeleteAt"))
        self.deleted_by_user_id = kwargs.get("deletedByUserId")
        if kwargs.get("comments", []):
            self.comments = [Comment(**x) for x in kwargs.get("comments", [])]
        else:
            self.comments = []

    def __str__(self) -> str:
        return f"#{self.case_id} {self.title}"

    def to_dict(self) -> dict:
        print(parse_enum_to_json(self.punishment_type))
        print(parse_enum_to_json(self.creation_type))
        return {
            "id": self.id,
            "caseId": self.case_id,
            "guildId": self.guild_id,
            "title": self.title,
            "description": self.description,
            "userId": self.user_id,
            "username": self.username,
            "discriminator": self.discriminator,
            "nickname": self.nickname,
            "modId": self.mod_id,
            "createdAt": parse_dt_to_json(self.created_at),
            "occuredAt": parse_dt_to_json(self.occured_at),
            "lastEditedAt": parse_dt_to_json(self.last_edited_at),
            "lastEditedByModId": self.last_edited_by_mod_id,
            "punishment": self.punishment,
            "labels": self.labels,
            "others": self.others,
            "valid": self.valid,
            "creationType": parse_enum_to_json(self.creation_type),
            "punishmentType": parse_enum_to_json(self.punishment_type),
            "punishedUntil": parse_dt_to_json(self.punished_until),
            "punishmentActive": self.punishment_active,
            "allowComments": self.allow_comments,
            "lockedByUserId": self.locked_by_user_id,
            "lockedAt": parse_dt_to_json(self.locked_at),
            "markedToDeleteAt": parse_dt_to_json(self.marked_to_delete_at),
            "deletedByUserId": self.deleted_by_user_id,
            "comments": [x.to_dict() for x in self.comments]
        }
