import os
from typing import Dict, Any, IO

import httpx
from httpx import Response

from picsart_sdk.core.logger import get_logger
from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors

PICSART_LOG_HTTP_CALLS = os.environ.get("PICSART_LOG_HTTP_CALLS", "false") == "true"
PICSART_LOG_HTTP_CALLS_HEADERS = os.environ.get("PICSART_LOG_HTTP_CALLS_HEADERS", "false") == "true"

logger = get_logger()

class HttpClient(BaseHttpClient):
    def __init__(self):
        pass

    def post(
        self,
        url: str,
        data: dict[str, any],
        files: dict[str, any],
        headers: dict[str, str],
    ) -> Any:
        response = self._do_call(
            method="POST",
            url=url,
            data=data,
            files=files,
            headers=headers,
        )

        return response.json()

    def get(
        self,
        url: str,
        headers: Dict[str, str] = None,
    ):
        response = self._do_call(
            method="GET",
            url=url,
            headers=headers,
        )

        return response.json()

    @classmethod
    @handle_http_errors
    def _do_call(
        cls,
        method: str,
        url,
        data: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
    ) -> Response:
        if PICSART_LOG_HTTP_CALLS:
            if PICSART_LOG_HTTP_CALLS_HEADERS:
                logger.debug(f"{method} {url} {data} {files} {headers}")
            else:
                logger.debug(f"{method} {url} {data} {files}")

        try:
            with httpx.Client() as client:
                response = client.request(
                    method=method,
                    url=url,
                    headers={**headers, **cls.default_headers},
                    data=data,
                    files=files,
                )
            response.raise_for_status()
            return response
        finally:
            # Close any file descriptors opened by this method
            if files:
                for file in files.values():
                    if isinstance(file, IO):
                        file.close()
