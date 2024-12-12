from typing import Optional, Union

from picsart_sdk.api_responses.text2image_response import (
    Text2ImageApiResponse,
    Text2ImageApiResponseData,
    Text2ImageCreateApiResponse,
)
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient
from picsart_sdk.clients.requests_models import Text2ImageRequest


class CommonText2ImageClient(GenAiBaseClient):
    @property
    def _endpoint(self) -> str:
        return "text2image"

    def parse_response(
        self, result: dict, request_method: str
    ) -> Union[Text2ImageCreateApiResponse, Text2ImageApiResponse]:
        if result.get("inference_id") and result.get("status") == "ACCEPTED":
            return Text2ImageCreateApiResponse(**result)

        data = None
        if result.get("data") and result.get("status") == "FINISHED":
            data = [
                Text2ImageApiResponseData(**item) for item in result.get("data", [])
            ]

        return Text2ImageApiResponse(status=result.get("status"), data=data)


class Text2ImageClient(CommonText2ImageClient):
    """
    Client for generating images from text prompts.

    The Text2Image service helps generate an image based on the text introduced as input by the user.
    """

    def text2image(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        count: Optional[int] = 2,
    ) -> Text2ImageCreateApiResponse:
        """
        Generate images based on a text prompt.

        :param prompt: The primary text prompt describing the desired image.
        :param negative_prompt: An optional text prompt specifying what to avoid in the image. Default is an empty string.
        :param width: The width of the generated image. Default is 1024.
        :param height: The height of the generated image. Default is 1024.
        :param count: The number of image variations to generate. Default is 2.
        :return: The API response containing the generated images.
        """
        request = Text2ImageRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            count=count,
        )
        return self.post(request=request, as_json=True)

    def get_result(self, inference_id: str) -> Text2ImageApiResponse:
        """
        Retrieve the result of a text-to-image operation using its inference ID.

        :param inference_id: The unique identifier for the text-to-image operation.
        :return: The API response containing the generated image results.
        """
        return self.get(postfix_url=f"inferences/{inference_id}")


class AsyncText2ImageClient(CommonText2ImageClient):
    """
    Client for generating images from text prompts, using an asynchronous HTTP client.

    The Text2Image service helps generate an image based on the text introduced as input by the user.
    """

    async def text2image(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        count: Optional[int] = 2,
    ) -> Text2ImageCreateApiResponse:
        """
        Generate images based on a text prompt using an asynchronous HTTP client.

        :param prompt: The primary text prompt describing the desired image.
        :param negative_prompt: An optional text prompt specifying what to avoid in the image. Default is an empty string.
        :param width: The width of the generated image. Default is 1024.
        :param height: The height of the generated image. Default is 1024.
        :param count: The number of image variations to generate. Default is 2.
        :return: The API response containing the generated images.
        """

        request = Text2ImageRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            count=count,
        )
        return await self.async_post(request=request, as_json=True)

    async def get_result(self, inference_id: str) -> Text2ImageApiResponse:
        """
        Retrieve the result of a text-to-image operation using its inference ID using an asynchronous HTTP client.

        :param inference_id: The unique identifier for the text-to-image operation.
        :return: The API response containing the generated image results.
        """
        return await self.async_get(postfix_url=f"inferences/{inference_id}")
