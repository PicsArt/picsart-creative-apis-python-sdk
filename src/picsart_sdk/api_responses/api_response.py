from dataclasses import dataclass
from typing import Optional


@dataclass
class ApiResponseData:
    """
    Represents the data of an API response.

    Attributes:
        id (str): The unique identifier for the response data.
        url (str): The URL associated with the response data.
    """

    id: str
    url: str


@dataclass
class ApiResponse:
    """
    Represents the structure of an API response if not otherwise specified.

    Attributes:
        status (str): The status of the API response, such as "success" or "failure".
        data (ApiResponseData): The response data containing details such as an ID and URL. See :ref:`api_response_data` for details.
        transaction_id (Optional[str]): The transaction ID associated with the API response, if available.
    """

    status: str
    data: ApiResponseData
    transaction_id: Optional[str] = None
