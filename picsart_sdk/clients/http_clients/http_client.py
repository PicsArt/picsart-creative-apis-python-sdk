from typing import IO, Any, Dict

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors


class HttpClient(BaseHttpClient):
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
        request_params = self.prepare_request_params(
            method=method,
            url=url,
            data=data,
            files=files,
            headers=headers,
            as_json=as_json,
        )
        try:
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
