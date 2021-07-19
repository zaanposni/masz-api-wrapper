from datetime import datetime
from typing import Optional

import dateparser

def parse(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    return dateparser.parse(value)


def parse_to_json(value: Optional[datetime]) -> Optional[str]:
    if not value or not isinstance(value, datetime):
        return None
    return value.isoformat()
