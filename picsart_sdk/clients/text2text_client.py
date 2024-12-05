from typing import Optional

from picsart_sdk.api_responses.text2text_response import Text2TextApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient
from picsart_sdk.clients.requests_models import Text2TextRequest
from picsart_sdk.clients.requests_models.text2text_request import Text2ImageMessage


class CommonText2TextClient(GenAiBaseClient):
    @property
    def endpoint(self) -> str:
        return "text2text/chat/completions"

    def parse_response(self, result) -> Text2TextApiResponse:
        return Text2TextApiResponse(**result)


class Text2TextClient(CommonText2TextClient):

    def chat_completions(
        self,
        content: str,
        role: str,
        max_tokens: Optional[int] = 512,
        temperature: Optional[int] = 1,
    ) -> Text2TextApiResponse:
        message = Text2ImageMessage(
            content=content,
            role=role,
        )
        request = Text2TextRequest(
            max_tokens=max_tokens, temperature=temperature, messages=[message]
        )
        return self.post(request=request, as_json=True)

    def parse_response(self, result) -> Text2TextApiResponse:
        return Text2TextApiResponse(**result)


class AsyncText2TextClient(CommonText2TextClient):
    @property
    def endpoint(self) -> str:
        return "text2text/chat/completions"

    async def chat_completions(
        self,
        content: str,
        role: str,
        max_tokens: Optional[int] = 512,
        temperature: Optional[int] = 1,
    ) -> Text2TextApiResponse:
        message = Text2ImageMessage(
            content=content,
            role=role,
        )
        request = Text2TextRequest(
            max_tokens=max_tokens, temperature=temperature, messages=[message]
        )
        return await self.async_post(request=request, as_json=True)
