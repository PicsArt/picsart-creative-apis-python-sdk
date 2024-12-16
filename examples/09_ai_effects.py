import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import AiEffectsClient

client: AiEffectsClient = picsart_sdk.client(PicsartAPI.AI_EFFECTS)

# get the list of available effects
effects = client.get_available_ai_effects()
print(effects.effects)

# apply an effect
response: ApiResponse = client.ai_effects(
    image_path="../tests/resources/image1.jpeg", effect_name="winterblues"
)
print(response.data.url)
