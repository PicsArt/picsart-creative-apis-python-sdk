from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    AdjustRequest,
    PicsartImage,
    PicsartImageFormat,
)


class AdjustClient(ImageBaseClient):
    """
    Client for applying adjustments to images.

    This client provides functionality to adjust image properties such as brightness,
    contrast, clarity, and more. The adjustments can be applied using image URLs or
    local image paths.
    """

    @property
    def _endpoint(self):
        return "adjust"

    def adjust(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        brightness: Optional[float] = 0,
        contrast: Optional[float] = 0,
        clarity: Optional[float] = 0,
        saturation: Optional[float] = 0,
        hue: Optional[float] = 0,
        shadows: Optional[bool] = 0,
        highlights: Optional[int] = 0,
        temperature: Optional[int] = 0,
        sharpen: Optional[int] = 0,
        noise: Optional[int] = 0,
        vignette: Optional[int] = 0,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Adjust image properties.

        :param image_url: URL of the image to be adjusted. Provide only if `image_path` is not provided.
        :param image_path: Local path of the image to be adjusted. Provide only if `image_url` is not provided.
        :param brightness: Brightness adjustment level.
        :param contrast: Contrast adjustment level.
        :param clarity: Clarity adjustment level.
        :param saturation: Saturation adjustment level.
        :param hue: Hue adjustment level.
        :param shadows: Enable or disable shadows adjustment.
        :param highlights: Highlights adjustment level.
        :param temperature: Color temperature adjustment level.
        :param sharpen: Sharpening level.
        :param noise: Noise reduction level.
        :param vignette: Vignette effect level.
        :param output_format: Format of the output image.
        :return: API response containing adjustment results.
        """
        request = AdjustRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            brightness=brightness,
            contrast=contrast,
            clarity=clarity,
            saturation=saturation,
            hue=hue,
            shadows=shadows,
            highlights=highlights,
            temperature=temperature,
            sharpen=sharpen,
            noise=noise,
            vignette=vignette,
            format=output_format,
        )
        return self.post(request=request)


class AsyncAdjustClient(ImageBaseClient):
    """
    HTTP Async client for applying adjustments to images.

    This client provides asynchronous functionality to adjust image properties
    such as brightness, contrast, clarity, and more. Adjustments can be applied
    using image URLs or local image paths.
    """

    @property
    def _endpoint(self):
        return "adjust"

    async def adjust(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        brightness: Optional[float] = 0,
        contrast: Optional[float] = 0,
        clarity: Optional[float] = 0,
        saturation: Optional[float] = 0,
        hue: Optional[float] = 0,
        shadows: Optional[bool] = 0,
        highlights: Optional[int] = 0,
        temperature: Optional[int] = 0,
        sharpen: Optional[int] = 0,
        noise: Optional[int] = 0,
        vignette: Optional[int] = 0,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Adjust image properties using the HTTP asynchronous client.

        :param image_url: URL of the image to be adjusted. Provide only if `image_path` is not provided.
        :param image_path: Local path of the image to be adjusted. Provide only if `image_url` is not provided.
        :param brightness: Brightness adjustment level.
        :param contrast: Contrast adjustment level.
        :param clarity: Clarity adjustment level.
        :param saturation: Saturation adjustment level.
        :param hue: Hue adjustment level.
        :param shadows: Enable or disable shadows adjustment.
        :param highlights: Highlights adjustment level.
        :param temperature: Color temperature adjustment level.
        :param sharpen: Sharpening level.
        :param noise: Noise reduction level.
        :param vignette: Vignette effect level.
        :param output_format: Format of the output image.
        :return: API response containing adjustment results.
        """

        request = AdjustRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            brightness=brightness,
            contrast=contrast,
            clarity=clarity,
            saturation=saturation,
            hue=hue,
            shadows=shadows,
            highlights=highlights,
            temperature=temperature,
            sharpen=sharpen,
            noise=noise,
            vignette=vignette,
            format=output_format,
        )
        return await self.async_post(request=request)
