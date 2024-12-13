import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses import EffectsListApiResponse
from picsart_sdk.clients import AiEffectsClient, AsyncAiEffectsClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_get_ai_effects():
    client: AiEffectsClient = picsart_sdk.client("ai_effects")
    result = client.get_available_ai_effects()

    assert isinstance(result, EffectsListApiResponse)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.asyncio
async def test_get_effects_async():
    client: AsyncAiEffectsClient = picsart_sdk.async_client("ai_effects")
    result = await client.get_available_ai_effects()

    assert isinstance(result, EffectsListApiResponse)
    assert isinstance(result.effects, list)
    assert len(result.effects) >= 1
