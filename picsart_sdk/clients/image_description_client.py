from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.api_responses.image_description_api_response import (
    ImageDescriptionApiResponse,
    ImageDescriptionApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import ImageDescriptionRequest, PicsartImage


class CommonImageDescriptionClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "describe"

    def _parse_response(self, result: dict) -> ImageDescriptionApiResponse:
        return ImageDescriptionApiResponse(
            status=result["status"],
            data=ImageDescriptionApiResponseData(
                description=result.get("data", {}).get("description")
            ),
        )


class ImageDescriptionClient(CommonImageDescriptionClient):

    def get_description(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ApiResponse:
        return self.post(
            request=ImageDescriptionRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )


class AsyncImageDescriptionClient(CommonImageDescriptionClient):

    async def get_description(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ApiResponse:
        return await self.async_post(
            request=ImageDescriptionRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )
