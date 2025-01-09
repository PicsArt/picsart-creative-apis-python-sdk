import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import RemoveBackgroundClient

client: RemoveBackgroundClient = picsart_sdk.client(PicsartAPI.REMOVE_BACKGROUND)

# remove the background and apply a stroke effect with a 2px red border
response: ApiResponse = client.remove_background(
    image_path="../tests/resources/image1.jpeg", stroke_size=2, stroke_color="red"
)
print(response.data.url)
