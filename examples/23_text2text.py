import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.text2text_response import Text2TextApiResponse
from picsart_sdk.clients import Text2TextClient

client: Text2TextClient = picsart_sdk.client(PicsartAPI.TEXT2TEXT)
response: Text2TextApiResponse = client.chat_completions(
    role="assistant", content="what is cat?"
)
print(response.data)
