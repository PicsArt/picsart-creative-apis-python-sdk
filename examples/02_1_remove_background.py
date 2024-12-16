import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import RemoveBackgroundClient

client: RemoveBackgroundClient = picsart_sdk.client(PicsartAPI.REMOVE_BACKGROUND)

# remove background of an image from local disk
response: ApiResponse = client.remove_background(
    image_path="../tests/resources/image1.jpeg"
)
print(response.data.url)
url = response.data.url

# remove background from URL
response = client.remove_background(image_url=url)
print(response.data.url)
