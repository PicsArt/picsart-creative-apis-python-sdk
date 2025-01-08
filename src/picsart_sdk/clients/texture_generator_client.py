from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    PicsartImage,
    PicsartImageFormat,
    TextureGeneratorRequest,
)


class TextureGeneratorClient(ImageBaseClient):
    """
    Client for generating textures based on images.

    The texture generator tool generates a background texture pattern for the input image.
    You can create unlimited textures from the same texture source image.
    """

    @property
    def _endpoint(self):
        return "background/texture"

    def texture_generator(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        offset_x: Optional[int] = 0,
        offset_y: Optional[int] = 0,
        pattern: Optional[str] = "hex",
        rotate: Optional[int] = 0,
        scale: Optional[float] = 1,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Generate a texture based on the provided image and parameters.

        :param image_url: The URL of the image to use for texture generation.
        :param image_path: The local path of the image to use for texture generation.
        :param width: The width of the generated texture. Default is 1024.
        :param height: The height of the generated texture. Default is 1024.
        :param offset_x: The horizontal offset for the texture pattern. Default is 0.
        :param offset_y: The vertical offset for the texture pattern. Default is 0.
        :param pattern: The pattern to apply (e.g., "hex", "stripe"). Default is "hex".
        :param rotate: The rotation angle for the texture pattern in degrees. Default is 0.
        :param scale: The scaling factor for the texture pattern. Default is 1.
        :param output_format: The desired format for the output texture. Default is PNG.
        :return: The API response containing the generated texture.
        """

        request = TextureGeneratorRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            width=width,
            height=height,
            offset_x=offset_x,
            offset_y=offset_y,
            pattern=pattern,
            rotate=rotate,
            scale=scale,
            format=output_format,
        )
        return self.post(request=request)


class AsyncTextureGeneratorClient(ImageBaseClient):
    """
    Client for generating textures based on images, using an asynchronous HTTP client.

    The texture generator tool generates a background texture pattern for the input image.
    You can create unlimited textures from the same texture source image.
    """

    @property
    def _endpoint(self):
        return "background/texture"

    async def texture_generator(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        offset_x: Optional[int] = 0,
        offset_y: Optional[int] = 0,
        pattern: Optional[str] = "hex",
        rotate: Optional[int] = 0,
        scale: Optional[float] = 1,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> ApiResponse:
        """
        Generate a texture based on the provided image and parameters, using an asynchronous HTTP client.

        :param image_url: The URL of the image to use for texture generation.
        :param image_path: The local path of the image to use for texture generation.
        :param width: The width of the generated texture. Default is 1024.
        :param height: The height of the generated texture. Default is 1024.
        :param offset_x: The horizontal offset for the texture pattern. Default is 0.
        :param offset_y: The vertical offset for the texture pattern. Default is 0.
        :param pattern: The pattern to apply (e.g., "hex", "stripe"). Default is "hex".
        :param rotate: The rotation angle for the texture pattern in degrees. Default is 0.
        :param scale: The scaling factor for the texture pattern. Default is 1.
        :param output_format: The desired format for the output texture. Default is PNG.
        :return: The API response containing the generated texture.
        """

        request = TextureGeneratorRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            width=width,
            height=height,
            offset_x=offset_x,
            offset_y=offset_y,
            pattern=pattern,
            rotate=rotate,
            scale=scale,
            format=output_format,
        )
        return await self.async_post(request=request)
