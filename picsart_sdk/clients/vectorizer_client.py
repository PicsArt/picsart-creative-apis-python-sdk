from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    VectorizerRequest,
)


class VectorizerClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "vectorizer"

    def vectorizer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        downscale_to: Optional[int] = 2048,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = VectorizerRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            downscale_to=downscale_to,
            format=output_format,
        )
        return self.post(request=request)


class AsyncVectorizerClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "vectorizer"

    async def vectorizer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        downscale_to: Optional[int] = 2048,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = VectorizerRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            downscale_to=downscale_to,
            format=output_format,
        )
        return await self.async_post(request=request)
