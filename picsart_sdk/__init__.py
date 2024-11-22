from picsart_sdk.clients.http_client import HttpClient
from picsart_sdk.core.session import Session


def client(client_name: str, *args, **kwargs):
    """
    Create a low-level service client by name using the default session.

    See :py:meth:`boto3.session.Session.client`.
    """
    return Session.get_default_session().client(
        client_name=client_name, *args, **kwargs
    )
