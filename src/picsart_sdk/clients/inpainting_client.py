from typing import Optional, Union

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import InpaintingCommon
from picsart_sdk.clients.requests_models import PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import PaintingMode


class InpaintingClient(InpaintingCommon):
    def get_result(self, inference_id: str) -> PaintingApiResponse:
        return self.get(postfix_url=inference_id)

    def inpainting(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        return super().sync_inpainting_request(
            prompt=prompt,
            image_url=image_url,
            image_path=image_path,
            mask_url=mask_url,
            mask_path=mask_path,
            negative_prompt=negative_prompt,
            count=count,
            output_format=output_format,
            mode=mode,
        )


class AsyncInpaintingClient(InpaintingCommon):

    async def get_result(self, inference_id: str) -> PaintingApiResponse:
        return await self.async_get(postfix_url=inference_id)

    async def inpainting(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        return await super().async_inpainting_request(
            prompt=prompt,
            image_url=image_url,
            image_path=image_path,
            mask_url=mask_url,
            mask_path=mask_path,
            negative_prompt=negative_prompt,
            count=count,
            output_format=output_format,
            mode=mode,
        )
