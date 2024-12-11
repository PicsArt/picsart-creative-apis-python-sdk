from dataclasses import dataclass


@dataclass
class ImageTaggingApiResponseData:
    """
    Represents the data of the Image Tagging API response.

    :param tags: The list of tags for the image.
    """

    tags: list[str]


@dataclass
class ImageTaggingApiResponse:
    """
    Represents the data of the Image Tagginng API response.

    :param status: The status of the API response (e.g., "success", "error").
    :param data: The object containing the tags of the image.
    """

    status: str
    data: ImageTaggingApiResponseData
