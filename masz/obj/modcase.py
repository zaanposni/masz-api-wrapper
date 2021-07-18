from typing import List
from datetime import datetime

import dateparser

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
        self.created_at = dateparser.parse(kwargs.get("createdAt"))
        self.occured_at = dateparser.parse(kwargs.get("occuredAt"))
        self.last_edited_at = dateparser.parse(kwargs.get("lastEditedAt"))
        self.last_edited_by_mod_id = kwargs.get("lastEditedByModId")
        self.punishment = kwargs.get("punishment")
        self.labels = kwargs.get("labels", [])
        self.others = kwargs.get("others")
        self.valid = kwargs.get("valid", False)
        self.creation_type = kwargs.get("creationType", CreationType.DEFAULT)
        self.punishment_type = kwargs.get("punishmentType", PunishmentType.NONE)
        self.punished_until = kwargs.get("punishedUntil")
        self.punishment_active = kwargs.get("punishmentActive", False)
        self.allow_comments = kwargs.get("allowComments", False)
        self.locked_by_user_id = kwargs.get("lockedByUserId")
        self.locked_at = dateparser.parse(kwargs.get("lockedAt"))
        self.marked_to_delete_at = dateparser.parse(kwargs.get("markedToDeleteAt"))
        self.deleted_by_user_id = kwargs.get("deletedByUserId")
        self.comments = [Comment(**x) for x in kwargs.get("comments", [])]

    def __str__(self) -> str:
        return f"#{self.case_id} {self.title}"
