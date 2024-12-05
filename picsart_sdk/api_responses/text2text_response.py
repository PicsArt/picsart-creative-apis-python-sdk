from dataclasses import dataclass
from typing import Optional


@dataclass
class Text2TextApiResponse:
    status: str
    data: Optional[str]
