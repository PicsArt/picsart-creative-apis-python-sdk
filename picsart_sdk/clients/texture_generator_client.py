from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    TextureGeneratorRequest,
)


class TextureGeneratorClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "background/texture"

    def texture_generator(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        offset_x: Optional[int] = 0,
        offset_y: Optional[int] = 0,
        pattern: Optional[str] = "hex",
        rotate: Optional[int] = 0,
        scale: Optional[float] = 1,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = TextureGeneratorRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            width=width,
            height=height,
            offset_x=offset_x,
            offset_y=offset_y,
            pattern=pattern,
            rotate=rotate,
            scale=scale,
            format=output_format,
        )
        return self.post(request=request)


class AsyncTextureGeneratorClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "background/texture"

    async def texture_generator(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        offset_x: Optional[int] = 0,
        offset_y: Optional[int] = 0,
        pattern: Optional[str] = "hex",
        rotate: Optional[int] = 0,
        scale: Optional[float] = 1,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = TextureGeneratorRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            width=width,
            height=height,
            offset_x=offset_x,
            offset_y=offset_y,
            pattern=pattern,
            rotate=rotate,
            scale=scale,
            format=output_format,
        )
        return await self.async_post(request=request)
