from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    SurfacemapRequest,
)


class CommonSurfacemap(ImageBaseClient):

    @property
    def _endpoint(self):
        return "surfacemap"

    def set_payload(self, request: SurfacemapRequest):
        super().set_payload(request)

        if request.mask.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault("mask_url", request.mask.image_url)

        if request.mask.image_path:
            self._payload = self._payload or {}
            self._files = self._files or {}
            self._files.setdefault(
                "mask",
                (
                    request.mask.image_path,
                    open(request.mask.image_path, "rb"),
                ),
            )

        if request.sticker.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault("sticker_url", request.sticker.image_url)

        if request.sticker.image_path:
            self._payload = self._payload or {}
            self._files = self._files or {}
            self._files.setdefault(
                "sticker",
                (
                    request.sticker.image_path,
                    open(request.sticker.image_path, "rb"),
                ),
            )

        self._payload.update(request.get_dict())


class SurfacemapClient(CommonSurfacemap):
    """
    Client for applying surfacemap effects to images.

    The Surface Map tool allows you to seamlessly 'print' a sticker onto a target image.
    By utilizing a mask, the tool maps the sticker's pixels onto the texture and contours of the target image,
    creating a realistic and dynamic print-preview effect.
    """

    def surfacemap(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        sticker_url: Optional[str] = None,
        sticker_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a surfacemap effect to an image.

        :param image_url: The URL of the target image to apply the effect to.
        :param image_path: The local path of the target image to apply the effect to.
        :param mask_url: The URL of the mask image defining the area for the effect.
        :param mask_path: The local path of the mask image defining the area for the effect.
        :param sticker_url: The URL of the sticker to be applied as part of the effect.
        :param sticker_path: The local path of the sticker to be applied as part of the effect.
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the image with the applied surfacemap effect.
        """

        request = SurfacemapRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            mask=PicsartImage(image_path=mask_path, image_url=mask_url),
            sticker=PicsartImage(image_path=sticker_path, image_url=sticker_url),
            format=output_format,
        )

        return self.post(request=request)


class AsyncSurfacemapClient(CommonSurfacemap):
    """
    Client for applying surfacemap effects to images, using an asynchronous HTTP client.

    The Surface Map tool allows you to seamlessly 'print' a sticker onto a target image.
    By utilizing a mask, the tool maps the sticker's pixels onto the texture and contours of the target image,
    creating a realistic and dynamic print-preview effect.
    """

    async def surfacemap(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        sticker_url: Optional[str] = None,
        sticker_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Apply a surfacemap effect to an image, using an asynchronous HTTP client.

        :param image_url: The URL of the target image to apply the effect to.
        :param image_path: The local path of the target image to apply the effect to.
        :param mask_url: The URL of the mask image defining the area for the effect.
        :param mask_path: The local path of the mask image defining the area for the effect.
        :param sticker_url: The URL of the sticker to be applied as part of the effect.
        :param sticker_path: The local path of the sticker to be applied as part of the effect.
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the image with the applied surfacemap effect.
        """
        request = SurfacemapRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            mask=PicsartImage(image_path=mask_path, image_url=mask_url),
            sticker=PicsartImage(image_path=sticker_path, image_url=sticker_url),
            format=output_format,
        )

        return await self.async_post(request=request)
