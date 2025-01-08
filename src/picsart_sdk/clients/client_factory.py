import importlib
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.clients.base.base_http_client import BaseHttpClient


class PicsartAPI(str, Enum):
    """
    The available API Clients.
    """

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
    """

    _clients = {
        PicsartAPI.BALANCE: "picsart_sdk.clients.BalanceClient",
        PicsartAPI.GEN_AI_BALANCE: "picsart_sdk.clients.GenAiBalanceClient",
        PicsartAPI.UPLOAD: "picsart_sdk.clients.UploadClient",
        PicsartAPI.REMOVE_BACKGROUND: "picsart_sdk.clients.RemoveBackgroundClient",
        PicsartAPI.UPSCALE: "picsart_sdk.clients.UpscaleClient",
        PicsartAPI.ULTRA_UPSCALE: "picsart_sdk.clients.UltraUpscaleClient",
        PicsartAPI.ULTRA_ENHANCE: "picsart_sdk.clients.UltraEnhanceClient",
        PicsartAPI.FACE_ENHANCEMENT: "picsart_sdk.clients.FaceEnhancementClient",
        PicsartAPI.EFFECTS: "picsart_sdk.clients.EffectsClient",
        PicsartAPI.AI_EFFECTS: "picsart_sdk.clients.AiEffectsClient",
        PicsartAPI.EFFECTS_PREVIEWS: "picsart_sdk.clients.EffectsPreviewsClient",
        PicsartAPI.COLOR_TRANSFER: "picsart_sdk.clients.ColorTransferClient",
        PicsartAPI.STYLE_TRANSFER: "picsart_sdk.clients.StyleTransferClient",
        PicsartAPI.MASKS: "picsart_sdk.clients.MasksClient",
        PicsartAPI.MASKS_PREVIEWS: "picsart_sdk.clients.MasksPreviewsClient",
        PicsartAPI.ADJUST: "picsart_sdk.clients.AdjustClient",
        PicsartAPI.EDIT: "picsart_sdk.clients.EditClient",
        PicsartAPI.TEXTURE_GENERATOR: "picsart_sdk.clients.TextureGeneratorClient",
        PicsartAPI.VECTORIZER: "picsart_sdk.clients.VectorizerClient",
        PicsartAPI.SURFACEMAP: "picsart_sdk.clients.SurfacemapClient",
        PicsartAPI.IMAGE_TAGGING: "picsart_sdk.clients.ImageTaggingClient",
        PicsartAPI.IMAGE_DESCRIPTION: "picsart_sdk.clients.ImageDescriptionClient",
        PicsartAPI.TEXT2IMAGE: "picsart_sdk.clients.Text2ImageClient",
        PicsartAPI.TEXT2TEXT: "picsart_sdk.clients.Text2TextClient",
        PicsartAPI.INPAINTING: "picsart_sdk.clients.InpaintingClient",
        PicsartAPI.OUTPAINTING: "picsart_sdk.clients.OutpaintingClient",
        PicsartAPI.REPLACE_BACKGROUND: "picsart_sdk.clients.PaintingReplaceBackgroundClient",
        PicsartAPI.EXPAND: "picsart_sdk.clients.PaintingExpandClient",
        PicsartAPI.BLEED: "picsart_sdk.clients.BleedClient",
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
        """
        The factory method to retrieve a specific API client (eg: :ref:`upscale_client`, :ref:`edit_client`, etc).

        :param client_name: The client name as defined in `PicsartAPI`
        :type client_name: str
        :param session: The session to use
        :type session: An instance of type :class:`~picsart_sdk.session.Session`
        :param http_client: The http client to use. An implementation of the :class:`~BaseHttpClient` class.
        :param is_async: Specifies if the HTTP client is asynchronous
        :type is_async: bool
        :param version: The version of the API to use
        :type version: str
        :param args: Other arguments
        :param kwargs: Other keyword arguments
        :return: An API Client instance.
        :rtype: :class:`~picsart_sdk.clients.base.base_http_client.BaseHttpClient`
        """
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
