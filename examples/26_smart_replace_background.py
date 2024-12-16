import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients import PaintingReplaceBackgroundClient

client: PaintingReplaceBackgroundClient = picsart_sdk.client(
    PicsartAPI.REPLACE_BACKGROUND
)
response: PaintingApiResponse = client.replace_background(
    image_path="../tests/resources/painting/inpainting_image.jpeg",
    prompt="a green field",
    mode="sync",
    count=2,  # it will generate two images
)

for item in response.data:
    print(item.url)

# see 24_2_inpainting_async.py for adapting it to mode="async".
