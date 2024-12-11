from typing import Optional

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import CommonPaintingClient
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import (
    ExpandRequest,
    PaintingMode,
)


class CommonExpandClient(CommonPaintingClient):
    @property
    def endpoint(self) -> str:
        return "painting/expand"

    def _get_url(self, postfix_url: str = "", query_params: dict = None) -> str:
        url = super()._get_url(postfix_url=postfix_url, query_params=query_params)
        return url.replace("expand/", "")


class PaintingExpandClient(CommonExpandClient):

    def get_result(self, inference_id: str) -> PaintingApiResponse:
        return self.get(postfix_url=inference_id)

    def expand(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        direction: Optional[str] = "center",
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        request = ExpandRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            width=width,
            height=height,
            direction=direction,
            format=output_format.value.upper(),
            mode=mode,
        )

        return self.post(request=request)


class AsyncPaintingExpandClient(CommonExpandClient):
    async def get_result(self, inference_id: str) -> PaintingApiResponse:
        return await self.async_get(postfix_url=inference_id)

    async def expand(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        direction: Optional[str] = "center",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        request = ExpandRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            width=width,
            height=height,
            direction=direction,
            format=output_format.value.upper(),
            mode=mode,
        )

        return await self.async_post(request=request)
