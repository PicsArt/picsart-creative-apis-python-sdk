from unittest.mock import MagicMock

import pytest

from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import (
    AdjustClient,
    AiEffectsClient,
    BleedClient,
    ColorTransferClient,
    EditClient,
    EffectsClient,
    FaceEnhancementClient,
    MasksClient,
    StyleTransferClient,
    SurfacemapClient,
    TextureGeneratorClient,
    UltraEnhanceClient,
    UltraUpscaleClient,
    UploadClient,
    UpscaleClient,
)
from picsart_sdk.clients.http_clients import HttpClient
from picsart_sdk.clients.remove_background_client import RemoveBackgroundClient
from picsart_sdk.errors import ApiError


@pytest.fixture
def http_client():
    return MagicMock(spec=HttpClient)


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


@pytest.mark.parametrize(
    "client_class, method_name, params",
    [
        (
            RemoveBackgroundClient,
            "remove_background",
            {"image_url": "https://example.com/image.png"},
        ),
        (UpscaleClient, "upscale", {"image_url": "https://example.com/image.png"}),
        (
            AdjustClient,
            "adjust",
            {"image_url": "https://example.com/image.png", "contrast": 50},
        ),
        (
            AiEffectsClient,
            "ai_effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            BleedClient,
            "bleed",
            {"image_url": "https://example.com/image.png", "bleed_size": 10},
        ),
        (
            ColorTransferClient,
            "color_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            EditClient,
            "edit",
            {"image_url": "https://example.com/image.png", "rotate": 45},
        ),
        (
            EffectsClient,
            "effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            FaceEnhancementClient,
            "face_enhancement",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            MasksClient,
            "masks",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            StyleTransferClient,
            "style_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            SurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
                "sticker_url": "https://example.com/image3.png",
            },
        ),
        (
            TextureGeneratorClient,
            "texture_generator",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UltraEnhanceClient,
            "ultra_enhance",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UltraUpscaleClient,
            "ultra_upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UploadClient,
            "upload_image",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UpscaleClient,
            "upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
    ],
)
def test_call_client_success(
    client_class, method_name, params, session, http_client, mock_response_data
):
    client = client_class(session=session, http_client=http_client)
    client.http_client.post.return_value = mock_response_data

    function = getattr(client, method_name)
    response = function(**params)

    assert isinstance(response, ApiResponse)
    assert response.status == "success"
    assert response.data.url == "https://example.com/image.png"
    assert response.data.id == "12345"
    assert response.transaction_id is None
    client.http_client.post.assert_called_once()


@pytest.mark.parametrize(
    "client_class, method_name, params",
    [
        (
            RemoveBackgroundClient,
            "remove_background",
            {"image_url": "https://example.com/image.png"},
        ),
        (UpscaleClient, "upscale", {"image_url": "https://example.com/image.png"}),
        (
            AdjustClient,
            "adjust",
            {"image_url": "https://example.com/image.png", "contrast": 50},
        ),
        (
            AiEffectsClient,
            "ai_effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            BleedClient,
            "bleed",
            {"image_url": "https://example.com/image.png", "bleed_size": 10},
        ),
        (
            ColorTransferClient,
            "color_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            EditClient,
            "edit",
            {"image_url": "https://example.com/image.png", "rotate": 45},
        ),
        (
            EffectsClient,
            "effects",
            {"image_url": "https://example.com/image.png", "effect_name": "test"},
        ),
        (
            FaceEnhancementClient,
            "face_enhancement",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            MasksClient,
            "masks",
            {"image_url": "https://example.com/image.png"},
        ),
        (
            StyleTransferClient,
            "style_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_url": "https://example.com/image2.png",
            },
        ),
        (
            SurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
                "sticker_url": "https://example.com/image3.png",
            },
        ),
        (
            TextureGeneratorClient,
            "texture_generator",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UltraEnhanceClient,
            "ultra_enhance",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UltraUpscaleClient,
            "ultra_upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UploadClient,
            "upload_image",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
        (
            UpscaleClient,
            "upscale",
            {
                "image_url": "https://example.com/image.png",
            },
        ),
    ],
)
def test_remove_background_api_error(
    client_class, method_name, params, session, http_client
):
    client = client_class(session=session, http_client=http_client)

    client.http_client.post.side_effect = ApiError(
        detail="API call failed", message="API call failed", code=123
    )

    function = getattr(client, method_name)

    with pytest.raises(ApiError) as exc_info:
        function(**params)

    assert exc_info.value.code == 123

    client.http_client.post.assert_called_once()


@pytest.mark.parametrize(
    "client_class, method_name, params, error_message",
    [
        (
            StyleTransferClient,
            "style_transfer",
            {"image_url": "https://example.com/image.png"},
            "At least one of `reference_image_url`, or `reference_image_path` must be provided.",
        ),
        (
            SurfacemapClient,
            "surfacemap",
            {"image_url": "https://example.com/image.png"},
            "At least one of `mask_url`, or `mask_path` must be provided.",
        ),
        (
            SurfacemapClient,
            "surfacemap",
            {
                "image_url": "https://example.com/image.png",
                "mask_url": "https://example.com/image2.png",
            },
            "At least one of `sticker_url`, or `sticker_path` must be provided.",
        ),
        (
            StyleTransferClient,
            "style_transfer",
            {"image_url": "https://example.com/image.png"},
            "At least one of `reference_image_url`, or `reference_image_path` must be provided.",
        ),
        (
            ColorTransferClient,
            "color_transfer",
            {"image_url": "https://example.com/image.png"},
            "At least one of `reference_image_url`, or `reference_image_path` must be provided.",
        ),
    ],
)
def test_missing_param(
    client_class, method_name, params, error_message, session, http_client
):
    client = client_class(session=session, http_client=http_client)
    function = getattr(client, method_name)
    with pytest.raises(ValueError) as exc_info:
        function(**params)

    assert exc_info.value.args[0] == error_message


@pytest.mark.parametrize(
    "client_class, method_name, params, error_message",
    [
        (
            RemoveBackgroundClient,
            "remove_background",
            {"image_url": "https://example.com/image.png", "image_path": "./file.png"},
            "Only one of `image_url`, or `image_path` can be provided.",
        ),
        (
            StyleTransferClient,
            "style_transfer",
            {
                "image_url": "https://example.com/image.png",
                "reference_image_path": "./file.png",
                "reference_image_url": "https://example.com/image2.png",
            },
            "Only one of `reference_image_url`, or `reference_image_path` can be provided.",
        ),
        (
            SurfacemapClient,
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
def test_image_url_and_image_path(
    client_class, method_name, params, error_message, session, http_client
):
    client = client_class(session=session, http_client=http_client)
    function = getattr(client, method_name)
    with pytest.raises(ValueError) as exc_info:
        function(**params)
    assert exc_info.value.args[0] == error_message
