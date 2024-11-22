from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.remove_background_request import (
    RemoveBackgroundRequest,
)


class RemoveBackgroundClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "/upload"

    def remove_background(self, request: RemoveBackgroundRequest) -> ApiResponse:
        self.set_payload(request)
        return self.http_client.post()

    def set_payload(self, request):
        pass
