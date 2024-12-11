from dataclasses import dataclass
from typing import Optional


@dataclass
class PaintingDataItemApiResponse:
    id: str
    url: str


@dataclass
class PaintingApiResponse:
    status: str
    data: list[PaintingDataItemApiResponse]
    inference_id: Optional[str] = None
