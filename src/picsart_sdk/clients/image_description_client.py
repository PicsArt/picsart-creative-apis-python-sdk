from typing import Optional

from picsart_sdk.api_responses.image_description_api_response import (
    ImageDescriptionApiResponse,
    ImageDescriptionApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import ImageDescriptionRequest, PicsartImage


class CommonImageDescriptionClient(ImageBaseClient):
    @property
    def _endpoint(self):
        return "describe"

    def parse_response(
        self, result: dict, request_method: str
    ) -> ImageDescriptionApiResponse:
        return ImageDescriptionApiResponse(
            status=result["status"],
            data=ImageDescriptionApiResponseData(
                description=result.get("data", {}).get("description")
            ),
        )


class ImageDescriptionClient(CommonImageDescriptionClient):
    """
    Client for getting the descriptions for an image.

    This client provides functionality to retrieve a textual description
    for a given image.
    """

    def get_description(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ImageDescriptionApiResponse:
        """
        Gets a description for the given image.

        :param image_url: The URL of the image to describe.
        :param image_path: The local path of the image to describe.
        :return: The API response containing the image description.
        """
        return self.post(
            request=ImageDescriptionRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )


class AsyncImageDescriptionClient(CommonImageDescriptionClient):
    """
    Client for getting the descriptions for an image, using the HTTP asynchronous client.

    This client provides functionality to retrieve a textual description
    for a given image.
    """

    async def get_description(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
    ) -> ImageDescriptionApiResponse:
        """
        Gets a description for the given image using the HTTP asynchronous client.

        :param image_url: The URL of the image to describe.
        :param image_path: The local path of the image to describe.
        :return: The API response containing the image description.
        """

        return await self.async_post(
            request=ImageDescriptionRequest(
                image=PicsartImage(image_path=image_path, image_url=image_url)
            )
        )
