import os

import pytest

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.clients import AsyncSurfacemapClient, SurfacemapClient


@pytest.fixture
def image_path():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../resources/surfacemap/image.jpeg")
    )


@pytest.fixture
def mask_path():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../resources/surfacemap/mask.png")
    )


@pytest.fixture
def sticker_path():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../resources/surfacemap/sticker.jpeg")
    )


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_surfacemap(image_path, mask_path, sticker_path):
    client: SurfacemapClient = picsart_sdk.client(PicsartAPI.SURFACEMAP)
    result = client.surfacemap(
        image_path=image_path, mask_path=mask_path, sticker_path=sticker_path
    )

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0


@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
async def test_surfacemap_async(image_path, mask_path, sticker_path):
    client: AsyncSurfacemapClient = picsart_sdk.async_client(PicsartAPI.SURFACEMAP)
    result = await client.surfacemap(
        image_path=image_path, mask_path=mask_path, sticker_path=sticker_path
    )

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
