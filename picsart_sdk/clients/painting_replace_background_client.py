from typing import Optional

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import CommonPaintingClient
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import (
    PaintingMode,
    ReplaceBackgroundRequest,
)


class CommonReplaceBackgroundClient(CommonPaintingClient):
    @property
    def endpoint(self) -> str:
        return "painting/replace-background"

    def _get_url(self, postfix_url: str = "", query_params: dict = None) -> str:
        url = super()._get_url(postfix_url=postfix_url, query_params=query_params)
        return url.replace("replace-background/", "")


class PaintingReplaceBackgroundClient(CommonReplaceBackgroundClient):

    def get_result(self, inference_id: str) -> PaintingApiResponse:
        return self.get(postfix_url=inference_id)

    def replace_background(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        request = ReplaceBackgroundRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            format=output_format.value.upper(),
            mode=mode,
        )

        return self.post(request=request)


class AsyncPaintingReplaceBackgroundClient(CommonReplaceBackgroundClient):
    async def get_result(self, inference_id: str) -> PaintingApiResponse:
        return await self.async_get(postfix_url=inference_id)

    async def replace_background(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        request = ReplaceBackgroundRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            format=output_format.value.upper(),
            mode=mode,
        )

        return await self.async_post(request=request)
