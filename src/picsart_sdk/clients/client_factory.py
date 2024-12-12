import importlib
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.clients.base.base_http_client import BaseHttpClient


class ApiClient(str, Enum):
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
    Factory class to create instances of API clients_image_api in the Picsart SDK.

    This class provides a centralized way to retrieve instances of specific
    API clients_image_api based on their names.
    """

    _clients = {
        ApiClient.BALANCE: "picsart_sdk.clients_image_api.BalanceClient",
        ApiClient.GEN_AI_BALANCE: "picsart_sdk.clients_image_api.GenAiBalanceClient",
        ApiClient.UPLOAD: "picsart_sdk.clients_image_api.UploadClient",
        ApiClient.REMOVE_BACKGROUND: "picsart_sdk.clients_image_api.RemoveBackgroundClient",
        ApiClient.UPSCALE: "picsart_sdk.clients_image_api.UpscaleClient",
        ApiClient.ULTRA_UPSCALE: "picsart_sdk.clients_image_api.UltraUpscaleClient",
        ApiClient.ULTRA_ENHANCE: "picsart_sdk.clients_image_api.UltraEnhanceClient",
        ApiClient.FACE_ENHANCEMENT: "picsart_sdk.clients_image_api.FaceEnhancementClient",
        ApiClient.EFFECTS: "picsart_sdk.clients_image_api.EffectsClient",
        ApiClient.AI_EFFECTS: "picsart_sdk.clients_image_api.AiEffectsClient",
        ApiClient.EFFECTS_PREVIEWS: "picsart_sdk.clients_image_api.EffectsPreviewsClient",
        ApiClient.COLOR_TRANSFER: "picsart_sdk.clients_image_api.ColorTransferClient",
        ApiClient.STYLE_TRANSFER: "picsart_sdk.clients_image_api.StyleTransferClient",
        ApiClient.MASKS: "picsart_sdk.clients_image_api.MasksClient",
        ApiClient.MASKS_PREVIEWS: "picsart_sdk.clients_image_api.MasksPreviewsClient",
        ApiClient.ADJUST: "picsart_sdk.clients_image_api.AdjustClient",
        ApiClient.EDIT: "picsart_sdk.clients_image_api.EditClient",
        ApiClient.TEXTURE_GENERATOR: "picsart_sdk.clients_image_api.TextureGeneratorClient",
        ApiClient.VECTORIZER: "picsart_sdk.clients_image_api.VectorizerClient",
        ApiClient.SURFACEMAP: "picsart_sdk.clients_image_api.SurfacemapClient",
        ApiClient.IMAGE_TAGGING: "picsart_sdk.clients_image_api.ImageTaggingClient",
        ApiClient.IMAGE_DESCRIPTION: "picsart_sdk.clients_image_api.ImageDescriptionClient",
        ApiClient.TEXT2IMAGE: "picsart_sdk.clients_image_api.Text2ImageClient",
        ApiClient.TEXT2TEXT: "picsart_sdk.clients_image_api.Text2TextClient",
        ApiClient.INPAINTING: "picsart_sdk.clients_image_api.InpaintingClient",
        ApiClient.OUTPAINTING: "picsart_sdk.clients_image_api.OutpaintingClient",
        ApiClient.REPLACE_BACKGROUND: "picsart_sdk.clients_image_api.PaintingReplaceBackgroundClient",
        ApiClient.EXPAND: "picsart_sdk.clients_image_api.PaintingExpandClient",
        ApiClient.BLEED: "picsart_sdk.clients_image_api.BleedClient",
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

        :param client_name: The client name as defined in `ApiClient`
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
