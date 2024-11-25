import importlib
from enum import Enum

from picsart_sdk.clients.base.base_client import BaseClient


class Clients(str, Enum):
    UPLOAD = "upload"
    REMOVEBG = "removebg"
    UPSCALE = "upscale"
    ULTRA_UPSCALE = "ultra_upscale"


class ClientFactory:
    _clients = {
        Clients.UPLOAD.value: "picsart_sdk.clients.UploadClient",
        Clients.REMOVEBG.value: "picsart_sdk.clients.RemoveBackgroundClient",
        Clients.UPSCALE.value: "picsart_sdk.clients.UpscaleClient",
        Clients.ULTRA_UPSCALE.value: "picsart_sdk.clients.UltraUpscaleClient",
    }

    @staticmethod
    def get_client(client_name: str, session, is_async=False, *args, **kwargs):
        class_path = ClientFactory._clients.get(client_name.lower())
        if not class_path:
            raise ValueError(f"Unknown client name: {client_name}")

        module_name, class_name = class_path.rsplit(".", 1)
        if is_async:
            class_name = f"Async{class_name}"

        module = importlib.import_module(module_name)
        client_class = getattr(module, class_name)
        if not issubclass(client_class, BaseClient):
            raise TypeError(f"{class_name} does not implement BaseClient")

        return client_class(session, *args, **kwargs)

    @staticmethod
    def add_client(name: str, class_name):
        ClientFactory._clients[name] = class_name
