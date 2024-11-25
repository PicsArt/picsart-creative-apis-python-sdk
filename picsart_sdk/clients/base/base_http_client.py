from abc import ABC, abstractmethod
from functools import wraps

import httpx

from picsart_sdk.clients.api_error import APIError


def handle_http_errors(func):
    """
    Decorator to handle HTTP errors.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except httpx.HTTPStatusError as e:
            default_message = (
                "HTTP 400 error" if e.response.status_code == 400 else "HTTP 500 error"
            )

            try:
                error_data = e.response.json()
            except ValueError:
                error_data = {
                    "detail": str(e),
                    "message": default_message,
                    "code": e.response.status_code,
                }

            raise APIError(response_data=error_data) from e

    return wrapper


class BaseHttpClient(ABC):

    @abstractmethod
    def post(self, url, payload, files, headers): ...

    @abstractmethod
    def get(self, url, headers): ...
