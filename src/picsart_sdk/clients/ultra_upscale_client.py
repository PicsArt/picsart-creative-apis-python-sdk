from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)
from picsart_sdk.clients.requests_models.ultra_upscale_request import (
    UltraUpscaleMode,
    UltraUpscaleRequest,
)


class UltraUpscaleClient(ImageBaseClient):
    """
    Client for ultra upscaling images.

    Upscale Ultra is an advanced upscaling technique that combines noise suppression with predictive and
    generative AI technology to deliver exceptional results.
    This method excels at enhancing images with faces, low-resolution photos, stickers, and objects featuring
    geometric shapes and clear edges. By intelligently 'completing' missing pixels, Upscale Ultra significantly
    improves image quality and resolution, achieving a best-in-class smoothing and enhancement effect.
    It is particularly effective for small-resolution images containing faces, ensuring outstanding detail and clarity.
    """

    @property
    def _endpoint(self):
        return "upscale/ultra"

    def ultra_upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[UltraUpscaleMode] = UltraUpscaleMode.SYNC,
    ) -> ApiResponse:
        """
        Perform ultra upscaling on an image.

        :param image_url: The URL of the image to upscale.
        :param image_path: The local path of the image to upscale.
        :param upscale_factor: The factor by which to upscale the image. Default is 2.
        :param output_format: The desired format for the upscaled image. Default is PNG.
        :param mode: The mode of operation (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the upscaled image.
        """
        request = UltraUpscaleRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            format=output_format,
            mode=mode,
        )
        return self.post(request=request)

    def get_result(self, transaction_id: str) -> ApiResponse:
        """
        Retrieve the result of an ultra upscaling operation using its transaction ID.

        :param transaction_id: The unique identifier for the upscaling operation.
        :return: The API response containing the upscaled image result.
        """
        return self.get(postfix_url=transaction_id)


class AsyncUltraUpscaleClient(ImageBaseClient):
    """
    Client for ultra upscaling images using an asynchronous HTTP client.

    Upscale Ultra is an advanced upscaling technique that combines noise suppression with predictive and
    generative AI technology to deliver exceptional results.
    This method excels at enhancing images with faces, low-resolution photos, stickers, and objects featuring
    geometric shapes and clear edges. By intelligently 'completing' missing pixels, Upscale Ultra significantly
    improves image quality and resolution, achieving a best-in-class smoothing and enhancement effect.
    It is particularly effective for small-resolution images containing faces, ensuring outstanding detail and clarity.
    """

    @property
    def _endpoint(self):
        return "upscale/ultra"

    async def ultra_upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[UltraUpscaleMode] = UltraUpscaleMode.SYNC,
    ) -> ApiResponse:
        """
        Perform ultra upscaling on an image using an asynchronous HTTP client.

        :param image_url: The URL of the image to upscale.
        :param image_path: The local path of the image to upscale.
        :param upscale_factor: The factor by which to upscale the image. Default is 2.
        :param output_format: The desired format for the upscaled image. Default is PNG.
        :param mode: The mode of operation (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the upscaled image.
        """
        request = UltraUpscaleRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            mode=mode,
            format=output_format,
        )
        return await self.async_post(request=request)

    async def get_result(self, transaction_id: str):
        """
        Retrieve the result of an ultra upscaling operation using its transaction ID, using an asynchronous HTTP client.

        :param transaction_id: The unique identifier for the upscaling operation.
        :return: The API response containing the upscaled image result.
        """
        return await self.async_get(postfix_url=transaction_id)
