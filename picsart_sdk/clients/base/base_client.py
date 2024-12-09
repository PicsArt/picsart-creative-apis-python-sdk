from abc import abstractmethod
from typing import IO, Dict, Optional, Union
from urllib.parse import urlencode

from picsart_sdk.clients.http_clients import AsyncHttpClient, HttpClient


class BaseClient:
    _payload = None
    _files = None
    _version = None
    headers = {
        "Accept": "application/json",
    }

    files: Dict[str, Union[str, IO]] = {}

    def __init__(
        self, session, http_client, version: Optional[str] = None, *args, **kwargs
    ):
        self._payload = self._payload if self._payload else {}
        self.session = session
        self.http_client = http_client
        self._version = version

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

    @abstractmethod
    def parse_response(self, result: dict): ...

    @property
    @abstractmethod
    def version(self): ...

    def set_version(self, version):
        self._version = version

    def get_payload(self) -> dict:
        return self._payload

    def get_files(self) -> dict:
        return self._files

    @property
    def endpoint_url(self) -> str:
        return f"{self.base_url}/{self.version}/{self.endpoint}"

    def post(self, request, as_json: Optional[bool] = False):
        self.set_payload(request)
        http_client: HttpClient = self.http_client
        result = http_client.post(
            url=self.endpoint_url,
            data=self._payload,
            files=self.get_files(),
            headers=self.headers,
            as_json=as_json,
        )

        return self.parse_response(result=result)

    async def async_post(self, request, as_json: Optional[bool] = False):
        self.set_payload(request)
        http_client: AsyncHttpClient = self.http_client
        result = await http_client.post(
            url=self.endpoint_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
            as_json=as_json,
        )

        return self.parse_response(result=result)

    def _get_url(self, postfix_url: str = "", query_params: dict = None) -> str:
        url = f"{self.endpoint_url}/{postfix_url}" if postfix_url else self.endpoint_url

        if query_params is not None:
            query_string = urlencode(query_params)
            url += f"?{query_string}"

        return url

    def get(self, postfix_url: str = "", query_params: dict = None):
        result = self.http_client.get(
            url=self._get_url(postfix_url, query_params),
            headers=self.headers,
        )

        return self.parse_response(result=result)

    async def async_get(self, postfix_url: str = "", query_params: dict = None):
        result = await self.http_client.get(
            url=self._get_url(postfix_url, query_params),
            headers=self.headers,
        )

        return self.parse_response(result=result)
