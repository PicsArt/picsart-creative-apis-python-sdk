from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.api_responses.image_tagging_api_response import (
    ImageTaggingApiResponse,
    ImageTaggingApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import ImageTaggingRequest, PicsartImage


class CommonImageTaggingClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "tags"

    def _parse_response(self, result: dict) -> ImageTaggingApiResponse:
        return ImageTaggingApiResponse(
            status=result["status"],
            data=ImageTaggingApiResponseData(
                tags=result.get("data", {}).get("tags", [])
            ),
        )


class ImageTaggingClient(CommonImageTaggingClient):

    def get_tags(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ApiResponse:
        return self.post(
            request=ImageTaggingRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )


class AsyncImageTaggingClient(CommonImageTaggingClient):

    async def get_tags(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ApiResponse:
        return await self.async_post(
            request=ImageTaggingRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )
