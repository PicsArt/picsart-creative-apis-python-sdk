from picsart_sdk.api_response import ApiResponse

from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage
from picsart_sdk.clients.requests_models.upload_request import UploadRequest


class UploadClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "upload"

    def upload_image(self, request: UploadRequest) -> ApiResponse:
        self.set_payload(request)
        return self.session.http_client.post(
            url=self.post_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
        )

    def upload_from_path(self, file_path: str) -> ApiResponse:
        return self.upload_image(
            UploadRequest(image=PicsartImage(image_path=file_path))
        )

    def upload_from_url(self, url: str) -> ApiResponse:
        return self.upload_image(UploadRequest(image=PicsartImage(image_url=url)))
