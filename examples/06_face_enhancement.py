import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import FaceEnhancementClient

client: FaceEnhancementClient = picsart_sdk.client(PicsartAPI.FACE_ENHANCEMENT)
response: ApiResponse = client.face_enhancement(image_path="./your-file.jpg")
print(response.data.url)
