import importlib
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.clients.base.base_http_client import BaseHttpClient


class ApiClient(str, Enum):
    AI_EFFECTS = "ai_effects"
    ADJUST = "adjust"
    BALANCE = "balance"
    BLEED = "bleed"
    COLOR_TRANSFER = "color_transfer"
    EDIT = "edit"
    EFFECTS = "effects"
    EFFECTS_PREVIEWS = "effects_previews"
    EXPAND = "expand"
    FACE_ENHANCEMENT = "face_enhancement"
    GEN_AI_BALANCE = "gen_ai_balance"
    IMAGE_DESCRIPTION = "image_description"
    IMAGE_TAGGING = "image_tagging"
    INPAINTING = "inpainting"
    MASKS = "masks"
    MASKS_PREVIEWS = "masks_previews"
    OUTPAINTING = "outpainting"
    REMOVE_BACKGROUND = "remove_background"
    REPLACE_BACKGROUND = "replace_background"
    STYLE_TRANSFER = "style_transfer"
    SURFACEMAP = "surfacemap"
    TEXT2IMAGE = "text2image"
    TEXT2TEXT = "text2text"
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
        ApiClient.BALANCE: "picsart_sdk.clients.BalanceClient",
        ApiClient.GEN_AI_BALANCE: "picsart_sdk.clients.GenAiBalanceClient",
        ApiClient.UPLOAD: "picsart_sdk.clients.UploadClient",
        ApiClient.REMOVE_BACKGROUND: "picsart_sdk.clients.RemoveBackgroundClient",
        ApiClient.UPSCALE: "picsart_sdk.clients.UpscaleClient",
        ApiClient.ULTRA_UPSCALE: "picsart_sdk.clients.UltraUpscaleClient",
        ApiClient.ULTRA_ENHANCE: "picsart_sdk.clients.UltraEnhanceClient",
        ApiClient.FACE_ENHANCEMENT: "picsart_sdk.clients.FaceEnhancementClient",
        ApiClient.EFFECTS: "picsart_sdk.clients.EffectsClient",
        ApiClient.AI_EFFECTS: "picsart_sdk.clients.AiEffectsClient",
        ApiClient.EFFECTS_PREVIEWS: "picsart_sdk.clients.EffectsPreviewsClient",
        ApiClient.COLOR_TRANSFER: "picsart_sdk.clients.ColorTransferClient",
        ApiClient.STYLE_TRANSFER: "picsart_sdk.clients.StyleTransferClient",
        ApiClient.MASKS: "picsart_sdk.clients.MasksClient",
        ApiClient.MASKS_PREVIEWS: "picsart_sdk.clients.MasksPreviewsClient",
        ApiClient.ADJUST: "picsart_sdk.clients.AdjustClient",
        ApiClient.EDIT: "picsart_sdk.clients.EditClient",
        ApiClient.TEXTURE_GENERATOR: "picsart_sdk.clients.TextureGeneratorClient",
        ApiClient.VECTORIZER: "picsart_sdk.clients.VectorizerClient",
        ApiClient.SURFACEMAP: "picsart_sdk.clients.SurfacemapClient",
        ApiClient.IMAGE_TAGGING: "picsart_sdk.clients.ImageTaggingClient",
        ApiClient.IMAGE_DESCRIPTION: "picsart_sdk.clients.ImageDescriptionClient",
        ApiClient.TEXT2IMAGE: "picsart_sdk.clients.Text2ImageClient",
        ApiClient.TEXT2TEXT: "picsart_sdk.clients.Text2TextClient",
        ApiClient.INPAINTING: "picsart_sdk.clients.InpaintingClient",
        ApiClient.OUTPAINTING: "picsart_sdk.clients.OutpaintingClient",
        ApiClient.REPLACE_BACKGROUND: "picsart_sdk.clients.PaintingReplaceBackgroundClient",
        ApiClient.EXPAND: "picsart_sdk.clients.PaintingExpandClient",
        ApiClient.BLEED: "picsart_sdk.clients.BleedClient",
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
