from dataclasses import asdict, fields
from enum import Enum

from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.remove_background_request import (
    RemoveBackgroundRequest,
)


class RemoveBackgroundClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "removebg"

    def remove_background(self, request: RemoveBackgroundRequest) -> ApiResponse:
        self.set_payload(request)
        return self.session.http_client.post(
            url=self.post_url,
            data=self._payload,
            files=self._files,
            headers=self.headers,
        )

    def set_payload(self, request: RemoveBackgroundRequest):
        super().set_payload(request)
        self._payload.update(request.get_dict())
