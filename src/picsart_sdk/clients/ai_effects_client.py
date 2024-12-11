from typing import Optional, Union

from picsart_sdk.api_responses import (
    ApiResponse,
    ApiResponseData,
    EffectsListApiResponse,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonAiEffects(ImageBaseClient):
    @property
    def _endpoint(self):
        return "effects/ai"

    def parse_response(
        self, result: dict, request_method: str
    ) -> Union[EffectsListApiResponse, ApiResponse]:
        if request_method == "GET":
            return EffectsListApiResponse(
                effects=[item.get("name") for item in result.get("data", [])]
            )
        return ApiResponse(
            status=result.get("status"), data=ApiResponseData(**result.get("data", {}))
        )


class AiEffectsClient(CommonAiEffects):
    """
    Client for applying AI effects to images.

    This client provides methods to apply specific AI effects to images
    and retrieve the list of available AI effects.
    """

    def ai_effects(
        self,
        effect_name: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a specific AI effect to an image.

        :param effect_name: Name of the AI effect to apply.
        :param image_url: URL of the image to which the effect will be applied.
        :param image_path: Local path of the image to which the effect will be applied.
        :param output_format: Format of the output image. Default is PNG.
        :return: API response containing the processed image.
        :rtype: :class:`~picsart_sdk.api_responses.ApiResponse`
        """
        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return self.post(request=request)

    def get_available_ai_effects(self) -> EffectsListApiResponse:
        """
        Retrieve the list of available AI effects.

        :return: List of available AI effects.
        :rtype: EffectsListApiResponse
        """
        return self.get()


class AsyncAiEffectsClient(CommonAiEffects):
    """
    Async HTTP client for applying AI effects to images.

    This client provides methods to apply specific AI effects to images
    and retrieve the list of available AI effects.
    """

    async def ai_effects(
        self,
        effect_name: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a specific AI effect to an image using the HTTP asynchronous client.

        :param effect_name: Name of the AI effect to apply.
        :param image_url: URL of the image to which the effect will be applied.
        :param image_path: Local path of the image to which the effect will be applied.
        :param output_format: Format of the output image. Default is PNG.
        :return: API response containing the processed image.
        :rtype: :class:`~picsart_sdk.api_responses.ApiResponse`
        """
        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return await self.async_post(request=request)

    async def get_available_ai_effects(self) -> EffectsListApiResponse:
        """
        Retrieve the list of available AI effects using the HTTP asynchronous client.

        :return: List of available AI effects.
        :rtype: EffectsListApiResponse
        """
        return await self.async_get()
