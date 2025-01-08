import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import VectorizerClient

image_path = "../tests/resources/image2.jpg"
client: VectorizerClient = picsart_sdk.client(PicsartAPI.VECTORIZER)
response: ApiResponse = client.vectorizer(image_path=image_path)
print(response.data.url)
