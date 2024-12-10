from typing import Optional, Union

from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.api_responses.effects_response import EffectsList
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonEffects(ImageBaseClient):
    @property
    def endpoint(self):
        return "effects"

    def parse_response(
        self, result: dict, request_method: str
    ) -> Union[EffectsList, ApiResponse]:
        if request_method == "GET":
            return EffectsList(
                effects=[item.get("name") for item in result.get("data", [])]
            )
        return ApiResponse(
            status=result.get("status"), data=ApiResponseData(**result.get("data", {}))
        )


class EffectsClient(CommonEffects):
    def effects(
        self,
        effect_name: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return self.post(request=request)

    def get_available_effects(self) -> EffectsList:
        return self.get()


class AsyncEffectsClient(CommonEffects):

    async def effects(
        self,
        effect_name: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return await self.async_post(request=request)

    async def get_available_effects(self) -> EffectsList:
        return await self.async_get()
