import inspect
from abc import ABC, abstractmethod
from functools import wraps

import httpx

from picsart_sdk.version import __version__
from picsart_sdk.clients.api_error import ApiError, ApiAuthenticationError


def handle_error(e: httpx.HTTPStatusError):
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

    if e.response.status_code == 401:
        raise ApiAuthenticationError(response_data=error_data) from e

    raise ApiError(response_data=error_data) from e


def handle_http_errors(func):
    """
    Decorator to handle HTTP errors for both sync and async functions.
    """
    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except httpx.HTTPStatusError as e:
                handle_error(e)

        return async_wrapper
    else:

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except httpx.HTTPStatusError as e:
                handle_error(e)

        return sync_wrapper


class BaseHttpClient(ABC):

    default_headers = {
        "User-Agent": f"picsart-sdk-python / {__version__}",
        "Accept": "application/json",
    }

    @abstractmethod
    def post(self, url, payload, files, headers): ...

    @abstractmethod
    def get(self, url, headers): ...
