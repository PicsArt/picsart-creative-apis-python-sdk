import pytest

import picsart_sdk
from picsart_sdk.api_responses import EffectsListApiResponse
from picsart_sdk.clients import AiEffectsClient, AsyncAiEffectsClient


def test_get_ai_effects():
    client: AiEffectsClient = picsart_sdk.client("ai_effects")
    result = client.get_available_ai_effects()

    assert isinstance(result, EffectsListApiResponse)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1


@pytest.mark.asyncio
async def test_get_effects_async():
    client: AsyncAiEffectsClient = picsart_sdk.async_client("ai_effects")
    result = await client.get_available_ai_effects()

    assert isinstance(result, EffectsListApiResponse)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1
