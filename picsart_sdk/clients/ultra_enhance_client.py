from typing import Optional

from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import PicsartImage
from picsart_sdk.clients.requests_models import UltraEnhanceRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImageFormat


class UltraEnhanceClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upscale/enhance"

    def ultra_enhance(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = UltraEnhanceRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return self.post(request=request)


class AsyncUltraEnhanceClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "upscale/enhance"

    async def ultra_enhance(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = UltraEnhanceRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            format=output_format,
        )
        return await self.async_post(request=request)
