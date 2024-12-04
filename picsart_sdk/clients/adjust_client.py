from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    AdjustRequest,
    PicsartImage,
    PicsartImageFormat,
)


class AdjustClient(ImageBaseClient):

    @property
    def endpoint(self):
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

    @property
    def endpoint(self):
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
