import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.image_description_api_response import (
    ImageDescriptionApiResponse,
)
from picsart_sdk.clients import ImageDescriptionClient

image_path = "../tests/resources/image1.jpeg"
client: ImageDescriptionClient = picsart_sdk.client(PicsartAPI.IMAGE_DESCRIPTION)
response: ImageDescriptionApiResponse = client.get_description(image_path=image_path)
print(response.data.description)
