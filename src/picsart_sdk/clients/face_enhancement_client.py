from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import FaceEnhancementRequest, PicsartImage
from picsart_sdk.clients.requests_models.picsart_image import PicsartImageFormat


class FaceEnhancementClient(ImageBaseClient):
    """
    Client for face enhancement in images.

    This client provides functionality to enhance facial features in an image,
    allowing for high-quality improvements.
    """

    @property
    def _endpoint(self):
        return "enhance/face"

    def face_enhancement(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Enhance facial features in an image.

        :param image_url: The URL of the image to enhance.
        :param image_path: The local path of the image to enhance.
        :param output_format: The desired format for the enhanced image. Default is PNG.
        :return: The API response containing the enhanced image.
        """
        request = FaceEnhancementRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            format=output_format,
        )
        return self.post(request=request)


class AsyncFaceEnhancementClient(ImageBaseClient):
    """
    HTTP Async client for face enhancement in images.

    This client provides functionality to enhance facial features in an image,
    allowing for high-quality improvements.
    """

    @property
    def _endpoint(self):
        return "enhance/face"

    async def face_enhancement(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Enhance facial features in an image using the HTTP asynchronous client.

        :param image_url: The URL of the image to enhance.
        :param image_path: The local path of the image to enhance.
        :param output_format: The desired format for the enhanced image. Default is PNG.
        :return: The API response containing the enhanced image.
        """
        request = FaceEnhancementRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            format=output_format,
        )
        return await self.async_post(request=request)
