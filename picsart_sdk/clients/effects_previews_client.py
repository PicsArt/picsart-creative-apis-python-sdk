from typing import Optional

from picsart_sdk.api_responses.effects_response import (
    EffectsPreviewsApiResponse,
    EffectsPreviewsApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsPreviewsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class EffectsPreviewsClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "effects/previews"

    def effects_previews(
        self,
        effect_names: list[str],
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> EffectsPreviewsApiResponse:
        request = EffectsPreviewsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_names=effect_names,
            preview_size=preview_size,
            format=output_format,
        )
        return self.post(request=request)

    def parse_response(
        self, result: dict, request_method: str
    ) -> EffectsPreviewsApiResponse:

        return EffectsPreviewsApiResponse(
            status=result.get("status"),
            data=[
                EffectsPreviewsApiResponseData(
                    id=item.get("id"),
                    url=item.get("url"),
                    effect_name=item.get("effect_name"),
                )
                for item in result.get("data", [])
            ],
        )


class AsyncEffectsPreviewsClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "effects/previews"

    async def effects_previews(
        self,
        effect_names: list[str],
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> EffectsPreviewsApiResponse:
        request = EffectsPreviewsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_names=effect_names,
            preview_size=preview_size,
            format=output_format,
        )
        return await self.async_post(request=request)

    def parse_response(
        self, result: dict, request_method: str
    ) -> EffectsPreviewsApiResponse:

        return EffectsPreviewsApiResponse(
            status=result.get("status"),
            data=[
                EffectsPreviewsApiResponseData(
                    id=item.get("id"),
                    url=item.get("url"),
                    effect_name=item.get("effect_name"),
                )
                for item in result.get("data", [])
            ],
        )
