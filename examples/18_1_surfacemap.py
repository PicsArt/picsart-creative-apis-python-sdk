import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import SurfacemapClient

image_path = "../tests/resources/surfacemap/image.jpeg"
mask_path = "../tests/resources/surfacemap/mask.png"
sticker_path = "../tests/resources/surfacemap/sticker.jpeg"

client: SurfacemapClient = picsart_sdk.client(PicsartAPI.SURFACEMAP)
result: ApiResponse = client.surfacemap(
    image_path=image_path, mask_path=mask_path, sticker_path=sticker_path
)

print(result)
