from typing import Optional, Union

from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.api_responses.effects_response import EffectsListApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonEffectsClient(ImageBaseClient):
    @property
    def _endpoint(self):
        return "effects"

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


class EffectsClient(CommonEffectsClient):
    """
    Client for applying effects to images.

    This client provides functionality to apply a specific effect to an image
    and retrieve a list of available effects.
    """

    def effects(
        self,
        effect_name: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a specific effect to an image.

        :param effect_name: The name of the effect to apply.
        :param image_url: The URL of the image to apply the effect to.
        :param image_path: The local path of the image to apply the effect to.
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the processed image.
        """

        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return self.post(request=request)

    def get_available_effects(self) -> EffectsListApiResponse:
        """
        Retrieve the list of available effects.

        :return: The API response containing the list of available effects.
        """
        return self.get()


class AsyncEffectsClient(CommonEffectsClient):
    """
    Client for applying effects to images using the HTTP asynchronous client.

    This client provides functionality to apply a specific effect to an image
    and retrieve a list of available effects.
    """

    async def effects(
        self,
        effect_name: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a specific effect to an image using the HTTP asynchronous client.

        :param effect_name: The name of the effect to apply.
        :param image_url: The URL of the image to apply the effect to.
        :param image_path: The local path of the image to apply the effect to.
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the processed image.
        """

        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return await self.async_post(request=request)

    async def get_available_effects(self) -> EffectsListApiResponse:
        """
        Retrieve the list of available effects.

        :return: The API response containing the list of available effects.
        """
        return await self.async_get()
