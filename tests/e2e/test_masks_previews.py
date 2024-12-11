import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses.masks_previews_response import (
    MasksPreviewsApiResponse,
    MasksPreviewsApiResponseData,
)
from picsart_sdk.clients import AsyncMasksPreviewsClient, MasksPreviewsClient
from picsart_sdk.clients.client_factory import ApiClient


def common_assertion(result, masks):
    assert isinstance(result, MasksPreviewsApiResponse)
    assert result.status == "success"
    assert isinstance(result.data, list)
    assert len(result.data) == len(masks)

    # the api doesn't return the mask name when there is only one mask requested
    assert set(item.mask for item in result.data) == set(masks)

    for item in result.data:
        assert isinstance(item, MasksPreviewsApiResponseData)


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.parametrize(
    "mask, expected_masks",
    [
        (["lace1", "lace2"], ["lace1", "lace2"]),
        (None, [""]),
        ([], [""]),
        ("lace1", [""]),
    ],
)
def test_masks_previews(mask, expected_masks):
    file_path = "../resources/image1.jpeg"
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))

    client: MasksPreviewsClient = picsart_sdk.client(ApiClient.MASKS_PREVIEWS)
    result = client.masks_previews(image_path=image_path, mask=mask)
    common_assertion(result, expected_masks)


@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.parametrize(
    "mask, expected_masks",
    [
        (["lace1", "lace2"], ["lace1", "lace2"]),
        (None, [""]),
        ([], [""]),
        ("lace1", [""]),
    ],
)
async def test_masks_previews_async(mask, expected_masks):
    file_path = "../resources/image1.jpeg"
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))

    client: MasksPreviewsClient = picsart_sdk.client(ApiClient.MASKS_PREVIEWS)
    result = client.masks_previews(image_path=image_path, mask=mask)
    common_assertion(result, expected_masks)
