import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.effects_response import EffectsPreviewsApiResponse
from picsart_sdk.clients import EffectsPreviewsClient

client: EffectsPreviewsClient = picsart_sdk.client(PicsartAPI.EFFECTS_PREVIEWS)
response: EffectsPreviewsApiResponse = client.effects_previews(
    image_path="../tests/resources/image1.jpeg", effect_names=["apr1", "brnz3"]
)
for item in response.data:
    print(item.effect_name, item.url)
