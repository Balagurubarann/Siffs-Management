from typing import Dict, List

def verify_required_fields(required_fields: Dict) -> List[List[str], str]:

    """
        Return array of missed field names
    """

    missing: List[str] = [k for k, v in required_fields.items() if v is None]

    if missing:

        return [missing, ",".join(missing)]