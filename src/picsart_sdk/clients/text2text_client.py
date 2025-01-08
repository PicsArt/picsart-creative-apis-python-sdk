from typing import Optional

from picsart_sdk.api_responses.text2text_response import Text2TextApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient
from picsart_sdk.clients.requests_models import Text2TextRequest
from picsart_sdk.clients.requests_models.text2text_request import Text2ImageMessage


class CommonText2TextClient(GenAiBaseClient):
    @property
    def _endpoint(self) -> str:
        return "text2text/chat/completions"

    def parse_response(self, result: dict, request_method: str) -> Text2TextApiResponse:
        return Text2TextApiResponse(**result)


class Text2TextClient(CommonText2TextClient):
    """
    Client for generating text completions based on the user provided content.

    The Text2Text Completion service helps generate a text based on the text introduced as input by the user.
    """

    def chat_completions(
        self,
        content: str,
        role: str,
        max_tokens: Optional[int] = 512,
        temperature: Optional[int] = 1,
    ) -> Text2TextApiResponse:
        """
        Generate a chat-based text completion.

        :param content: The content of the message or prompt to process.
        :param role: The role of the message sender (e.g., "user", "assistant").
        :param max_tokens: The maximum number of tokens to generate. Default is 512.
        :param temperature: The sampling temperature to control randomness. Default is 1.
        :return: The API response containing the generated text completion.
        """
        message = Text2ImageMessage(
            content=content,
            role=role,
        )
        request = Text2TextRequest(
            max_tokens=max_tokens, temperature=temperature, messages=[message]
        )
        return self.post(request=request, as_json=True)


class AsyncText2TextClient(CommonText2TextClient):
    """
    Client for generating text completions based on the user-provided content, using an asynchronous HTTP client.

    The Text2Text Completion service helps generate a text based on the text introduced as input by the user.
    """

    async def chat_completions(
        self,
        content: str,
        role: str,
        max_tokens: Optional[int] = 512,
        temperature: Optional[int] = 1,
    ) -> Text2TextApiResponse:
        """
        Generate a chat-based text completion, using an asynchronous HTTP client.

        :param content: The content of the message or prompt to process.
        :param role: The role of the message sender (e.g., "user", "assistant").
        :param max_tokens: The maximum number of tokens to generate. Default is 512.
        :param temperature: The sampling temperature to control randomness. Default is 1.
        :return: The API response containing the generated text completion.
        """
        message = Text2ImageMessage(
            content=content,
            role=role,
        )
        request = Text2TextRequest(
            max_tokens=max_tokens, temperature=temperature, messages=[message]
        )
        return await self.async_post(request=request, as_json=True)
