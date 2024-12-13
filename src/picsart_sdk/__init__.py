from picsart_sdk.clients.http_clients import AsyncHttpClient, HttpClient
from picsart_sdk.core.session import Session


def client(client_name: str, is_async: bool = False, api_key=None, *args, **kwargs):
    """
    Create a low-level service client by name.

    Returns an implementation of BaseClient class (eg: RemoveBackgroundClient).
    """
    if api_key:
        session = Session(api_key=api_key)
    else:
        session = Session.get_default_session()

    return session.client(client_name=client_name, is_async=is_async, *args, **kwargs)


def async_client(client_name: str, api_key=None, *args, **kwargs):
    """
    Create a low-level async service client by name.

    Returns an async implementation of BaseClient class (eg: AsyncRemoveBackgroundClient).
    """
    return client(
        client_name=client_name, is_async=True, api_key=api_key, *args, **kwargs
    )
