from typing import Optional

from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient
from picsart_sdk.clients.requests_models import (
    BleedRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonBleedClient(GenAiBaseClient):
    def parse_response(self, result: dict, request_method: str):
        return ApiResponse(
            status=result.get("status"), data=ApiResponseData(**result.get("data", {}))
        )

    @property
    def endpoint(self) -> str:
        return "painting/bleed"

    def set_payload(self, request):
        if request.image.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault("image_url", request.image.image_url)

        if request.image.image_path:
            self._payload = self._payload or {}
            self._files = self._files or {}
            self._files.setdefault(
                "image",
                (
                    request.image.image_path,
                    open(request.image.image_path, "rb"),
                ),
            )

        super().set_payload(request)


class BleedClient(CommonBleedClient):

    def bleed(
        self,
        prompt: Optional[str] = "",
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        bleed_size: Optional[int] = 5,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ):
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

        return await self.async_post(request=request)
