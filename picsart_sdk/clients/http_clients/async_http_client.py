from typing import IO, Any, Dict, Optional

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors


class AsyncHttpClient(BaseHttpClient):
    async def post(
        self,
        url: str,
        data: dict[str, any],
        files: dict[str, any],
        headers: dict[str, str],
        as_json: bool = False,
    ) -> Any:
        response = await self._do_call(
            method="POST",
            url=url,
            data=data,
            files=files,
            headers=headers,
            as_json=as_json,
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

    @handle_http_errors
    async def _do_call(
        self,
        method: str,
        url,
        data: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        as_json: Optional[bool] = False,
    ) -> Response:
        request_params = self.prepare_request_params(
            method=method,
            url=url,
            data=data,
            files=files,
            headers=headers,
            as_json=as_json,
        )

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.request(**request_params)
            response.raise_for_status()
            return response
        finally:
            # Close any file descriptors opened by this method
            if files:
                for file in files.values():
                    if isinstance(file, IO):
                        file.close()
