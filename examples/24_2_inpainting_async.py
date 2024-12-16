import time

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.painting_response import PaintingApiResponse
from picsart_sdk.clients import InpaintingClient

client: InpaintingClient = picsart_sdk.client(PicsartAPI.INPAINTING)
response: PaintingApiResponse = client.inpainting(
    image_path="../tests/resources/painting/inpainting_image.jpeg",
    mask_path="../tests/resources/painting/inpainting_mask.png",
    prompt="a green logo",
    mode="async",  # <- ask for results asynchronously
    count=2,
)


while True:
    response: PaintingApiResponse = client.get_result(
        inference_id=response.inference_id
    )

    if not response.data:
        time.sleep(1)
        continue

    for item in response.data:
        print(item.url)

    break
