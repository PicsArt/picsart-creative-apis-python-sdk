import picsart_sdk
from picsart_sdk.clients import EffectsClient


def test_get_effects():
    client: EffectsClient = picsart_sdk.client("effects")
    client.get_effects()
