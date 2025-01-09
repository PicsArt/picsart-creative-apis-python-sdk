import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.masks_previews_response import MasksPreviewsApiResponse
from picsart_sdk.clients import MasksPreviewsClient

client: MasksPreviewsClient = picsart_sdk.client(PicsartAPI.MASKS_PREVIEWS)
response: MasksPreviewsApiResponse = client.masks_previews(
    image_path="../tests/resources/image1.jpeg", mask=["lace1", "lace2"]
)
print(response.data[0].mask, response.data[0].url)
print(response.data[0].mask, response.data[1].url)
