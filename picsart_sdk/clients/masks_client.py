from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    MasksRequest,
    PicsartImage,
    PicsartImageFormat,
)


class MasksClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "masks"

    def masks(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[str] = "lace1",
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = MasksRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=mask,
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            format=output_format,
        )
        return self.post(request=request)


class AsyncMasksClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "masks"

    async def masks(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[str] = "lace1",
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = MasksRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=mask,
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            format=output_format,
        )
        return await self.async_post(request=request)
