import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import StyleTransferClient

path1 = "../tests/resources/image1.jpeg"
path2 = "../tests/resources/image2.jpg"
client: StyleTransferClient = picsart_sdk.client(PicsartAPI.STYLE_TRANSFER)
response: ApiResponse = client.style_transfer(
    image_path=path1, reference_image_path=path2
)
print(response.data.url)
