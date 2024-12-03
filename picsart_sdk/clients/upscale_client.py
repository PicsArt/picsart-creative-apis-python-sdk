from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    UpscaleRequest,
)


class UpscaleClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upscale"

    def upscale(
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
