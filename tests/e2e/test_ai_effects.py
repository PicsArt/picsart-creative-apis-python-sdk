import pytest

import picsart_sdk
from picsart_sdk.api_responses.effects_response import EffectsList
from picsart_sdk.clients import AiEffectsClient, AsyncAiEffectsClient


def test_get_ai_effects():
    client: AiEffectsClient = picsart_sdk.client("ai_effects")
    result = client.get_available_ai_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1


@pytest.mark.asyncio
async def test_get_effects_async():
    client: AsyncAiEffectsClient = picsart_sdk.async_client("ai_effects")
    result = await client.get_available_ai_effects()

    assert isinstance(result, EffectsList)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1
