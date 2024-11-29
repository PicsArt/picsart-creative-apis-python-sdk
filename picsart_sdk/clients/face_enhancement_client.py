from typing import Optional

from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import PicsartImage, FaceEnhancementRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImageFormat


class FaceEnhancementClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "enhance/face"

    def face_enhancement(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = FaceEnhancementRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            format=output_format,
        )
        return self.post(request=request)


class AsyncFaceEnhancementClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "enhance/face"

    async def face_enhancement(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = FaceEnhancementRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            format=output_format,
        )
        return await self.async_post(request=request)
