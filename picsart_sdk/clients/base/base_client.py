from abc import abstractmethod
from typing import Dict, Union, IO
from urllib.parse import urlencode

from picsart_sdk.api_response import ApiResponse, ApiResponseData


class BaseClient:
    _payload = None
    _files = None
    headers = {
        "accept": "application/json",
    }

    files: Dict[str, Union[str, IO]] = {}

    def __init__(self, session, http_client, *args, **kwargs):
        self.session = session
        self.http_client = http_client

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

    def get_payload(self) -> dict:
        return self._payload

    def get_files(self) -> dict:
        return self._files

    @property
    def endpoint_url(self) -> str:
        return f"{self.base_url}/{self.session.api_version}/{self.endpoint}"

    def post(self, request) -> ApiResponse:
        self.set_payload(request)
        result = self.http_client.post(
            url=self.endpoint_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
        )

        return self._parse_response(result=result)

    async def async_post(self, request) -> ApiResponse:
        self.set_payload(request)
        result = await self.http_client.post(
            url=self.endpoint_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
        )

        return self._parse_response(result=result)

    def _get_url(self, postfix_url: str = "", query_params: dict = None) -> str:
        url = f"{self.endpoint_url}/{postfix_url}" if postfix_url else self.endpoint_url

        if query_params is not None:
            query_string = urlencode(query_params)
            url += f"?{query_string}"

        return url

    def get(self, postfix_url: str = "", query_params: dict = None) -> ApiResponse:
        result = self.http_client.get(
            url=self._get_url(postfix_url, query_params),
            headers=self.headers,
        )

        return self._parse_response(result=result)

    async def async_get(
        self, postfix_url: str = "", query_params: dict = None
    ) -> ApiResponse:
        result = await self.http_client.get(
            url=self._get_url(postfix_url, query_params),
            headers=self.headers,
        )

        return self._parse_response(result=result)

    def _parse_response(self, result: dict) -> ApiResponse:
        data = result["data"] if "data" in result else None
        return ApiResponse(
            status=result["status"],
            data=ApiResponseData(url=data["url"], id=data["id"]) if data else None,
            transaction_id=result.get("transaction_id"),
        )
