from typing import IO, Any, Dict

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors


class AsyncHttpClient(BaseHttpClient):
    _raw_response = None
    _json_response = None

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

    @classmethod
    @handle_http_errors
    async def _do_call(
        cls,
        method: str,
        url,
        data: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
    ) -> Response:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
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
