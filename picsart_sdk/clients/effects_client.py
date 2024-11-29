from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage
from picsart_sdk.clients.requests_models.ultra_upscale_request import (
    UltraUpscaleRequest,
    UltraUpscaleMode,
)


class EffectsClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upscale/ultra"

    def ultra_upscale(self, request: UltraUpscaleRequest) -> ApiResponse:
        return self.post(request=request)

    def ultra_upscale_from_path(
        self, file_path: str, upscale_factor: int = 2, mode=UltraUpscaleMode.SYNC
    ) -> ApiResponse:
        return self.ultra_upscale(
            request=UltraUpscaleRequest(
                image=PicsartImage(image_path=file_path),
                upscale_factor=upscale_factor,
                mode=mode,
            )
        )

    def ultra_upscale_from_url(
        self, url: str, upscale_factor: int = 2, mode=UltraUpscaleMode.SYNC
    ) -> ApiResponse:
        return self.ultra_upscale(
            request=UltraUpscaleRequest(
                image=PicsartImage(image_url=url),
                upscale_factor=upscale_factor,
                mode=mode,
            )
        )

    def get_result(self, transaction_id: str) -> ApiResponse:
        return self.get(postfix_url=transaction_id)


class AsyncUltraUpscaleClient(UltraUpscaleClient):

    async def ultra_upscale(self, request: UltraUpscaleRequest) -> ApiResponse:
        return await self.async_post(request=request)

    async def ultra_upscale_from_path(
        self, file_path: str, upscale_factor: int = 2, mode=UltraUpscaleMode.SYNC
    ) -> ApiResponse:
        return await self.ultra_upscale(
            request=UltraUpscaleRequest(
                image=PicsartImage(image_path=file_path),
                upscale_factor=upscale_factor,
                mode=mode,
            )
        )

    async def ultra_upscale_from_url(
        self, url: str, upscale_factor: int = 2, mode=UltraUpscaleMode.SYNC
    ) -> ApiResponse:
        return await self.ultra_upscale(
            request=UltraUpscaleRequest(
                image=PicsartImage(image_url=url),
                upscale_factor=upscale_factor,
                mode=mode,
            )
        )

    async def get_result(self, transaction_id: str):
        return await self.async_get(postfix_url=transaction_id)
