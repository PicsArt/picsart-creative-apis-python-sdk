from dataclasses import dataclass

from docutils.nodes import description


@dataclass
class ImageDescriptionApiResponseData:
    """
    Represents the data of the Image Description API response.

    :param description: The description of the image.
    """

    description: str


@dataclass
class ImageDescriptionApiResponse:
    """
    Represents the data of the Image Description API response.

    :param status: The status of the API response (e.g., "success", "error").
    :param data: The object containing the description of the image.
    """

    status: str
    data: ImageDescriptionApiResponseData
