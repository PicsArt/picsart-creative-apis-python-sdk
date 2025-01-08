from typing import Optional, Union

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import CommonReplaceBackgroundClient
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import (
    PaintingMode,
    ReplaceBackgroundRequest,
)


class PaintingReplaceBackgroundClient(CommonReplaceBackgroundClient):
    """
    Client for replacing the background of an image based on a prompt.

    This client provides functionality to replace the background of an image
    by generating new content based on user-provided prompts.
    """

    def replace_background(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Replace the background of an image based on a user-provided prompt.

        :param prompt: The prompt describing the desired content for the new background.
        :param image_url: The URL of the image whose background is to be replaced.
        :param image_path: The local path of the image whose background is to be replaced.
        :param negative_prompt: An optional prompt specifying what to avoid in the new background.
        :param count: The number of variations of the replaced background to generate. Default is 4.
        :param output_format: The desired format for the output image. Default is PNG.
        :param mode: The mode of operation (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the image with the replaced background.
        """
        request = ReplaceBackgroundRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            format=output_format.value.upper(),
            mode=mode,
        )

        return self.post(request=request)

    def get_result(self, inference_id: str) -> PaintingApiResponse:
        """
        Retrieve the result of a background replacement operation using its inference ID.

        :param inference_id: The unique identifier for the background replacement operation, returned by the `replace_background` method.
        :return: The API response containing the image with the replaced background.
        """

        return self.get(postfix_url=inference_id)


class AsyncPaintingReplaceBackgroundClient(CommonReplaceBackgroundClient):
    """
    Client for replacing the background of an image based on a prompt, using the asynchronous HTTP client.

    This client provides functionality to replace the background of an image
    by generating new content based on user-provided prompts.
    """

    async def replace_background(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Replace the background of an image based on a user-provided prompt, using the asynchronous HTTP client.

        :param prompt: The prompt describing the desired content for the new background.
        :param image_url: The URL of the image whose background is to be replaced.
        :param image_path: The local path of the image whose background is to be replaced.
        :param negative_prompt: An optional prompt specifying what to avoid in the new background.
        :param count: The number of variations of the replaced background to generate. Default is 4.
        :param output_format: The desired format for the output image. Default is PNG.
        :param mode: The mode of operation (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the image with the replaced background.
        """
        request = ReplaceBackgroundRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            format=output_format.value.upper(),
            mode=mode,
        )

        return await self.async_post(request=request)

    async def get_result(self, inference_id: str) -> PaintingApiResponse:
        """
        Asynchronous HTTP call for retrieve the result of a background replacement operation, using its inference ID.

        :param inference_id: The unique identifier for the background replacement operation, returned by the `replace_background` method.
        :return: The API response containing the image with the replaced background.
        """
        return await self.async_get(postfix_url=inference_id)
