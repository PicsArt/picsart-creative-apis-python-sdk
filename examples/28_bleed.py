import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import BleedClient

client: BleedClient = picsart_sdk.client(PicsartAPI.BLEED)
res = client.bleed(
    image_path="../tests/resources/painting/inpainting_image.jpeg", bleed_size=30
)
print(res)
