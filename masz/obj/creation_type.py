from enum import Enum

class CreationType(Enum):
    DEFAULT: int = 0
    AUTO_MODERATION: int = 1
    IMPORTED: int = 2
    BY_COMMAND: int= 3
