from dataclasses import dataclass


@dataclass
class MasksPreviewsApiResponseData:
    id: str
    url: str
    mask: str


@dataclass
class MasksPreviewsApiResponse:
    status: str
    data: list[MasksPreviewsApiResponseData]
