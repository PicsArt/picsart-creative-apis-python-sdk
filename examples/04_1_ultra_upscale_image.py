import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(PicsartAPI.ULTRA_UPSCALE)

# upscale using synchronous mode
response: ApiResponse = client.ultra_upscale(
    image_path="../tests/resources/image1.jpeg", mode=UltraUpscaleMode.SYNC
)
print(response.data.url)
