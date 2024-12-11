from dataclasses import dataclass


@dataclass
class ImageDescriptionApiResponseData:
    description: str


@dataclass
class ImageDescriptionApiResponse:
    status: str
    data: ImageDescriptionApiResponseData
