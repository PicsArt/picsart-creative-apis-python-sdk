from dataclasses import dataclass
from typing import Optional


@dataclass
class ApiResponseData:
    """
    Represents the data of an API response.

    :param id: The unique identifier for the response data.
    :type id: str
    :param url: The URL associated with the response data.
    :type url: str
    """

    id: str
    url: str


@dataclass
class ApiResponse:
    """
    Represents the response returned by the API.

    This data class encapsulates the status, data, and optional transaction ID
    of an API response.

    :param status: The status of the API response (e.g., "success", "error").
    :param data: The main data payload of the API response.
    :param transaction_id: An optional identifier for the transaction associated with this response.
    """

    status: str
    data: ApiResponseData
    transaction_id: Optional[str] = None
