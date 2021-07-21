from datetime import datetime
from typing import Optional
import pytz

import dateparser

def parse(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    x = dateparser.parse(value)
    return x.replace(tzinfo=pytz.UTC)


def parse_to_json(value: Optional[datetime]) -> Optional[str]:
    if not value or not isinstance(value, datetime):
        return None
    return value.isoformat()
