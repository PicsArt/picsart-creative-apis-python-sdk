import os
from typing import IO, Any, Dict

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors
from picsart_sdk.core.logger import get_logger
from picsart_sdk.settings import PICSART_LOG_HTTP_CALLS, PICSART_LOG_HTTP_CALLS_HEADERS

logger = get_logger()


class AsyncHttpClient(BaseHttpClient):
    _raw_response = None
    _json_response = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def post(
        self,
        url: str,
        data: dict[str, any],
        files: dict[str, any],
        headers: dict[str, str],
    ) -> Any:
        response = await self._do_call(
            method="POST",
            url=url,
            data=data,
            files=files,
            headers=headers,
        )

        return response.json()

    async def get(
        self,
        url: str,
        headers: Dict[str, str] = None,
        as_json: bool = True,
    ):
        response = await self._do_call(
            method="GET",
            url=url,
            headers=headers,
        )

        self._raw_response = response
        self._json_response = response.json()

        if as_json:
            return self._json_response

        return self._raw_response

    @property
    def json(self):
        return self._json_response

    @property
    def raw_response(self):
        return self._raw_response

    @handle_http_errors
    async def _do_call(
        self,
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
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.request(
                    method=method,
                    url=url,
                    headers={**headers, **self.default_headers},
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
