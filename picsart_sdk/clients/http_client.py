from typing import Dict, Any, IO

import httpx
from httpx import Response

from picsart_sdk.clients.base.base_client import BaseClient


class HttpClient:
    def __init__(self, api_client: BaseClient):
        self.api_client = api_client

    def post(self) -> Any:
        response = self._do_call(
            method="POST",
            url=self.api_client.post_url,
            payload=self.api_client.get_payload(),
            files=self.api_client.get_files(),
            headers=self.api_client.headers,
        )

        return response.json()

    @classmethod
    def _do_call(
        cls,
        method: str,
        url,
        payload: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
    ) -> Response:
        print(f"{method} {url}: payload={payload} files={files} headers={headers}")

        try:
            with httpx.Client() as client:
                response = client.post(
                    url=url,
                    headers=headers,
                    data=payload,
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
