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

    @property
    def endpoint(self):
        return "upscale/ultra"

    def ultra_upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[UltraUpscaleMode] = UltraUpscaleMode.SYNC,
    ) -> ApiResponse:
        request = UltraUpscaleRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            format=output_format,
            mode=mode,
        )
        return self.post(request=request)

    def get_result(self, transaction_id: str) -> ApiResponse:
        return self.get(postfix_url=transaction_id)


class AsyncUltraUpscaleClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "upscale/ultra"

    async def ultra_upscale(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        upscale_factor: int = 2,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[UltraUpscaleMode] = UltraUpscaleMode.SYNC,
    ) -> ApiResponse:
        request = UltraUpscaleRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            upscale_factor=upscale_factor,
            mode=mode,
            format=output_format,
        )
        return await self.async_post(request=request)

    async def get_result(self, transaction_id: str):
        return await self.async_get(postfix_url=transaction_id)
