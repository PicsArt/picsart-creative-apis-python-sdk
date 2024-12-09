from typing import Optional

from picsart_sdk.clients.common_painting_client import (
    InpaintingCommon,
    OutpaintingCommon,
)
from picsart_sdk.clients.requests_models import PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import PaintingMode


class InpaintingClient(InpaintingCommon):
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
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ):
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
    ):
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


class OutpaintingClient(OutpaintingCommon):

    def outpainting(
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
    ):
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


class AsyncOutpaintingClient(OutpaintingCommon):
    async def outpainting(
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
    ):
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
