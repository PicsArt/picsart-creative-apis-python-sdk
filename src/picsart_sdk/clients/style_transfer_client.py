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
    def _endpoint(self):
        return "styletransfer"

    def set_payload(self, request: StyleTransferRequest):
        super().set_payload(request)

        if request.reference_image.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault(
                "reference_image_url", request.reference_image.image_url
            )
            if isinstance(self._files, dict):
                self._files.pop("reference_image", None)

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
            self._payload.pop("reference_image_url", None)

        self._payload.update(request.get_dict())


class StyleTransferClient(CommonStyleTransfer):
    """
    Client for performing style transfer on images.

    The style transfer tool transfers a style from a reference image to a content image.
    The smart algorithm blends the two images, so the output looks like the content image,
    but "painted" in the style of the reference image.
    """

    def style_transfer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        reference_image_url: Optional[str] = None,
        reference_image_path: Optional[str] = None,
        level: Optional[str] = "l1",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a style transfer from a reference image to a target image

        :param image_url: The URL of the target image to which the style will be applied.
        :param image_path: The local path of the target image to which the style will be applied.
        :param reference_image_url: The URL of the reference image providing the style.
        :param reference_image_path: The local path of the reference image providing the style.
        :param level: The intensity level of the style transfer (e.g., "l1" for level 1). Default is "l1".
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the styled image.
        """

        request = StyleTransferRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            reference_image=PicsartImage(
                image_path=reference_image_path,
                image_url=reference_image_url,
                _field_name="reference_image",
            ),
            level=level,
            format=output_format,
        )

        return self.post(request=request)


class AsyncStyleTransferClient(CommonStyleTransfer):
    """
    Client for performing style transfer on images, using an asynchronous HTTP client.

    The style transfer tool transfers a style from a reference image to a content image.
    The smart algorithm blends the two images, so the output looks like the content image,
    but "painted" in the style of the reference image.
    """

    async def style_transfer(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        reference_image_path: Optional[str] = None,
        reference_image_url: Optional[str] = None,
        level: Optional[str] = "l1",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a style transfer from a reference image to a target image using an asynchronous HTTP client.

        :param image_url: The URL of the target image to which the style will be applied.
        :param image_path: The local path of the target image to which the style will be applied.
        :param reference_image_url: The URL of the reference image providing the style.
        :param reference_image_path: The local path of the reference image providing the style.
        :param level: The intensity level of the style transfer (e.g., "l1" for level 1). Default is "l1".
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the styled image.
        """

        request = StyleTransferRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            reference_image=PicsartImage(
                image_path=reference_image_path,
                image_url=reference_image_url,
                _field_name="reference_image",
            ),
            level=level,
            format=output_format,
        )

        return await self.async_post(request=request)
