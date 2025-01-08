import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.api_responses.effects_response import EffectsListApiResponse
from picsart_sdk.clients import EffectsClient

client: EffectsClient = picsart_sdk.client(PicsartAPI.EFFECTS)

# get the list of effects
response: EffectsListApiResponse = client.get_available_effects()
for effect_name in response.effects:
    print(effect_name)

# apply an effect
response: ApiResponse = client.effects(
    image_path="../tests/resources/image1.jpeg", effect_name="apr1"
)
print(response.data.url)
