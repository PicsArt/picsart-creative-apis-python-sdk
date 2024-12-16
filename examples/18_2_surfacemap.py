import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import SurfacemapClient, UploadClient

image_path = "../tests/resources/surfacemap/image.jpeg"
mask_path = "../tests/resources/surfacemap/mask.png"
sticker_path = "../tests/resources/surfacemap/sticker.jpeg"


def upload_images(image_path, mask_path, sticker_path):
    upload_client: UploadClient = picsart_sdk.client(PicsartAPI.UPLOAD)

    result = upload_client.upload_image(image_path=image_path)
    image_url = result.data.url

    result = upload_client.upload_image(image_path=mask_path)
    mask_url = result.data.url

    result = upload_client.upload_image(image_path=sticker_path)
    sticker_url = result.data.url

    return image_url, mask_url, sticker_url


image_url, mask_url, sticker_url = upload_images(image_path, mask_path, sticker_path)

client: SurfacemapClient = picsart_sdk.client(PicsartAPI.SURFACEMAP)
result1: ApiResponse = client.surfacemap(
    image_path=image_path, mask_path=mask_path, sticker_path=sticker_path
)

print(result1)

result2: ApiResponse = client.surfacemap(
    image_path=image_path, mask_url=mask_url, sticker_url=sticker_url
)

print(result2)
