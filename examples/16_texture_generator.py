import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import TextureGeneratorClient

image_path = "../tests/resources/image2.jpg"
client: TextureGeneratorClient = picsart_sdk.client(PicsartAPI.TEXTURE_GENERATOR)
response: ApiResponse = client.texture_generator(image_path=image_path)
print(response.data.url)
