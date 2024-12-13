from unittest.mock import AsyncMock, MagicMock

import pytest

from picsart_sdk import AsyncHttpClient
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import (
    AsyncAdjustClient,
    AsyncAiEffectsClient,
    AsyncBleedClient,
    AsyncColorTransferClient,
    AsyncEditClient,
    AsyncEffectsClient,
    AsyncFaceEnhancementClient,
    AsyncMasksClient,
    AsyncStyleTransferClient,
    AsyncSurfacemapClient,
    AsyncTextureGeneratorClient,
    AsyncUltraEnhanceClient,
    AsyncUltraUpscaleClient,
    AsyncUploadClient,
    AsyncUpscaleClient,
)
from picsart_sdk.clients.remove_background_client import AsyncRemoveBackgroundClient
from picsart_sdk.errors import ApiError


@pytest.fixture
def http_client():
    return AsyncMock(spec=AsyncHttpClient)


@pytest.fixture
def session():
    return MagicMock(api_key="test_api_key")


@pytest.fixture
def mock_response_data():
    return {
        "status": "success",
        "data": {"url": "https://example.com/image.png", "id": "12345"},
        "transaction_id": None,
    }


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_class, method_name, params",
    [
        (
            AsyncRemoveBackgroundClient,
            "remove_background",
            {"image_url": "https://example.com/image.png"},
        ),
        (AsyncUpscaleClient, "upscale", {"image_url": "https://example.com/image.png"}),
        (
            AsyncAdjustClient,
            "adjust",
            {"image_url": "https://example.com/image.png", "contrast": 50},
        ),
        (
            AsyncAiEffectsClient,
            "ai_effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            AsyncBleedClient,
            "bleed",
            {"image_url": "https://example.com/image.png", "bleed_size": 10},
        ),
        (
            AsyncColorTransferClient,
            "color_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            AsyncEditClient,
            "edit",
            {"image_url": "https://example.com/image.png", "rotate": 45},
        ),
        (
            AsyncEffectsClient,
            "effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            AsyncFaceEnhancementClient,
            "face_enhancement",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            AsyncMasksClient,
            "masks",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            AsyncStyleTransferClient,
            "style_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            AsyncSurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
                "sticker_url": "https://example.com/image3.png",
            },
        ),
        (
            AsyncTextureGeneratorClient,
            "texture_generator",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUltraEnhanceClient,
            "ultra_enhance",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUltraUpscaleClient,
            "ultra_upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUploadClient,
            "upload_image",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUpscaleClient,
            "upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
    ],
)
async def test_call_client_success(
    client_class, method_name, params, session, http_client, mock_response_data
):
    client = client_class(session=session, http_client=http_client)
    client.http_client.post.return_value = mock_response_data

    function = getattr(client, method_name)
    response = await function(**params)

    assert isinstance(response, ApiResponse)
    assert response.status == "success"
    assert response.data.url == "https://example.com/image.png"
    assert response.data.id == "12345"
    assert response.transaction_id is None
    client.http_client.post.assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_class, method_name, params",
    [
        (
            AsyncRemoveBackgroundClient,
            "remove_background",
            {"image_url": "https://example.com/image.png"},
        ),
        (AsyncUpscaleClient, "upscale", {"image_url": "https://example.com/image.png"}),
        (
            AsyncAdjustClient,
            "adjust",
            {"image_url": "https://example.com/image.png", "contrast": 50},
        ),
        (
            AsyncAiEffectsClient,
            "ai_effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            AsyncBleedClient,
            "bleed",
            {"image_url": "https://example.com/image.png", "bleed_size": 10},
        ),
        (
            AsyncColorTransferClient,
            "color_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            AsyncEditClient,
            "edit",
            {"image_url": "https://example.com/image.png", "rotate": 45},
        ),
        (
            AsyncEffectsClient,
            "effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            AsyncFaceEnhancementClient,
            "face_enhancement",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            AsyncMasksClient,
            "masks",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            AsyncStyleTransferClient,
            "style_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            AsyncSurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
                "sticker_url": "https://example.com/image3.png",
            },
        ),
        (
            AsyncTextureGeneratorClient,
            "texture_generator",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUltraEnhanceClient,
            "ultra_enhance",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUltraUpscaleClient,
            "ultra_upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUploadClient,
            "upload_image",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            AsyncUpscaleClient,
            "upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
    ],
)
async def test_remove_background_api_error(
    client_class, method_name, params, session, http_client
):
    client = client_class(session=session, http_client=http_client)

    client.http_client.post.side_effect = ApiError(
        detail="API call failed", message="API call failed", code=123
    )

    function = getattr(client, method_name)

    with pytest.raises(ApiError) as exc_info:
        await function(**params)

    assert exc_info.value.code == 123

    client.http_client.post.assert_called_once()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_class, method_name, params, error_message",
    [
        (
            AsyncStyleTransferClient,
            "style_transfer",
            {"image_url": "https://example.com/image.png"},
            "At least one of `reference_image_url`, or `reference_image_path` must be provided.",
        ),
        (
            AsyncSurfacemapClient,
            "surfacemap",
            {"image_url": "https://example.com/image.png"},
            "At least one of `mask_url`, or `mask_path` must be provided.",
        ),
        (
            AsyncSurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
            },
            "At least one of `sticker_url`, or `sticker_path` must be provided.",
        ),
        (
            AsyncStyleTransferClient,
            "style_transfer",
            {"image_url": "https://example.com/image.png"},
            "At least one of `reference_image_url`, or `reference_image_path` must be provided.",
        ),
        (
            AsyncColorTransferClient,
            "color_transfer",
            {"image_url": "https://example.com/image.png"},
            "At least one of `reference_image_url`, or `reference_image_path` must be provided.",
        ),
    ],
)
async def test_missing_param(
    client_class, method_name, params, error_message, session, http_client
):
    client = client_class(session=session, http_client=http_client)
    function = getattr(client, method_name)
    with pytest.raises(ValueError) as exc_info:
        await function(**params)

    assert exc_info.value.args[0] == error_message


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_class, method_name, params, error_message",
    [
        (
            AsyncRemoveBackgroundClient,
            "remove_background",
            {"image_url": "https://example.com/image.png", "image_path": "./file.png"},
            "Only one of `image_url`, or `image_path` can be provided.",
        ),
        (
            AsyncStyleTransferClient,
            "style_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_path": "./file.png",
                "reference_image_url": "https://example.com/image2.png",
            },
            "Only one of `reference_image_url`, or `reference_image_path` can be provided.",
        ),
        (
            AsyncSurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
                "sticker_url": "https://example.com/image3.png",
                "sticker_path": "./file.png",
            },
            "Only one of `sticker_url`, or `sticker_path` can be provided.",
        ),
    ],
)
async def test_image_url_and_image_path(
    client_class, method_name, params, error_message, session, http_client
):
    client = client_class(session=session, http_client=http_client)
    function = getattr(client, method_name)
    with pytest.raises(ValueError) as exc_info:
        await function(**params)
    assert exc_info.value.args[0] == error_message
