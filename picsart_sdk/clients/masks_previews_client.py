from abc import ABC
from typing import Optional

from picsart_sdk.api_responses.masks_previews_response import (
    MasksPreviewsApiResponse,
    MasksPreviewsApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    MasksPreviewsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class MasksPreviewsClientCommon(ImageBaseClient):

    @property
    def endpoint(self):
        return "masks/previews"

    @classmethod
    def _get_mask_param(
        cls,
        mask: Optional[list[str]] = None,
    ):
        if isinstance(mask, str):
            return [mask]

        if isinstance(mask, list) and len(mask) >= 1:
            return mask

        return ["lace1"]

    def parse_response(self, result: dict) -> MasksPreviewsApiResponse:
        data = result.get("data")
        if isinstance(data, dict):
            return MasksPreviewsApiResponse(
                status=result.get("status"),
                data=[
                    MasksPreviewsApiResponseData(
                        id=data.get("id"),
                        url=data.get("url"),
                        mask="",
                    )
                ],
            )

        for item in result.get("data", []):
            print(item)

        return MasksPreviewsApiResponse(
            status=result.get("status"),
            data=[
                MasksPreviewsApiResponseData(
                    id=item.get("id"),
                    url=item.get("url"),
                    mask=item.get("mask"),
                )
                for item in result.get("data", [])
            ],
        )


class MasksPreviewsClient(MasksPreviewsClientCommon):

    def masks_previews(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[list[str]] = None,
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> MasksPreviewsApiResponse:
        request = MasksPreviewsRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=self._get_mask_param(mask),
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            preview_size=preview_size,
            format=output_format,
        )
        return self.post(request=request)


class AsyncMasksPreviewsClient(MasksPreviewsClientCommon):

    async def masks_previews(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[list[str]] = None,
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> MasksPreviewsApiResponse:
        request = MasksPreviewsRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=self._get_mask_param(mask),
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            preview_size=preview_size,
            format=output_format,
        )
        return await self.async_post(request=request)
