import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients import PaintingExpandClient

client: PaintingExpandClient = picsart_sdk.client(PicsartAPI.EXPAND)
response: PaintingApiResponse = client.expand(
    image_path="../tests/resources/image1.jpeg",
    prompt="a green field",
    mode="sync",
    count=2,  # it will generate two images
)

for item in response.data:
    print(item.url)

# see 24_2_inpainting_async.py for adapting it to mode="async".
