import time

import picsart_sdk
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UploadClient

upload_client: UploadClient = picsart_sdk.client("upload")


response: ApiResponse = upload_client.upload_image(
    image_path="../tests/resources/image1.jpeg"
)
print(response.data.url)

# upload from an url (we use the previous url)
url = response.data.url
response: ApiResponse = upload_client.upload_image(image_url=url)
print(response.data.url)
