from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage
from picsart_sdk.clients.requests_models.remove_background_request import (
    RemoveBackgroundRequest,
)


class RemoveBackgroundClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "removebg"

    def remove_background(self, request: RemoveBackgroundRequest) -> ApiResponse:
        return self.post(request=request)

    def remove_background_from_path(self, file_path: str) -> ApiResponse:
        return self.remove_background(
            RemoveBackgroundRequest(image=PicsartImage(image_path=file_path))
        )

    def remove_background_from_url(self, url: str) -> ApiResponse:
        return self.remove_background(
            RemoveBackgroundRequest(image=PicsartImage(image_url=url))
        )
