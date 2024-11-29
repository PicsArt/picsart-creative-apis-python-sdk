import picsart_sdk
from picsart_sdk.api_responses.effects_responses import EffectsList
from picsart_sdk.clients import EffectsClient


def test_get_effects():
    client: EffectsClient = picsart_sdk.client("effects")
    result = client.get_available_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1
