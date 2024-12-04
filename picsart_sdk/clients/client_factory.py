import importlib
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.clients.base.base_http_client import BaseHttpClient


class ApiClient(str, Enum):
    AI_EFFECTS = "ai_effects"
    ADJUST = "adjust"
    BALANCE = "balance"
    COLOR_TRANSFER = "color_transfer"
    EDIT = "edit"
    EFFECTS = "effects"
    EFFECTS_PREVIEWS = "effects_previews"
    FACE_ENHANCEMENT = "face_enhancement"
    IMAGE_DESCRIPTION = "image_description"
    IMAGE_TAGGING = "image_tagging"
    MASKS = "masks"
    MASKS_PREVIEWS = "masks_previews"
    REMOVE_BACKGROUND = "remove_background"
    STYLE_TRANSFER = "style_transfer"
    SURFACEMAP = "surfacemap"
    TEXT2IMAGE = "text2image"
    TEXTURE_GENERATOR = "texture_generator"
    ULTRA_ENHANCE = "ultra_enhance"
    ULTRA_UPSCALE = "ultra_upscale"
    UPLOAD = "upload"
    UPSCALE = "upscale"
    VECTORIZER = "vectorizer"


class ClientFactory:
    """
    Factory class to create instances of API clients in the Picsart SDK.

    This class provides a centralized way to retrieve instances of specific
    API clients based on their names.

    Attributes:
        _clients (dict): A mapping of client names to their class paths.
    """

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
        ApiClient.EDIT.value: "picsart_sdk.clients.EditClient",
        ApiClient.TEXTURE_GENERATOR.value: "picsart_sdk.clients.TextureGeneratorClient",
        ApiClient.VECTORIZER.value: "picsart_sdk.clients.VectorizerClient",
        ApiClient.SURFACEMAP.value: "picsart_sdk.clients.SurfacemapClient",
        ApiClient.IMAGE_TAGGING.value: "picsart_sdk.clients.ImageTaggingClient",
        ApiClient.IMAGE_DESCRIPTION.value: "picsart_sdk.clients.ImageDescriptionClient",
        ApiClient.TEXT2IMAGE.value: "picsart_sdk.clients.Text2ImageClient",
    }

    @staticmethod
    def get_client(
        client_name: str,
        session,
        http_client: BaseHttpClient,
        is_async: Optional[bool] = False,
        version: Optional[str] = None,
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

        return client_class(
            session=session, http_client=http_client, version=version, *args, **kwargs
        )

    @staticmethod
    def add_client(name: str, class_name):
        ClientFactory._clients[name] = class_name
