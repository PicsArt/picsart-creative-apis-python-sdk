from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    StyleTransferRequest,
)


class CommonStyleTransfer(ImageBaseClient):

    @property
    def endpoint(self):
        return "styletransfer"

    def set_payload(self, request: StyleTransferRequest):
        super().set_payload(request)

        if request.reference_image.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault("reference_image_url", request.image.image_url)

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


class StyleTransferClient(CommonStyleTransfer):

    def style_transfer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        reference_image_url: Optional[str] = None,
        reference_image_path: Optional[str] = None,
        level: Optional[str] = "l1",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = StyleTransferRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            reference_image=PicsartImage(
                image_path=reference_image_path, image_url=reference_image_url
            ),
            level=level,
            format=output_format,
        )

        self.set_payload(request)
        return self.post(request=request)


class AsyncStyleTransferClient(CommonStyleTransfer):

    async def style_transfer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        reference_image_path: Optional[str] = None,
        reference_image_url: Optional[str] = None,
        level: Optional[str] = "l1",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        return await self.async_post(
            request=StyleTransferRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url),
                reference_image=PicsartImage(
                    image_path=reference_image_path, image_url=reference_image_url
                ),
                level=level,
                format=output_format,
            )
        )
