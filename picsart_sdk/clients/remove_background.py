from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient


class RemoveBackgroundClient(ImageBaseClient):

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(RemoveBackgroundClient, self).__init__(session, *args, **kwargs)

    @property
    def endpoint(self):
        return "/upload"

    def upload_image(self, file_path, *args, **kwargs) -> ApiResponse:
        print("Uploading file {}".format(file_path))

    def upload_image_from_url(self, url, *args, **kwargs) -> ApiResponse:
        print("Uploading file from url {}".format(url))
