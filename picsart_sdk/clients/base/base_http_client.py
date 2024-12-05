import inspect
from abc import ABC, abstractmethod
from functools import wraps
from typing import Any, Dict

import httpx

from picsart_sdk.clients.api_error import ApiAuthenticationError, ApiError
from picsart_sdk.core.logger import get_logger
from picsart_sdk.settings import PICSART_LOG_HTTP_CALLS, PICSART_LOG_HTTP_CALLS_HEADERS
from picsart_sdk.version import __version__

logger = get_logger()


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
    _raw_response = None
    _json_response = None

    default_headers = {
        "User-Agent": f"picsart-sdk-python/{__version__}",
        "Accept": "application/json",
    }

    default_timeout_seconds = 30

    def __init__(self, timeout=default_timeout_seconds):
        self.timeout = timeout

    @abstractmethod
    def post(self, url, payload, files, headers): ...

    @abstractmethod
    def get(self, url, headers): ...

    def prepare_request_params(
        self,
        method: str,
        url,
        data: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        as_json: bool = False,
    ):
        request_params = {
            "method": method,
            "url": url,
            "headers": {
                **headers,
                **self.default_headers,
                "content-type": "application/json",
            },
        }

        if files:
            request_params["files"] = files

        if as_json:
            request_params["json"] = data
        else:
            request_params["data"] = data

        if PICSART_LOG_HTTP_CALLS:
            log_message = f"{request_params}"
            if not PICSART_LOG_HTTP_CALLS_HEADERS:
                filtered_dict = request_params.copy()
                filtered_dict.pop("headers", None)
                log_message = f"{filtered_dict}"

            logger.debug(log_message)

        return request_params

    @property
    def json(self):
        return self._json_response

    @property
    def raw_response(self):
        return self._raw_response
