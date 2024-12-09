from typing import Optional

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import CommonPaintingClient
from picsart_sdk.clients.requests_models import (
    BleedRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonBleedClient(CommonPaintingClient):
    @property
    def endpoint(self) -> str:
        return "painting/bleed"


class BleedClient(CommonBleedClient):

    def bleed(
        self,
        prompt: Optional[str] = "",
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        bleed_size: Optional[int] = 5,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> PaintingApiResponse:
        request = BleedRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            bleed_size=bleed_size,
            format=output_format.value.upper(),
        )

        return self.post(request=request)


class AsyncBleedClient(CommonBleedClient):
    async def bleed(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        bleed_size: Optional[int] = 5,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> PaintingApiResponse:
        request = BleedRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            bleed_size=bleed_size,
            format=output_format.value.upper(),
        )

        return await self.async_post(request=request)
