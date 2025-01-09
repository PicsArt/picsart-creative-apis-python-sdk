import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import AdjustClient

image_path = "../tests/resources/image1.jpeg"
client: AdjustClient = picsart_sdk.client(PicsartAPI.ADJUST)
response: ApiResponse = client.adjust(image_path=image_path, contrast=50, noise=90)
print(response.data.url)
