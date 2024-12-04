from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EditRequest,
    PicsartImage,
    PicsartImageFormat,
)


class EditClient(ImageBaseClient):

    @property
    def endpoint(self):
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

    @property
    def endpoint(self):
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
