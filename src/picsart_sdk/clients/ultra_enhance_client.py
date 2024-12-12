from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import PicsartImage, UltraEnhanceRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImageFormat


class UltraEnhanceClient(ImageBaseClient):
    """
    Client for enhancing and upscaling images.

    Ultra Enhance is an advanced upscaling technique powered by a generative model designed to deliver high-frequency
    details with exceptional clarity.
    It excels on noise-free images, ensuring superior preservation of intricate details for high-quality results.
    """

    @property
    def _endpoint(self):
        return "upscale/enhance"

    def ultra_enhance(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Perform ultra enhancement and upscaling on an image.

        :param image_url: The URL of the image to enhance and upscale.
        :param image_path: The local path of the image to enhance and upscale.
        :param upscale_factor: The factor by which to upscale the image. Default is 2.
        :param output_format: The desired format for the enhanced image. Default is PNG.
        :return: The API response containing the enhanced and upscaled image.
        """
        request = UltraEnhanceRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return self.post(request=request)


class AsyncUltraEnhanceClient(ImageBaseClient):
    """
    Client for enhancing and upscaling images, using an asynchronous HTTP client.

    Ultra Enhance is an advanced upscaling technique powered by a generative model designed to deliver high-frequency
    details with exceptional clarity.
    It excels on noise-free images, ensuring superior preservation of intricate details for high-quality results.
    """

    @property
    def _endpoint(self):
        return "upscale/enhance"

    async def ultra_enhance(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Perform ultra enhancement and upscaling on an image using an asynchronous HTTP client.

        :param image_url: The URL of the image to enhance and upscale.
        :param image_path: The local path of the image to enhance and upscale.
        :param upscale_factor: The factor by which to upscale the image. Default is 2.
        :param output_format: The desired format for the enhanced image. Default is PNG.
        :return: The API response containing the enhanced and upscaled image.
        """
        request = UltraEnhanceRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return await self.async_post(request=request)
