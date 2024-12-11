from typing import Optional

from picsart_sdk.api_responses.image_tagging_api_response import (
    ImageTaggingApiResponse,
    ImageTaggingApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import ImageTaggingRequest, PicsartImage


class CommonImageTaggingClient(ImageBaseClient):
    @property
    def _endpoint(self):
        return "tags"

    def parse_response(
        self, result: dict, request_method: str
    ) -> ImageTaggingApiResponse:
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
    ) -> ImageTaggingApiResponse:
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
    ) -> ImageTaggingApiResponse:
        return await self.async_post(
            request=ImageTaggingRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )
