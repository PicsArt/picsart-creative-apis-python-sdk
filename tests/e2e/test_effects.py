import pytest

import picsart_sdk
from picsart_sdk.api_responses.effects_responses import EffectsList
from picsart_sdk.clients import AsyncEffectsClient, EffectsClient


def test_get_effects():
    client: EffectsClient = picsart_sdk.client("effects")
    result = client.get_available_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1


@pytest.mark.asyncio
async def test_get_effects_async():
    client: AsyncEffectsClient = picsart_sdk.async_client("effects")
    result = await client.get_available_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1
