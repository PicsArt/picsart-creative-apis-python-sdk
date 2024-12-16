import time

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.text2image_response import (
    Text2ImageApiResponse,
    Text2ImageCreateApiResponse,
)
from picsart_sdk.clients import Text2ImageClient

client: Text2ImageClient = picsart_sdk.client(PicsartAPI.TEXT2IMAGE)
response1: Text2ImageCreateApiResponse = client.text2image(
    prompt="a cat in the green field",
    count=2,  # it will generate 2 images
)

while True:
    response2: Text2ImageApiResponse = client.get_result(response1.inference_id)
    if response2.status != "FINISHED":
        time.sleep(1)
        continue

    for item in response2.data:
        print(item.url)

    break
