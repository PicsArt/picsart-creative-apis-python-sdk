import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses.effects_response import EffectsList
from picsart_sdk.clients import AsyncEffectsClient, EffectsClient
from picsart_sdk.clients.client_factory import ApiClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_get_effects():
    client: EffectsClient = picsart_sdk.client(ApiClient.EFFECTS)
    result = client.get_available_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.asyncio
async def test_get_effects_async():
    client: AsyncEffectsClient = picsart_sdk.async_client(ApiClient.EFFECTS)
    result = await client.get_available_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1
