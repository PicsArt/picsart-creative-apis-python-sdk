from abc import ABC
from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat
from picsart_sdk.clients.requests_models.painting_request import (
    InpaintingRequest,
    PaintingMode,
)


@dataclass
class AsyncPaintingDataApiResponse:
    id: str
    url: str


@dataclass
class PaintingApiResponse:
    status: str
    data: list[AsyncPaintingDataApiResponse]
    inference_id: str


class CommonPaintingClient(GenAiBaseClient, ImageBaseClient, ABC):
    def parse_response(self, result):
        return PaintingApiResponse(**result)

    def set_payload(self, request: InpaintingRequest):
        ImageBaseClient.set_payload(self, request)

        if request.mask.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault("mask_url", request.mask.image_url)

        if request.mask.image_path:
            self._payload = self._payload or {}
            self._files = self._files or {}
            self._files.setdefault(
                "mask",
                (
                    request.mask.image_path,
                    open(request.mask.image_path, "rb"),
                ),
            )

        self._payload.update(request.get_dict())


class InpaintingClient(CommonPaintingClient):
    @property
    def endpoint(self) -> str:
        return "painting/inpaint"

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
        mode: Optional[PaintingMode] = PaintingMode.SYNC,
    ):
        request = InpaintingRequest(
            image=PicsartImage(image_url=image_url, image_path=image_path),
            mask=PicsartImage(image_url=mask_url, image_path=mask_path),
            prompt=prompt,
            negative_prompt=negative_prompt,
            count=count,
            mode=mode,
            format=output_format.value.upper(),
        )
        return self.post(request=request)

    def get_results(self, inference_id: str) -> PaintingApiResponse:
        return self.get(postfix_url=inference_id)

    def _get_url(self, postfix_url: str = "", query_params: dict = None) -> str:
        url = super()._get_url(postfix_url=postfix_url, query_params=query_params)
        return url.replace("inpaint/", "")
