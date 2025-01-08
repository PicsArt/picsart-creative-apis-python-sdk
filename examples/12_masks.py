import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import MasksClient

client: MasksClient = picsart_sdk.client(PicsartAPI.MASKS)
response: ApiResponse = client.masks(
    image_path="../tests/resources/image1.jpeg", mask="lace1"
)
print(response.data.url)
