from abc import abstractmethod
from typing import Dict, Union, IO

from picsart_sdk.api_response import ApiResponse, ApiResponseData


class BaseClient:
    _payload = None
    _files = None
    headers = {
        "accept": "application/json",
    }

    files: Dict[str, Union[str, IO]] = {}

    def __init__(self, session, *args, **kwargs):
        self.session = session
        self.headers = {
            **self.headers,
            **kwargs.get("headers", {}),
            "X-Picsart-API-Key": session.api_key,
        }

    @property
    @abstractmethod
    def base_url(self) -> str: ...

    @property
    @abstractmethod
    def endpoint(self) -> str: ...

    @abstractmethod
    def set_payload(self, request): ...

    def get_payload(self):
        return self._payload

    def get_files(self):
        return self._files

    @property
    def post_url(self):
        return f"{self.base_url}/{self.session.api_version}/{self.endpoint}"

    def post(self, request):
        self.set_payload(request)
        result = self.session.http_client.post(
            url=self.post_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
        )

        return ApiResponse(
            status=result["status"],
            data=ApiResponseData(url=result["data"]["url"], id=result["data"]["id"]),
        )

    async def async_post(self, request):
        self.set_payload(request)
        result = await self.session.http_client.post(
            url=self.post_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
        )

        return ApiResponse(
            status=result["status"],
            data=ApiResponseData(url=result["data"]["url"], id=result["data"]["id"]),
        )
