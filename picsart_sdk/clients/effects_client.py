from typing import Optional, Union

from picsart_sdk.api_responses import ApiResponse

from picsart_sdk.api_responses.effects_responses import EffectsList
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    EffectsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class EffectsClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "effects"

    def effects(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        effect_name: Optional[str] = None,
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

    def _parse_response(self, result: dict) -> Union[ApiResponse, EffectsList]:
        if isinstance(result.get("data"), list):
            return EffectsList(
                effects=[item.get("name") for item in result.get("data", [])]
            )

        return super()._parse_response(result)


class AsyncEffectsClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "effects"

    async def effects(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        effect_name: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        request = EffectsRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            effect_name=effect_name,
            format=output_format,
        )
        return await self.async_post(request=request)
