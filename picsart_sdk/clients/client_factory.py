import importlib

from picsart_sdk.clients.base.base_client import BaseClient


class ClientFactory:
    _clients = {
        "upload": "picsart_sdk.clients.upload_client.UploadClient",
        "removebg": "picsart_sdk.clients.remove_background_client.RemoveBackgroundClient",
    }

    @staticmethod
    def get_client(client_name: str, session, *args, **kwargs):
        class_path = ClientFactory._clients.get(client_name.lower())
        if not class_path:
            raise ValueError(f"Unknown client name: {client_name}")

        module_name, class_name = class_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        client_class = getattr(module, class_name)
        if not issubclass(client_class, BaseClient):
            raise TypeError(f"{class_name} does not implement BaseClient")

        return client_class(session, *args, **kwargs)

    @staticmethod
    def add_client(name: str, class_name):
        ClientFactory._clients[name] = class_name
