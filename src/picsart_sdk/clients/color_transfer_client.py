from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    ColorTransferRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonColorTransfer(ImageBaseClient):

    @property
    def _endpoint(self):
        return "color-transfer"

    def set_payload(self, request: ColorTransferRequest):
        super().set_payload(request)

        if request.reference_image.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault(
                "reference_image_url", request.reference_image.image_url
            )

        if request.reference_image.image_path:
            self._payload = self._payload or {}
            self._files = self._files or {}
            self._files.setdefault(
                "reference_image",
                (
                    request.reference_image.image_path,
                    open(request.reference_image.image_path, "rb"),
                ),
            )

        self._payload.update(request.get_dict())


class ColorTransferClient(CommonColorTransfer):

    def color_transfer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        reference_image_url: Optional[str] = None,
        reference_image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = ColorTransferRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            reference_image=PicsartImage(
                image_path=reference_image_path, image_url=reference_image_url
            ),
            format=output_format,
        )

        return self.post(request=request)


class AsyncColorTransferClient(CommonColorTransfer):

    async def color_transfer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        reference_image_path: Optional[str] = None,
        reference_image_url: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = ColorTransferRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            reference_image=PicsartImage(
                image_path=reference_image_path, image_url=reference_image_url
            ),
            format=output_format,
        )

        return await self.async_post(request=request)
