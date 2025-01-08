import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse

client = picsart_sdk.client(PicsartAPI.UPSCALE)

response: ApiResponse = client.upscale(
    image_path="../tests/resources/image1.jpeg", upscale_factor=2
)
print(response.data.url)
