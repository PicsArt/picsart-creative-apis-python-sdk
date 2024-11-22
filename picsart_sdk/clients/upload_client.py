from picsart_sdk.api_response import ApiResponse, ApiResponseData

from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage
from picsart_sdk.clients.requests_models.upload_request import UploadRequest


class UploadClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upload"

    def upload_image(self, request: UploadRequest) -> ApiResponse:
        return self.post(request=request)

    def upload_from_path(self, file_path: str) -> ApiResponse:
        return self.upload_image(
            UploadRequest(image=PicsartImage(image_path=file_path))
        )

    def upload_from_url(self, url: str) -> ApiResponse:
        return self.upload_image(UploadRequest(image=PicsartImage(image_url=url)))
