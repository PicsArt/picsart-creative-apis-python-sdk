import picsart_sdk
from picsart_sdk.api_responses.text2text_response import Text2TextApiResponse
from picsart_sdk.clients.client_factory import ApiClient
from picsart_sdk.clients.text2text_client import Text2TextClient


def test_create_text2text():
    client: Text2TextClient = picsart_sdk.client(ApiClient.TEXT2TEXT)

    result = client.chat_completions(content="generate a test text", role="assistant")
    assert isinstance(result, Text2TextApiResponse)
    assert result.status == "DONE"
    assert isinstance(result.data, str)
