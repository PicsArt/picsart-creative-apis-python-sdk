from dataclasses import dataclass
from typing import Optional


@dataclass
class PaintingDataItemApiResponse:
    """
    Represents the data of an API response.

    :param id: The unique identifier for the response data.
    :param url: The URL associated with the response data.
    """

    id: str
    url: str


@dataclass
class PaintingApiResponse:
    """
    Represents the response returned by the API.

    This data class encapsulates the status, data, and optional transaction ID
    of an API response.

    :param status: The status of the API response (e.g., "success", "error").
    :param data: The main data payload of the API response.
    :param inference_id: An optional identifier for the transaction associated with this response.
    """

    status: str
    data: list[PaintingDataItemApiResponse]
    inference_id: Optional[str] = None
