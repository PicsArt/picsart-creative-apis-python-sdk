from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import UploadRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage


class UploadClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upload"

    def upload_image(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ApiResponse:
        request = UploadRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url)
        )
        return self.post(request=request)


class AsyncUploadClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upload"

    async def upload_image(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ApiResponse:
        request = UploadRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url)
        )
        return await self.async_post(request=request)
