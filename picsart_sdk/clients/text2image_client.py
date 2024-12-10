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
    def endpoint(self) -> str:
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
    def text2image(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        count: Optional[int] = 2,
    ) -> Text2ImageCreateApiResponse:
        request = Text2ImageRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            count=count,
        )
        return self.post(request=request, as_json=True)

    def get_text2image_result(self, inference_id: str) -> Text2ImageApiResponse:
        return self.get(postfix_url=f"inferences/{inference_id}")


class AsyncText2ImageClient(CommonText2ImageClient):

    async def text2image(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        count: Optional[int] = 2,
    ) -> Text2ImageCreateApiResponse:
        request = Text2ImageRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            count=count,
        )
        return await self.async_post(request=request, as_json=True)

    async def get_text2image_result(self, inference_id: str) -> Text2ImageApiResponse:
        return await self.async_get(postfix_url=f"inferences/{inference_id}")
