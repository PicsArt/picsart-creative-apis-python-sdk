import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses.effects_responses import (
    EffectsPreviewsApiResponse,
    EffectsPreviewsApiResponseData,
)
from picsart_sdk.clients import AsyncEffectsPreviewsClient, EffectsPreviewsClient


def common_assertion(result, effect_names):
    assert isinstance(result, EffectsPreviewsApiResponse)
    assert result.status == "success"
    assert isinstance(result.data, list)
    assert len(result.data) == len(effect_names)
    assert set(item.effect_name for item in result.data) == set(effect_names)
    for item in result.data:
        assert isinstance(item, EffectsPreviewsApiResponseData)


def test_effects_previews():
    file_path = "../resources/image1.jpeg"
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))

    effect_names = ["apr1", "icy1"]
    client: EffectsPreviewsClient = picsart_sdk.client("effects_previews")
    result = client.effects_previews(image_path=image_path, effect_names=effect_names)

    common_assertion(result, effect_names)


@pytest.mark.asyncio
async def test_effects_previews_async():
    file_path = "../resources/image1.jpeg"
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))

    effect_names = ["apr1", "icy1"]
    client: AsyncEffectsPreviewsClient = picsart_sdk.async_client("effects_previews")
    result = await client.effects_previews(
        image_path=image_path, effect_names=effect_names
    )
    common_assertion(result, effect_names)
