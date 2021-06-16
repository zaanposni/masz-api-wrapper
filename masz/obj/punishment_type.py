from enum import Enum

class PunishmentType(Enum):
    NONE: int = 0
    MUTE: int = 1
    KICK: int = 2
    BAN: int= 3
