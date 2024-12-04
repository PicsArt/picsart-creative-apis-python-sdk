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
    A client for the Upscale API.

    Provides methods to upscale images using the Picsart SDK.

    Attributes:
        endpoint (str): The API endpoint for upscaling.
    """

    @property
    def endpoint(self):
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
        Upscale an image.

        Args:
            image_url (str, optional): URL of the image to upscale.
            image_path (str, optional): Path to the local image file.
            upscale_factor (int): The factor by which to upscale (default: 2).
            output_format (PicsartImageFormat, optional): The desired image format.

        Returns:
            ApiResponse: The response from the upscale API.
        """
        request = UpscaleRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return self.post(request=request)


class AsyncUpscaleClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upscale"

    async def upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = UpscaleRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return await self.async_post(request=request)
