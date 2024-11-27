import importlib
from enum import Enum

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.clients.base.base_http_client import BaseHttpClient


class Clients(str, Enum):
    UPLOAD = "upload"
    REMOVEBG = "removebg"
    UPSCALE = "upscale"
    ULTRA_UPSCALE = "ultra_upscale"
    ULTRA_ENHANCE = "ultra_enhance"
    FACE_ENHANCEMENT = "face_enhancement"


class ClientFactory:
    _clients = {
        Clients.UPLOAD.value: "picsart_sdk.clients.UploadClient",
        Clients.REMOVEBG.value: "picsart_sdk.clients.RemoveBackgroundClient",
        Clients.UPSCALE.value: "picsart_sdk.clients.UpscaleClient",
        Clients.ULTRA_UPSCALE.value: "picsart_sdk.clients.UltraUpscaleClient",
        Clients.ULTRA_ENHANCE.value: "picsart_sdk.clients.UltraEnhanceClient",
        Clients.FACE_ENHANCEMENT.value: "picsart_sdk.clients.FaceEnhancementClient",
    }

    @staticmethod
    def get_client(
        client_name: str,
        session,
        http_client: BaseHttpClient,
        is_async=False,
        *args,
        **kwargs,
    ):
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

        return client_class(session=session, http_client=http_client, *args, **kwargs)

    @staticmethod
    def add_client(name: str, class_name):
        ClientFactory._clients[name] = class_name
