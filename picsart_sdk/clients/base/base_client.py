from abc import abstractmethod
from typing import Dict, Union, IO

from picsart_sdk.clients.http_client import HttpClient


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
