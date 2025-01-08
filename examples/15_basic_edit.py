import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import EditClient

image_path = "../tests/resources/image2.jpg"
client: EditClient = picsart_sdk.client(PicsartAPI.EDIT)
response: ApiResponse = client.edit(image_path=image_path, rotate=90)
print(response.data.url)
