import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import ColorTransferClient

path1 = "../tests/resources/image1.jpeg"
path2 = "../tests/resources/image3.jpg"
client: ColorTransferClient = picsart_sdk.client(PicsartAPI.COLOR_TRANSFER)
response: ApiResponse = client.color_transfer(
    image_path=path1, reference_image_path=path2
)
print(response.data.url)
