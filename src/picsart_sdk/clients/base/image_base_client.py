from abc import ABC

from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.settings import PICSART_IMAGE_API_VERSION


class ImageBaseClient(BaseClient, ABC):

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(ImageBaseClient, self).__init__(session, *args, **kwargs)

    @property
    def base_url(self):
        return "https://api.picsart.io/tools"

    @property
    def version(self):
        return self._version or PICSART_IMAGE_API_VERSION

    def set_payload(self, request):
        """
        Set the payload for the API HTTP request.

        :param request: A dataclass implementing `BaseRequest`
        """
        if request.image.image_url is not None:
            self._payload = self._payload or {}
            if isinstance(self._files, dict):
                self._files.pop("image", None)
            self._payload.setdefault("image_url", request.image.image_url)

        if request.image.image_path:
            self._payload = self._payload or {}
            self._files = self._files or {}
            self._files.setdefault(
                "image",
                (
                    request.image.image_path,
                    open(request.image.image_path, "rb"),
                ),
            )
            self._payload.pop("image_url", None)

        self._payload.update(request.get_dict())

    def parse_response(self, result: dict, request_method: str) -> ApiResponse:
        """
        Parse the response from the Picsart API.
        :param result: The JSON object returned by the Picsart API
        :param request_method: The HTTP method used to send the request
        :return: The ApiResponse object
        """
        data = result["data"] if "data" in result else None
        return ApiResponse(
            status=result["status"],
            data=ApiResponseData(url=data["url"], id=data["id"]) if data else None,
            # in the response from the API, the key name is called `transaction_id`
            inference_id=result.get("transaction_id"),
        )
