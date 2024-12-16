import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients import OutpaintingClient

client: OutpaintingClient = picsart_sdk.client(PicsartAPI.OUTPAINTING)
response: PaintingApiResponse = client.outpainting(
    image_path="../tests/resources/painting/inpainting_image.jpeg",
    mask_path="../tests/resources/painting/inpainting_mask.png",
    prompt="a green logo",
    mode="sync",
    count=2,  # it will generate two images
)

for item in response.data:
    print(item.url)

# see 24_2_inpainting_async.py for adapting it to mode="async".
