from typing import TypedDict, Optional

class JSONReponse(TypedDict, total=False):

    message: str
    success: bool
    data: Optional[dict[str, any]]
