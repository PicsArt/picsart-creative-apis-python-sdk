from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EditRequest,
    PicsartImage,
    PicsartImageFormat,
)


class EditClient(ImageBaseClient):
    """
    Client for editing images.
    Refer to the `API documentation <https://docs.picsart.io/reference/image-edit>`_ for more details on each transformation.

    This client provides functionality to apply various editing operations to images,
    such as resizing, rotating, flipping, and adjusting perspective.
    """

    @property
    def _endpoint(self):
        return "edit"

    def edit(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mode: Optional[str] = None,
        size: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        flip: Optional[str] = None,
        rotate: Optional[int] = 0,
        perspective_horizontal: Optional[int] = 0,
        perspective_vertical: Optional[int] = 0,
        quality: Optional[int] = 90,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Edit an image by applying various transformations.

        :param image_url: The URL of the image to be edited.
        :param image_path: The local path of the image to be edited.
        :param mode: The editing mode to be applied.
        :param size: The size to which the image should be resized.
        :param width: The width to which the image should be resized.
        :param height: The height to which the image should be resized.
        :param flip: The flipping mode (e.g., "horizontal" or "vertical").
        :param rotate: The degree to rotate the image. Default is 0.
        :param perspective_horizontal: The horizontal perspective adjustment value. Default is 0.
        :param perspective_vertical: The vertical perspective adjustment value. Default is 0.
        :param quality: The quality of the output image. Default is 90.
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the edited image.
        """
        request = EditRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            mode=mode,
            size=size,
            width=width,
            height=height,
            flip=flip,
            rotate=rotate,
            perspective_horizontal=perspective_horizontal,
            perspective_vertical=perspective_vertical,
            quality=quality,
            format=output_format,
        )
        return self.post(request=request)


class AsyncEditClient(ImageBaseClient):
    """
    Client for editing images using the HTTP asynchronous client.
    Refer to the `API documentation <https://docs.picsart.io/reference/image-edit>`_ for more details on each transformation.

    This client provides functionality to apply various editing operations to images,
    such as resizing, rotating, flipping, and adjusting perspective.
    """

    @property
    def _endpoint(self):
        return "edit"

    async def edit(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mode: Optional[str] = None,
        size: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        flip: Optional[str] = None,
        rotate: Optional[int] = 0,
        perspective_horizontal: Optional[int] = 0,
        perspective_vertical: Optional[int] = 0,
        quality: Optional[int] = 90,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Edit an image by applying various transformations using an HTTP asynchronous client.

        :param image_url: The URL of the image to be edited.
        :param image_path: The local path of the image to be edited.
        :param mode: The editing mode to be applied.
        :param size: The size to which the image should be resized.
        :param width: The width to which the image should be resized.
        :param height: The height to which the image should be resized.
        :param flip: The flipping mode (e.g., "horizontal" or "vertical").
        :param rotate: The degree to rotate the image. Default is 0.
        :param perspective_horizontal: The horizontal perspective adjustment value. Default is 0.
        :param perspective_vertical: The vertical perspective adjustment value. Default is 0.
        :param quality: The quality of the output image. Default is 90.
        :param output_format: The desired format for the output image. Default is PNG.
        :return: The API response containing the edited image.
        """

        request = EditRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            mode=mode,
            size=size,
            width=width,
            height=height,
            flip=flip,
            rotate=rotate,
            perspective_horizontal=perspective_horizontal,
            perspective_vertical=perspective_vertical,
            quality=quality,
            format=output_format,
        )
        return await self.async_post(request=request)
