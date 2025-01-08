import time

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(PicsartAPI.ULTRA_UPSCALE)
response: ApiResponse = client.ultra_upscale(
    image_path="../tests/resources/image1.jpeg", mode=UltraUpscaleMode.ASYNC
)

inference_id = response.inference_id

while True:
    response: ApiResponse = client.get_result(inference_id=inference_id)
    print(response)
    if response.status == "success":
        print(response.data.url)
        break

    time.sleep(
        1
    )  # depending on the load of the service and the size of the image, the time to process can differ
