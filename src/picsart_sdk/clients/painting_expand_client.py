from typing import Optional, Union

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import CommonExpandClient
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import (
    ExpandRequest,
    PaintingMode,
)


class PaintingExpandClient(CommonExpandClient):
    """
    Client for expanding images based on a prompt.

    This client provides functionality to extend an image by generating additional
    content in specified directions using AI-based prompts.

    It supports two operational modes:

    * **Single Image Mode**: Upload one RGBA image. The API enhances the outer area with content based on the prompt parameter.
    * **Mask Mode**: Provide an RGBA image along with a mask of the same size. The API applies this mask to paint beyond the masked region, using content determined by the prompt parameter.
    """

    def expand(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        direction: Optional[str] = "center",
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Expand an image by generating additional content based on a prompt, using an asynchronous HTTP client.

        :param prompt: The prompt describing the content to generate in the expanded areas.
        :param image_url: The URL of the image to expand.
        :param image_path: The local path of the image to expand.
        :param negative_prompt: An optional prompt specifying what to avoid in the expansion.
        :param width: The width of the expanded image. Default is 1024.
        :param height: The height of the expanded image. Default is 1024.
        :param direction: The direction in which to expand the image (e.g., "center", "top").
        :param count: The number of expansion variations to generate. Default is 4.
        :param output_format: The desired format for the expanded image. Default is PNG.
        :param mode: The mode of operation (e.g., synchronous, asynchronous). Default is synchronous.
        :return: The API response containing the expanded image.
        """
        request = ExpandRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            width=width,
            height=height,
            direction=direction,
            format=output_format.value.upper(),
            mode=mode,
        )

        return self.post(request=request)

    def get_result(self, inference_id: str) -> PaintingApiResponse:
        """
        Retrieve the result of an expansion operation using its inference ID.

        :param inference_id: The unique identifier for the expansion operation, returned by the `expand` method.
        :return: The API response containing the expanded image.
        """
        return self.get(postfix_url=inference_id)


class AsyncPaintingExpandClient(CommonExpandClient):
    """
    Client for expanding images based on a prompt.

    This client provides functionality to extend an image by generating additional
    content in specified directions using AI-based prompts.

    It supports two operational modes:

    * **Single Image Mode**: Upload one RGBA image. The API enhances the outer area with content based on the prompt parameter.
    * **Mask Mode**: Provide an RGBA image along with a mask of the same size. The API applies this mask to paint beyond the masked region, using content determined by the prompt parameter.
    """

    async def expand(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        direction: Optional[str] = "center",
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Expand an image by generating additional content based on a prompt, using an asynchronous HTTP client.

        :param prompt: The prompt describing the content to generate in the expanded areas.
        :param image_url: The URL of the image to expand.
        :param image_path: The local path of the image to expand.
        :param negative_prompt: An optional prompt specifying what to avoid in the expansion.
        :param width: The width of the expanded image. Default is 1024.
        :param height: The height of the expanded image. Default is 1024.
        :param direction: The direction in which to expand the image (e.g., "center", "top").
        :param count: The number of expansion variations to generate. Default is 4.
        :param output_format: The desired format for the expanded image. Default is PNG.
        :param mode: The mode of operation (e.g., synchronous, asynchronous). Default is synchronous.
        :return: The API response containing the expanded image.
        """

        request = ExpandRequest(
            prompt=prompt,
            image=PicsartImage(image_url=image_url, image_path=image_path),
            negative_prompt=negative_prompt,
            count=count,
            width=width,
            height=height,
            direction=direction,
            format=output_format.value.upper(),
            mode=mode,
        )

        return await self.async_post(request=request)

    async def get_result(self, inference_id: str) -> PaintingApiResponse:
        """
        Retrieve the result of an expansion operation using its inference ID, using an asynchronous HTTP client.

        :param inference_id: The unique identifier for the expansion operation, returned by the `expand` method.
        :return: The API response containing the expanded image.
        """
        return await self.async_get(postfix_url=inference_id)
