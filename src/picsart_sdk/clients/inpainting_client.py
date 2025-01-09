from typing import Optional, Union

from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients.common_painting_client import InpaintingCommon
from picsart_sdk.clients.requests_models import PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import PaintingMode


class InpaintingClient(InpaintingCommon):
    """
    Client for performing inpainting operations.

    The Inpainting service offers inpainting capabilities,
    enabling users to fill or replace areas within an image based on specified criteria.

    It operates in two modes:

    * Single Image Mode: Submit one RGBA image. The API fills the specified inner area with content based on the `prompt` parameter.
    * Mask Mode: Along with the RGBA image, provide a mask of identical size and format. The API uses this mask to identify areas for inpainting with content determined by the `prompt` parameter.

    """

    def inpainting(
        self,
        prompt: str,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        mask_url: Optional[str] = None,
        mask_path: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        count: Optional[int] = 4,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
        mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC,
    ) -> PaintingApiResponse:
        """
        Perform an inpainting operation on an image.

        :param prompt: The prompt describing the desired changes or replacements for the image.
        :param image_url: The URL of the image to inpaint.
        :param image_path: The local path of the image to inpaint.
        :param mask_url: The URL of the mask image defining the area to inpaint.
        :param mask_path: The local path of the mask image defining the area to inpaint.
        :param negative_prompt: An optional prompt specifying what to avoid in the inpainting result.
        :param count: The number of inpainting variations to generate. Default is 4.
        :param output_format: The desired format for the inpainting result. Default is PNG.
        :param mode: The mode of inpainting (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the inpainting result.
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
        Retrieve the result of an inpainting operation using its inference ID.

        :param inference_id: The unique identifier for the inpainting operation, returned by the `inpainting` method.
        :return: The API response containing the inpainting result.
        """

        return self.get(postfix_url=inference_id)


class AsyncInpaintingClient(InpaintingCommon):
    """
    Client for performing inpainting operations, using an HTTP asynchronous client.

    The Inpainting service offers inpainting capabilities,
    enabling users to fill or replace areas within an image based on specified criteria.

    It operates in two modes:

    * Single Image Mode: Submit one RGBA image. The API fills the specified inner area with content based on the `prompt` parameter.
    * Mask Mode: Along with the RGBA image, provide a mask of identical size and format. The API uses this mask to identify areas for inpainting with content determined by the `prompt` parameter.

    """

    async def inpainting(
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
        Perform an inpainting operation on an image using an asynchronous HTTP client.

        :param prompt: The prompt describing the desired changes or replacements for the image.
        :param image_url: The URL of the image to inpaint.
        :param image_path: The local path of the image to inpaint.
        :param mask_url: The URL of the mask image defining the area to inpaint.
        :param mask_path: The local path of the mask image defining the area to inpaint.
        :param negative_prompt: An optional prompt specifying what to avoid in the inpainting result.
        :param count: The number of inpainting variations to generate. Default is 4.
        :param output_format: The desired format for the inpainting result. Default is PNG.
        :param mode: The mode of inpainting (e.g., synchronous or asynchronous). Default is synchronous.
        :return: The API response containing the inpainting result.
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
        Retrieve the result of an inpainting operation using its inference ID, using an asynchronous HTTP client.

        :param inference_id: The unique identifier for the inpainting operation, returned by the `inpainting` method.
        :return: The API response containing the inpainting result.
        """

        return await self.async_get(postfix_url=inference_id)
