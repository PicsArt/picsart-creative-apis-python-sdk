import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.image_tagging_api_response import ImageTaggingApiResponse
from picsart_sdk.clients import ImageTaggingClient

image_path = "../tests/resources/image1.jpeg"
client: ImageTaggingClient = picsart_sdk.client(PicsartAPI.IMAGE_TAGGING)
response: ImageTaggingApiResponse = client.get_tags(image_path=image_path)
print(response.data.tags)
