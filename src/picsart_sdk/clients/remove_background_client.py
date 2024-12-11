from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)
from picsart_sdk.clients.requests_models.remove_background_request import (
    RemoveBackgroundOutputType,
    RemoveBackgroundRequest,
    RemoveBackgroundScale,
    RemoveBackgroundShadow,
)


class RemoveBackgroundClient(ImageBaseClient):
    """
    Client for removing the background of an image.

    This client provides functionality to remove the background of an image
    and optionally replace it with a color, another image, or apply additional
    effects such as strokes or shadows.
    """

    @property
    def _endpoint(self):
        return "removebg"

    def remove_background(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_type: Optional[
            RemoveBackgroundOutputType
        ] = RemoveBackgroundOutputType.CUTOUT,
        bg_image: Optional[PicsartImage] = None,
        bg_color: Optional[str] = None,
        bg_width: Optional[int] = None,
        bg_height: Optional[int] = None,
        scale: Optional[RemoveBackgroundScale] = RemoveBackgroundScale.FIT,
        auto_center: Optional[bool] = False,
        stroke_size: Optional[int] = 0,
        stroke_color: Optional[str] = "FFFFFF",
        stroke_opacity: Optional[int] = 100,
        shadow: Optional[RemoveBackgroundShadow] = RemoveBackgroundShadow.DISABLED,
        shadow_opacity: Optional[int] = 20,
        shadow_blur: Optional[int] = 50,
        shadow_offset_x: Optional[int] = None,
        shadow_offset_y: Optional[int] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Remove or modify the background of an image.

        :param image_url: The URL of the image to process.
        :param image_path: The local path of the image to process.
        :param output_type: The type of output (e.g., cutout, transparent).
        :param bg_image: An optional background image to use as a replacement.
        :param bg_color: An optional background color in hex format (e.g., "FFFFFF").
        :param bg_width: The width of the background image if replacing the background.
        :param bg_height: The height of the background image if replacing the background.
        :param scale: The scaling option for the background (e.g., fit, fill).
        :param auto_center: Whether to center the image automatically on the background.
        :param stroke_size: The size of the stroke around the image.
        :param stroke_color: The color of the stroke around the image in hex format.
        :param stroke_opacity: The opacity of the stroke (0 to 100).
        :param shadow: The shadow effect to apply (enabled or disabled).
        :param shadow_opacity: The opacity of the shadow (0 to 100).
        :param shadow_blur: The blur amount for the shadow.
        :param shadow_offset_x: The horizontal offset for the shadow.
        :param shadow_offset_y: The vertical offset for the shadow.
        :param output_format: The desired output format for the processed image. Default is PNG.
        :return: The API response containing the processed image.
        """

        request = RemoveBackgroundRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            output_type=output_type,
            bg_image=bg_image,
            bg_color=bg_color,
            bg_width=bg_width,
            bg_height=bg_height,
            scale=scale,
            auto_center=auto_center,
            stroke_size=stroke_size,
            stroke_color=stroke_color,
            stroke_opacity=stroke_opacity,
            shadow=shadow,
            shadow_opacity=shadow_opacity,
            shadow_blur=shadow_blur,
            shadow_offset_x=shadow_offset_x,
            shadow_offset_y=shadow_offset_y,
            format=output_format,
        )

        return self.post(request=request)


class AsyncRemoveBackgroundClient(ImageBaseClient):
    """
    Client for removing the background of an image, using the HTTP asynchronous client.

    This client provides functionality to remove the background of an image
    and optionally replace it with a color, another image, or apply additional
    effects such as strokes or shadows.
    """

    @property
    def _endpoint(self):
        return "removebg"

    async def remove_background(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_type: Optional[
            RemoveBackgroundOutputType
        ] = RemoveBackgroundOutputType.CUTOUT,
        bg_image: Optional[PicsartImage] = None,
        bg_color: Optional[str] = None,
        bg_width: Optional[int] = None,
        bg_height: Optional[int] = None,
        scale: Optional[RemoveBackgroundScale] = RemoveBackgroundScale.FIT,
        auto_center: Optional[bool] = False,
        stroke_size: Optional[int] = 0,
        stroke_color: Optional[str] = "FFFFFF",
        stroke_opacity: Optional[int] = 100,
        shadow: Optional[RemoveBackgroundShadow] = RemoveBackgroundShadow.DISABLED,
        shadow_opacity: Optional[int] = 20,
        shadow_blur: Optional[int] = 50,
        shadow_offset_x: Optional[int] = None,
        shadow_offset_y: Optional[int] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Remove or modify the background of an image.

        :param image_url: The URL of the image to process.
        :param image_path: The local path of the image to process.
        :param output_type: The type of output (e.g., cutout, transparent).
        :param bg_image: An optional background image to use as a replacement.
        :param bg_color: An optional background color in hex format (e.g., "FFFFFF").
        :param bg_width: The width of the background image if replacing the background.
        :param bg_height: The height of the background image if replacing the background.
        :param scale: The scaling option for the background (e.g., fit, fill).
        :param auto_center: Whether to center the image automatically on the background.
        :param stroke_size: The size of the stroke around the image.
        :param stroke_color: The color of the stroke around the image in hex format.
        :param stroke_opacity: The opacity of the stroke (0 to 100).
        :param shadow: The shadow effect to apply (enabled or disabled).
        :param shadow_opacity: The opacity of the shadow (0 to 100).
        :param shadow_blur: The blur amount for the shadow.
        :param shadow_offset_x: The horizontal offset for the shadow.
        :param shadow_offset_y: The vertical offset for the shadow.
        :param output_format: The desired output format for the processed image. Default is PNG.
        :return: The API response containing the processed image.
        """

        request = RemoveBackgroundRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            output_type=output_type,
            bg_image=bg_image,
            bg_color=bg_color,
            bg_width=bg_width,
            bg_height=bg_height,
            scale=scale,
            auto_center=auto_center,
            stroke_size=stroke_size,
            stroke_color=stroke_color,
            stroke_opacity=stroke_opacity,
            shadow=shadow,
            shadow_opacity=shadow_opacity,
            shadow_blur=shadow_blur,
            shadow_offset_x=shadow_offset_x,
            shadow_offset_y=shadow_offset_y,
            format=output_format,
        )
        return await self.async_post(request=request)
