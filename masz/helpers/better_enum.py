from typing import Optional

def parse(value) -> Optional[int]:
    if not value:
        return None
    try:
        return value.value
    except:
        return None
