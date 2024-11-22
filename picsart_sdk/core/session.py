import os

from picsart_sdk import HttpClient
from picsart_sdk.clients.client_factory import ClientFactory
from picsart_sdk.version import __version__


class Session:

    def __init__(self, api_key=None, api_version: str = "1.0"):
        self.user_agent_name = "picsart-sdk-python"
        self.user_agent_version = __version__

        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.environ.get("PICSART_API_KEY", "")

        self.api_version = api_version
        if self.api_version is None:
            self.api_version = os.environ.get("PICSART_API_VERSION", "1.0")

        # todo, inject somehow else in order to support also async http
        self.http_client = HttpClient()

    @staticmethod
    def get_default_session():
        return Session()

    def client(self, client_name: str):
        return ClientFactory.get_client(client_name=client_name, session=self)
