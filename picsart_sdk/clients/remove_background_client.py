from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)
from picsart_sdk.clients.requests_models.remove_background_request import (
    RemoveBackgroundOutputType,
    RemoveBackgroundRequest,
    RemoveBackgroundScale,
    RemoveBackgroundShadow,
)


class RemoveBackgroundClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "removebg"

    def remove_background(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_type: Optional[
            RemoveBackgroundOutputType
        ] = RemoveBackgroundOutputType.CUTOUT,
        bg_image: Optional[PicsartImage] = None,
        bg_color: Optional[str] = None,
        bg_width: Optional[int] = None,
        bg_height: Optional[int] = None,
        scale: Optional[RemoveBackgroundScale] = RemoveBackgroundScale.FIT,
        auto_center: Optional[bool] = False,
        stroke_size: Optional[int] = 0,
        stroke_color: Optional[str] = "FFFFFF",
        stroke_opacity: Optional[int] = 100,
        shadow: Optional[RemoveBackgroundShadow] = RemoveBackgroundShadow.DISABLED,
        shadow_opacity: Optional[int] = 20,
        shadow_blur: Optional[int] = 50,
        shadow_offset_x: Optional[int] = None,
        shadow_offset_y: Optional[int] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = RemoveBackgroundRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            output_type=output_type,
            bg_image=bg_image,
            bg_color=bg_color,
            bg_width=bg_width,
            bg_height=bg_height,
            scale=scale,
            auto_center=auto_center,
            stroke_size=stroke_size,
            stroke_color=stroke_color,
            stroke_opacity=stroke_opacity,
            shadow=shadow,
            shadow_opacity=shadow_opacity,
            shadow_blur=shadow_blur,
            shadow_offset_x=shadow_offset_x,
            shadow_offset_y=shadow_offset_y,
            format=output_format,
        )

        return self.post(request=request)


class AsyncRemoveBackgroundClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "removebg"

    async def remove_background(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_type: Optional[
            RemoveBackgroundOutputType
        ] = RemoveBackgroundOutputType.CUTOUT,
        bg_image: Optional[PicsartImage] = None,
        bg_color: Optional[str] = None,
        bg_width: Optional[int] = None,
        bg_height: Optional[int] = None,
        scale: Optional[RemoveBackgroundScale] = RemoveBackgroundScale.FIT,
        auto_center: Optional[bool] = False,
        stroke_size: Optional[int] = 0,
        stroke_color: Optional[str] = "FFFFFF",
        stroke_opacity: Optional[int] = 100,
        shadow: Optional[RemoveBackgroundShadow] = RemoveBackgroundShadow.DISABLED,
        shadow_opacity: Optional[int] = 20,
        shadow_blur: Optional[int] = 50,
        shadow_offset_x: Optional[int] = None,
        shadow_offset_y: Optional[int] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = RemoveBackgroundRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            output_type=output_type,
            bg_image=bg_image,
            bg_color=bg_color,
            bg_width=bg_width,
            bg_height=bg_height,
            scale=scale,
            auto_center=auto_center,
            stroke_size=stroke_size,
            stroke_color=stroke_color,
            stroke_opacity=stroke_opacity,
            shadow=shadow,
            shadow_opacity=shadow_opacity,
            shadow_blur=shadow_blur,
            shadow_offset_x=shadow_offset_x,
            shadow_offset_y=shadow_offset_y,
            format=output_format,
        )
        return await self.async_post(request=request)
