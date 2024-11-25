from typing import Dict, Any, IO

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_http_client import BaseHttpClient, handle_http_errors


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
        try:
            with httpx.Client() as client:
                response = client.request(
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

    def get(self, url, headers):
        pass
