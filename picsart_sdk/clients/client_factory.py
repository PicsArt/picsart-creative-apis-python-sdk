import importlib
from enum import Enum

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.clients.base.base_http_client import BaseHttpClient


class ApiClient(str, Enum):
    UPLOAD = "upload"
    REMOVE_BACKGROUND = "remove_background"
    UPSCALE = "upscale"
    ULTRA_UPSCALE = "ultra_upscale"
    ULTRA_ENHANCE = "ultra_enhance"
    FACE_ENHANCEMENT = "face_enhancement"
    EFFECTS = "effects"
    AI_EFFECTS = "ai_effects"
    EFFECTS_PREVIEWS = "effects_previews"
    BALANCE = "balance"
    COLOR_TRANSFER = "color_transfer"
    STYLE_TRANSFER = "style_transfer"
    MASKS = "masks"
    MASKS_PREVIEWS = "masks_previews"
    ADJUST = "adjust"


class ClientFactory:
    _clients = {
        ApiClient.BALANCE.value: "picsart_sdk.clients.BalanceClient",
        ApiClient.UPLOAD.value: "picsart_sdk.clients.UploadClient",
        ApiClient.REMOVE_BACKGROUND.value: "picsart_sdk.clients.RemoveBackgroundClient",
        ApiClient.UPSCALE.value: "picsart_sdk.clients.UpscaleClient",
        ApiClient.ULTRA_UPSCALE.value: "picsart_sdk.clients.UltraUpscaleClient",
        ApiClient.ULTRA_ENHANCE.value: "picsart_sdk.clients.UltraEnhanceClient",
        ApiClient.FACE_ENHANCEMENT.value: "picsart_sdk.clients.FaceEnhancementClient",
        ApiClient.EFFECTS.value: "picsart_sdk.clients.EffectsClient",
        ApiClient.AI_EFFECTS.value: "picsart_sdk.clients.AiEffectsClient",
        ApiClient.EFFECTS_PREVIEWS.value: "picsart_sdk.clients.EffectsPreviewsClient",
        ApiClient.COLOR_TRANSFER.value: "picsart_sdk.clients.ColorTransferClient",
        ApiClient.STYLE_TRANSFER.value: "picsart_sdk.clients.StyleTransferClient",
        ApiClient.MASKS.value: "picsart_sdk.clients.MasksClient",
        ApiClient.MASKS_PREVIEWS.value: "picsart_sdk.clients.MasksPreviewsClient",
        ApiClient.ADJUST.value: "picsart_sdk.clients.AdjustClient",
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
