from picsart_sdk.api_response import ApiResponse

from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.http_client import HttpClient
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage
from picsart_sdk.clients.requests_models.upload_request import UploadRequest


class UploadClient(ImageBaseClient):

    def __init__(self, session, http_client: HttpClient = None, *args, **kwargs):

        self.session = session
        self.http_client = http_client
        if self.http_client is None:
            self.http_client = HttpClient(self)
        super(UploadClient, self).__init__(session, *args, **kwargs)

    @property
    def endpoint(self):
        return "upload"

    def set_payload(self, upload_request: UploadRequest):
        if upload_request.image.image_url is not None:
            self._payload = {
                "image_url": upload_request.image.image_url,
            }

        if upload_request.image.image_path:
            self._files = {
                "image": (
                    upload_request.image.image_path,
                    open(upload_request.image.image_path, "rb"),
                )
            }

    def upload_image(self, upload_request: UploadRequest) -> ApiResponse:
        self.set_payload(upload_request)
        return self.http_client.post()


    def upload_from_path(self, file_path: str) -> ApiResponse:
        return self.upload_image(UploadRequest(image=PicsartImage(image_path=file_path)))

    def upload_from_url(self, url: str) -> ApiResponse:
        return self.upload_image(UploadRequest(image=PicsartImage(image_url=url)))
