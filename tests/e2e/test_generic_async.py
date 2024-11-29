import os

import pytest

import picsart_sdk
from picsart_sdk.api_response import ApiResponse, ApiResponseData
from picsart_sdk.clients.remove_background_client import RemoveBackgroundClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_name, method_name, image_path, image_url",
    [
        ("remove_background", "remove_background", "../resources/image1.jpeg", None),
        (
            "remove_background",
            "remove_background",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
        ("upscale", "upscale", "../resources/image1.jpeg", None),
        (
            "upscale",
            "upscale",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
        ("ultra_upscale", "ultra_upscale", "../resources/image1.jpeg", None),
        (
                "ultra_upscale",
                "ultra_upscale",
                None,
                "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
        ("ultra_enhance", "ultra_enhance", "../resources/image1.jpeg", None),
        (
                "ultra_enhance",
                "ultra_enhance",
                None,
                "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
        ("face_enhancement", "face_enhancement", "../resources/image1.jpeg", None),
        (
                "face_enhancement",
                "face_enhancement",
                None,
                "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
        ("upload", "upload_image", "../resources/image1.jpeg", None),
        (
                "upload",
                "upload_image",
                None,
                "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
    ],
)
async def test_generic_async(client_name, method_name, image_path, image_url):
    client: RemoveBackgroundClient = picsart_sdk.async_client(client_name)

    params = {"image_url": image_url}
    if image_path:
        current_dir = os.path.dirname(__file__)
        params = {"image_path": os.path.abspath(os.path.join(current_dir, image_path))}

    function = getattr(client, method_name)
    result = await function(**params)

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
