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
    """
    Client for getting the tags for an image.

    This client provides functionality to retrieve the tags for a given image.
    """

    def get_tags(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ImageTaggingApiResponse:
        """
        Gets the tags for the given image.

        :param image_url: The URL of the image to describe.
        :param image_path: The local path of the image to describe.
        :return: The API response containing the image description.
        """

        return self.post(
            request=ImageTaggingRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )


class AsyncImageTaggingClient(CommonImageTaggingClient):
    """
    Client for getting the tags for an image, using the HTTP asynchronous client.

    This client provides functionality to retrieve the tags for a given image.
    """

    async def get_tags(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ImageTaggingApiResponse:
        """
        Gets the tags for the given image using the HTTP asynchronous client.

        :param image_url: The URL of the image to describe.
        :param image_path: The local path of the image to describe.
        :return: The API response containing the image description.
        """

        return await self.async_post(
            request=ImageTaggingRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )
