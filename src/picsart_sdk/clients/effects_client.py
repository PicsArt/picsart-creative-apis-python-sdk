from typing import Optional, Union

from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.api_responses.effects_response import EffectsListApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonEffectsClient(ImageBaseClient):
    @property
    def _endpoint(self):
        return "effects"

    def parse_response(
        self, result: dict, request_method: str
    ) -> Union[EffectsListApiResponse, ApiResponse]:
        if request_method == "GET":
            return EffectsListApiResponse(
                effects=[item.get("name") for item in result.get("data", [])]
            )
        return ApiResponse(
            status=result.get("status"), data=ApiResponseData(**result.get("data", {}))
        )


class EffectsClient(CommonEffectsClient):
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

    def get_available_effects(self) -> EffectsListApiResponse:
        return self.get()


class AsyncEffectsClient(CommonEffectsClient):

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

    async def get_available_effects(self) -> EffectsListApiResponse:
        return await self.async_get()
