from dataclasses import dataclass


@dataclass
class ImageTaggingApiResponseData:
    tags: list[str]


@dataclass
class ImageTaggingApiResponse:
    status: str
    data: ImageTaggingApiResponseData
