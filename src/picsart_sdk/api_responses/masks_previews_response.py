from dataclasses import dataclass


@dataclass
class MasksPreviewsApiResponseData:
    """
    Represents the data of an API response.

    :param id: The unique identifier for the response data.
    :param url: The URL associated with the response data.
    :param mask: The mask name associated with the response data.
    """

    id: str
    url: str
    mask: str


@dataclass
class MasksPreviewsApiResponse:
    """
    Represents the data of the Mask Previews API response.

    :param status: The status of the API response (e.g., "success", "error").
    :param data: The object containing the details of the API response.
    """

    status: str
    data: list[MasksPreviewsApiResponseData]
