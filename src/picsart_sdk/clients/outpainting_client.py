from typing import Optional, Union

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import OutpaintingCommon
from picsart_sdk.clients.requests_models import PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import PaintingMode


class OutpaintingClient(OutpaintingCommon):
    """
    Client for performing outpainting operations.

    The Outpainting service enables outpainting, allowing users to extend or replace specific parts of an image.
    This is a reversed form of the Inpainting service (drawing outside of the mask, not inside).

    It operates in two modes:

    * **Single Image Mode**: Upload one RGBA image. The API enhances the outer area with content based on the prompt parameter.
    * **Mask Mode**: Provide an RGBA image along with a mask of the same size. The API applies this mask to paint beyond the masked region, using content determined by the prompt parameter.
    """

    def outpainting(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Perform an outpainting operation on an image.

        :param prompt: The prompt describing the desired changes or replacements for the image.
        :param image_url: The URL of the image to outpaint.
        :param image_path: The local path of the image to outpaint.
        :param mask_url: The URL of the mask image defining the area to outpaint.
        :param mask_path: The local path of the mask image defining the area to outpaint.
        :param negative_prompt: An optional prompt specifying what to avoid in the outpainting result.
        :param count: The number of outpainting variations to generate. Default is 4.
        :param output_format: The desired format for the outpainting result. Default is PNG.
        :param mode: The mode of outpainting (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the outpainting result.
        """

        return super().sync_inpainting_request(
            prompt=prompt,
            image_url=image_url,
            image_path=image_path,
            mask_url=mask_url,
            mask_path=mask_path,
            negative_prompt=negative_prompt,
            count=count,
            output_format=output_format,
            mode=mode,
        )

    def get_result(self, inference_id: str) -> PaintingApiResponse:
        """
        Retrieve the result of an outpainting operation using its inference ID.

        :param inference_id: The unique identifier for the outpainting operation.
        :return: The API response containing the outpainting result.
        """

        return self.get(postfix_url=inference_id)


class AsyncOutpaintingClient(OutpaintingCommon):
    """
    Client for performing outpainting operations, using an asynchronous HTTP client.

    The Outpainting service enables outpainting, allowing users to extend or replace specific parts of an image.
    This is a reversed form of the Inpainting service (drawing outside of the mask, not inside).

    It operates in two modes:

    * **Single Image Mode**: Upload one RGBA image. The API enhances the outer area with content based on the prompt parameter.
    * **Mask Mode**: Provide an RGBA image along with a mask of the same size. The API applies this mask to paint beyond the masked region, using content determined by the prompt parameter.
    """

    async def outpainting(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Perform an outpainting operation on an image using an asynchronous HTTP client.

        :param prompt: The prompt describing the desired changes or replacements for the image.
        :param image_url: The URL of the image to outpaint.
        :param image_path: The local path of the image to outpaint.
        :param mask_url: The URL of the mask image defining the area to outpaint.
        :param mask_path: The local path of the mask image defining the area to outpaint.
        :param negative_prompt: An optional prompt specifying what to avoid in the outpainting result.
        :param count: The number of outpainting variations to generate. Default is 4.
        :param output_format: The desired format for the outpainting result. Default is PNG.
        :param mode: The mode of outpainting (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the outpainting result.
        """

        return await super().async_inpainting_request(
            prompt=prompt,
            image_url=image_url,
            image_path=image_path,
            mask_url=mask_url,
            mask_path=mask_path,
            negative_prompt=negative_prompt,
            count=count,
            output_format=output_format,
            mode=mode,
        )

    async def get_result(self, inference_id: str) -> PaintingApiResponse:
        """
        Retrieve the result of an outpainting operation using its inference ID, using an asynchronous HTTP client.

        :param inference_id: The unique identifier for the outpainting operation.
        :return: The API response containing the outpainting result.
        """

        return await self.async_get(postfix_url=inference_id)
