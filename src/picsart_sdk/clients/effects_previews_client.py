from typing import Optional

from picsart_sdk.api_responses.effects_response import (
    EffectsPreviewsApiResponse,
    EffectsPreviewsApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsPreviewsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonEffectsPreviewsClient(ImageBaseClient):

    @property
    def _endpoint(self):
        return "effects/previews"

    def parse_response(
        self, result: dict, request_method: str
    ) -> EffectsPreviewsApiResponse:

        return EffectsPreviewsApiResponse(
            status=result.get("status"),
            data=[
                EffectsPreviewsApiResponseData(
                    id=item.get("id"),
                    url=item.get("url"),
                    effect_name=item.get("effect_name"),
                )
                for item in result.get("data", [])
            ],
        )


class EffectsPreviewsClient(CommonEffectsPreviewsClient):
    """
    Client for generating previews of effects on images.

    The effects previews service applies an effect to a given input image and returns a preview
    (i.e., thumbnail) of the effect.
    """

    def effects_previews(
        self,
        effect_names: list[str],
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> EffectsPreviewsApiResponse:
        """
        Generate previews for multiple effects applied to an image.

        :param effect_names: A list of effect names to apply.
        :param image_url: The URL of the image to generate effect previews for.
        :param image_path: The local path of the image to generate effect previews for.
        :param preview_size: The size of the effect previews. Default is 120.
        :param output_format: The desired output format for the preview images. Default is PNG.
        :return: The API response containing the effect previews.
        """

        request = EffectsPreviewsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_names=effect_names,
            preview_size=preview_size,
            format=output_format,
        )
        return self.post(request=request)


class AsyncEffectsPreviewsClient(CommonEffectsPreviewsClient):
    """
    HTTP Async client for generating previews of effects on images.

    The effects previews service applies an effect to a given input image and returns a preview
    (i.e., thumbnail) of the effect.
    """

    @property
    def _endpoint(self):
        return "effects/previews"

    async def effects_previews(
        self,
        effect_names: list[str],
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> EffectsPreviewsApiResponse:
        """
        Generate previews for multiple effects applied to an image using the HTTP asynchronous client.

        :param effect_names: A list of effect names to apply.
        :param image_url: The URL of the image to generate effect previews for.
        :param image_path: The local path of the image to generate effect previews for.
        :param preview_size: The size of the effect previews. Default is 120.
        :param output_format: The desired output format for the preview images. Default is PNG.
        :return: The API response containing the effect previews.
        """
        request = EffectsPreviewsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_names=effect_names,
            preview_size=preview_size,
            format=output_format,
        )
        return await self.async_post(request=request)
