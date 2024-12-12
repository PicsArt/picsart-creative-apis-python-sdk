from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    MasksRequest,
    PicsartImage,
    PicsartImageFormat,
)


class MasksClient(ImageBaseClient):
    """
    Client for applying a mask to an image.

    This client provides functionality to overlay masks on images with
    customizable blending, opacity, mask flip, and hue adjustments.
    """

    @property
    def _endpoint(self):
        return "masks"

    def masks(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[str] = "lace1",
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a mask to an image with customizable blending, opacity, hue, etc.

        :param image_url: The URL of the image to apply the mask to.
        :param image_path: The local path of the image to apply the mask to.
        :param blend: The blending mode for the mask (e.g., "screen").
        :param mask: The type of mask to apply (e.g., "lace1").
        :param opacity: The opacity of the mask (0 to 100). Default is 100.
        :param hue: The hue adjustment for the mask. Default is 0.
        :param mask_flip: The flip mode for the mask (e.g., "horizontal").
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the masked image.
        """

        request = MasksRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=mask,
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            format=output_format,
        )
        return self.post(request=request)


class AsyncMasksClient(ImageBaseClient):
    """
    Client for applying a mask to an image using the HTTP asynchronous client.

    This client provides functionality to overlay masks on images with
    customizable blending, opacity, mask flip, and hue adjustments.
    """

    @property
    def _endpoint(self):
        return "masks"

    async def masks(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[str] = "lace1",
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a mask to an image with customizable blending, opacity, hue, etc., using the asynchronous HTTP client.

        :param image_url: The URL of the image to apply the mask to.
        :param image_path: The local path of the image to apply the mask to.
        :param blend: The blending mode for the mask (e.g., "screen").
        :param mask: The type of mask to apply (e.g., "lace1").
        :param opacity: The opacity of the mask (0 to 100). Default is 100.
        :param hue: The hue adjustment for the mask. Default is 0.
        :param mask_flip: The flip mode for the mask (e.g., "horizontal").
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the masked image.
        """
        request = MasksRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=mask,
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            format=output_format,
        )
        return await self.async_post(request=request)
