from dataclasses import dataclass
from typing import Optional


@dataclass
class Text2ImageCreateApiResponse:
    """
    Represents the response for a `text2image` request.

    :param inference_id: An identifier for the transaction associated with this response, to be used to retrieve the results.
    :param status: The status of the request.
    """

    inference_id: str
    status: str


@dataclass
class Text2ImageApiResponseData:
    """ ""
    Represents the data of an API response for Text to Image call.

    :param id: The unique identifier for the response data.
    :param url: The URL associated with the response data.
    :param status: The status of the processing.
    """

    id: str
    url: str
    status: str


@dataclass
class Text2ImageApiResponse:
    """
    Represents the response with the result returned by the Text2Image API.

    :param status: The status of the API response (e.g., "success", "error").
    :param data: The main data payload of the API response.
    """

    status: str
    data: Optional[list[Text2ImageApiResponseData]] = None
