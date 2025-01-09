from dataclasses import dataclass
from typing import Optional


@dataclass
class Text2TextApiResponse:
    """
    The response object returned by the Text2Text API.

    :param status: The status of the request
    :param data: The response string for the chat completion
    """

    status: str
    data: Optional[str]
