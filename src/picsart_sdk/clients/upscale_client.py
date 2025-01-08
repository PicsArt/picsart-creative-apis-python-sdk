from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    UpscaleRequest,
)


class UpscaleClient(ImageBaseClient):
    """
    Client for upscaling images.

    This client provides functionality to upscale images by a specified factor.
    """

    @property
    def _endpoint(self):
        """The API endpoint for upscaling."""
        return "upscale"

    def upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Upscale an image by a specified factor.

        :param image_url: URL of the image to be upscaled.
        :param image_path: Local path of the image to be upscaled.
        :param upscale_factor: Factor by which to upscale the image. Default is 2.
        :param output_format: Format of the output image. Default is PNG.
        :return: API response containing the upscaled image.
        :rtype: :class:`~picsart_sdk.api_responses.ApiResponse`
        """
        request = UpscaleRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return self.post(request=request)


class AsyncUpscaleClient(ImageBaseClient):
    """
    Async HTTP client for upscaling images.

    This client provides functionality to upscale images by a specified factor.
    """

    @property
    def _endpoint(self):
        return "upscale"

    async def upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Upscale an image by a specified factor using the HTTP asynchronous client.

        :param image_url: URL of the image to be upscaled.
        :param image_path: Local path of the image to be upscaled.
        :param upscale_factor: Factor by which to upscale the image. Default is 2.
        :param output_format: Format of the output image. Default is PNG.
        :return: API response containing the upscaled image.
        :rtype: :class:`~picsart_sdk.api_responses.ApiResponse`
        """
        request = UpscaleRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return await self.async_post(request=request)
