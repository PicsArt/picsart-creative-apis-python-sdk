import os
from typing import IO, Any, Dict

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors
from picsart_sdk.core.logger import get_logger
from picsart_sdk.settings import PICSART_LOG_HTTP_CALLS, PICSART_LOG_HTTP_CALLS_HEADERS

logger = get_logger()


class HttpClient(BaseHttpClient):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def post(
        self,
        url: str,
        data: dict[str, any],
        files: dict[str, any],
        headers: dict[str, str],
        as_json: bool = False,
    ) -> Any:
        response = self._do_call(
            method="POST",
            url=url,
            data=data,
            files=files,
            headers=headers,
            as_json=as_json,
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

    @handle_http_errors
    def _do_call(
        self,
        method: str,
        url,
        data: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        as_json: bool = False,
    ) -> Response:
        try:
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

            with httpx.Client(timeout=self.timeout) as client:
                response = client.request(**request_params)
            response.raise_for_status()
            return response
        finally:
            # Close any file descriptors opened by this method
            if files:
                for file in files.values():
                    if isinstance(file, IO):
                        file.close()
