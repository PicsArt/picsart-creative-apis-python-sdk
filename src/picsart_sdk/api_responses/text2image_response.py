from dataclasses import dataclass
from typing import Optional


@dataclass
class Text2ImageCreateApiResponse:
    inference_id: str
    status: str


@dataclass
class Text2ImageApiResponseData:
    id: str
    url: str
    status: str


@dataclass
class Text2ImageApiResponse:
    status: str
    data: Optional[list[Text2ImageApiResponseData]] = None
