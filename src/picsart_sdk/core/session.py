import os

from picsart_sdk import AsyncHttpClient, HttpClient
from picsart_sdk.clients.client_factory import ClientFactory
from picsart_sdk.settings import DEFAULT_HTTP_TIMEOUT_SECONDS
from picsart_sdk.version import __version__


class Session:

    def __init__(self, api_key=None):
        self.user_agent_name = "picsart-sdk-python"
        self.user_agent_version = __version__

        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.environ.get("PICSART_API_KEY", "")

    @staticmethod
    def get_default_session():
        return Session()

    def client(
        self,
        client_name: str,
        is_async: bool = False,
        timeout: int = DEFAULT_HTTP_TIMEOUT_SECONDS,
        version=None,
    ):
        if is_async:
            http_client = AsyncHttpClient(timeout=timeout)
        else:
            http_client = HttpClient(timeout=timeout)

        return ClientFactory.get_client(
            client_name=client_name,
            session=self,
            is_async=is_async,
            http_client=http_client,
            version=version,
        )
