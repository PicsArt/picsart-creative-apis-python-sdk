from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage
from picsart_sdk.clients.requests_models.upscale_request import UpscaleRequest


class UpscaleClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upscale"

    def upscale(self, request: UpscaleRequest) -> ApiResponse:
        return self.post(request=request)

    def upscale_from_path(self, file_path: str, upscale_factor: int = 2) -> ApiResponse:
        return self.upscale(
            request=UpscaleRequest(
                image=PicsartImage(image_path=file_path), upscale_factor=upscale_factor
            )
        )

    def upscale_from_url(self, url: str, upscale_factor: int = 2) -> ApiResponse:
        return self.upscale(
            request=UpscaleRequest(
                image=PicsartImage(image_url=url), upscale_factor=upscale_factor
            )
        )


class AsyncUpscaleClient(UpscaleClient):

    async def upscale(self, request: UpscaleRequest) -> ApiResponse:
        return await self.async_post(request=request)

    async def upscale_from_path(
        self, file_path: str, upscale_factor: int = 2
    ) -> ApiResponse:
        return await self.upscale(
            request=UpscaleRequest(
                image=PicsartImage(image_path=file_path), upscale_factor=upscale_factor
            )
        )

    async def upscale_from_url(self, url: str, upscale_factor: int = 2) -> ApiResponse:
        return await self.upscale(
            request=UpscaleRequest(
                image=PicsartImage(image_url=url), upscale_factor=upscale_factor
            )
        )
