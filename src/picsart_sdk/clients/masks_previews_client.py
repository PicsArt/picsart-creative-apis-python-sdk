from typing import Optional

from picsart_sdk.api_responses.masks_previews_response import (
    MasksPreviewsApiResponse,
    MasksPreviewsApiResponseData,
)
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import (
    MasksPreviewsRequest,
    PicsartImage,
    PicsartImageFormat,
)


class CommonMasksPreviewsClient(ImageBaseClient):

    @property
    def _endpoint(self):
        return "masks/previews"

    @classmethod
    def _get_mask_param(
        cls,
        mask: Optional[list[str]] = None,
    ):
        if isinstance(mask, str):
            return [mask]

        if isinstance(mask, list) and len(mask) >= 1:
            return mask

        return ["lace1"]

    def parse_response(
        self, result: dict, request_method: str
    ) -> MasksPreviewsApiResponse:
        data = result.get("data")
        if isinstance(data, dict):
            return MasksPreviewsApiResponse(
                status=result.get("status"),
                data=[
                    MasksPreviewsApiResponseData(
                        id=data.get("id"),
                        url=data.get("url"),
                        mask="",
                    )
                ],
            )

        return MasksPreviewsApiResponse(
            status=result.get("status"),
            data=[
                MasksPreviewsApiResponseData(
                    id=item.get("id"),
                    url=item.get("url"),
                    mask=item.get("mask"),
                )
                for item in result.get("data", [])
            ],
        )


class MasksPreviewsClient(CommonMasksPreviewsClient):
    """
    Client for generating mask effects to a given input image and returns a preview (i.e., thumbnail) of the effect.

    This client provides functionality to apply multiple masks to an image
    and generate previews with customizable parameters such as blending, opacity, mask flip,
    and hue adjustments.
    """

    def masks_previews(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[list[str]] = None,
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> MasksPreviewsApiResponse:
        """
        Generate previews for multiple masks applied to an image.

        :param image_url: The URL of the image to apply the masks to.
        :param image_path: The local path of the image to apply the masks to.
        :param blend: The blending mode for the masks (e.g., "screen").
        :param mask: A list of mask names to apply.
        :param opacity: The opacity of the masks (0 to 100). Default is 100.
        :param hue: The hue adjustment for the masks. Default is 0.
        :param mask_flip: The flip mode for the masks (e.g., "horizontal").
        :param preview_size: The size of the preview images. Default is 120.
        :param output_format: The desired format for the preview images. Default is PNG.
        :return: The API response containing the mask previews.
        """

        request = MasksPreviewsRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=self._get_mask_param(mask),
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            preview_size=preview_size,
            format=output_format,
        )
        return self.post(request=request)


class AsyncMasksPreviewsClient(CommonMasksPreviewsClient):
    """
    Client for generating mask effects to a given input image and returns a preview (i.e., thumbnail) of the effect,
    using the asynchronous HTTP client.

    This client provides functionality to apply multiple masks to an image
    and generate previews with customizable parameters such as blending, opacity, mask flip,
    and hue adjustments.
    """

    async def masks_previews(
        self,
        image_url: Optional[str] = None,
        image_path: Optional[str] = None,
        blend: Optional[str] = "screen",
        mask: Optional[list[str]] = None,
        opacity: Optional[int] = 100,
        hue: Optional[int] = 0,
        mask_flip: Optional[str] = "",
        preview_size: Optional[int] = 120,
        output_format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG,
    ) -> MasksPreviewsApiResponse:
        """
        Generate previews for multiple masks applied to an image using the asynchronous HTTP client.

        :param image_url: The URL of the image to apply the masks to.
        :param image_path: The local path of the image to apply the masks to.
        :param blend: The blending mode for the masks (e.g., "screen").
        :param mask: A list of mask names to apply.
        :param opacity: The opacity of the masks (0 to 100). Default is 100.
        :param hue: The hue adjustment for the masks. Default is 0.
        :param mask_flip: The flip mode for the masks (e.g., "horizontal").
        :param preview_size: The size of the preview images. Default is 120.
        :param output_format: The desired format for the preview images. Default is PNG.
        :return: The API response containing the mask previews.
        """

        request = MasksPreviewsRequest(
            image=PicsartImage(image_path=image_path, image_url=image_url),
            blend=blend,
            mask=self._get_mask_param(mask),
            opacity=opacity,
            hue=hue,
            mask_flip=mask_flip,
            preview_size=preview_size,
            format=output_format,
        )
        return await self.async_post(request=request)
