from typing import Optional

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.api_responses.text2image_response import Text2ImageApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient
from picsart_sdk.clients.requests_models.text2image_request import Text2ImageRequest


class Text2ImageClient(GenAiBaseClient):
    @property
    def endpoint(self) -> str:
        return "text2image"

    def text2image(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: Optional[int] = 1024,
        height: Optional[int] = 1024,
        count: Optional[int] = 2,
    ) -> Text2ImageApiResponse:
        request = Text2ImageRequest(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            count=count,
        )
        return self.post(request=request, as_json=True)

    def parse_response(self, result) -> Text2ImageApiResponse:
        return Text2ImageApiResponse(**result)
