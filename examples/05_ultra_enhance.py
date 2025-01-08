import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UltraEnhanceClient

client: UltraEnhanceClient = picsart_sdk.client(PicsartAPI.ULTRA_ENHANCE)
response: ApiResponse = client.ultra_enhance(
    image_path="../tests/resources/image1.jpeg"
)
print(response.data.url)
