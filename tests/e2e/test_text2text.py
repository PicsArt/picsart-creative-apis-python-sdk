import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses.text2text_response import Text2TextApiResponse
from picsart_sdk.clients.client_factory import ApiClient
from picsart_sdk.clients.text2text_client import AsyncText2TextClient, Text2TextClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_create_text2text():
    client: Text2TextClient = picsart_sdk.client(ApiClient.TEXT2TEXT)

    result = client.chat_completions(content="generate a test text", role="assistant")
    assert isinstance(result, Text2TextApiResponse)
    assert result.status == "DONE"
    assert isinstance(result.data, str)


@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
async def test_create_text2text_async():
    client: AsyncText2TextClient = picsart_sdk.async_client(ApiClient.TEXT2TEXT)

    result = await client.chat_completions(
        content="generate a test text", role="assistant"
    )
    assert isinstance(result, Text2TextApiResponse)
    assert result.status == "DONE"
    assert isinstance(result.data, str)
