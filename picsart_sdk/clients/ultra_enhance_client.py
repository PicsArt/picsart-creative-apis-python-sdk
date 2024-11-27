from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import PicsartImage
from picsart_sdk.clients.requests_models import UltraEnhanceRequest


class UltraEnhanceClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upscale/enhance"

    def ultra_enhance(self, request: UltraEnhanceRequest) -> ApiResponse:
        return self.post(request=request)

    def ultra_enhance_from_path(
        self, file_path: str, upscale_factor: int = 2
    ) -> ApiResponse:
        return self.ultra_enhance(
            request=UltraEnhanceRequest(
                image=PicsartImage(image_path=file_path), upscale_factor=upscale_factor
            )
        )

    def ultra_enhance_from_url(self, url: str, upscale_factor: int = 2) -> ApiResponse:
        return self.ultra_enhance(
            request=UltraEnhanceRequest(
                image=PicsartImage(image_url=url), upscale_factor=upscale_factor
            )
        )


class AsyncUltraEnhanceClient(UltraEnhanceClient):

    async def ultra_enhance(self, request: UltraEnhanceRequest) -> ApiResponse:
        return await self.async_post(request=request)

    async def ultra_enhance_from_path(
        self, file_path: str, upscale_factor: int = 2
    ) -> ApiResponse:
        return await self.ultra_enhance(
            request=UltraEnhanceRequest(
                image=PicsartImage(image_path=file_path), upscale_factor=upscale_factor
            )
        )

    async def ultra_enhance_from_url(
        self, url: str, upscale_factor: int = 2
    ) -> ApiResponse:
        return await self.ultra_enhance(
            request=UltraEnhanceRequest(
                image=PicsartImage(image_url=url), upscale_factor=upscale_factor
            )
        )
