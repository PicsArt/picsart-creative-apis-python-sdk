import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses import ApiResponse, ApiResponseData


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.parametrize(
    "client_name, method_name, image_path, image_url, extra_params",
    [
        (
            "remove_background",
            "remove_background",
            "../resources/image1.jpeg",
            None,
            None,
        ),
        (
            "remove_background",
            "remove_background",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            None,
        ),
        (
            "upscale",
            "upscale",
            "../resources/image1.jpeg",
            None,
            None,
        ),
        (
            "upscale",
            "upscale",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            None,
        ),
        ("ultra_upscale", "ultra_upscale", "../resources/image1.jpeg", None, None, ),
        (
            "ultra_upscale",
            "ultra_upscale",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            None,
        ),
        ("ultra_enhance", "ultra_enhance", "../resources/image1.jpeg", None, None, ),
        (
            "ultra_enhance",
            "ultra_enhance",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            None,
        ),
        ("face_enhancement", "face_enhancement", "../resources/image1.jpeg", None, None, ),
        (
            "face_enhancement",
            "face_enhancement",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            None,
        ),
        ("upload", "upload_image", "../resources/image1.jpeg", None, None, ),
        (
            "upload",
            "upload_image",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            None,
        ),
        (
            "effects",
            "effects",
            "../resources/image1.jpeg",
            None,
            {"effect_name": "apr1"},
        ),
        (
            "effects",
            "effects",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            {"effect_name": "apr1"},
        ),
    ],
)
def test_generic(client_name, method_name, image_path, image_url, extra_params):
    if extra_params is None:
        extra_params = {}

    client = picsart_sdk.client(client_name)

    params = {"image_url": image_url}
    if image_path:
        current_dir = os.path.dirname(__file__)
        params = {"image_path": os.path.abspath(os.path.join(current_dir, image_path))}

    function = getattr(client, method_name)
    result = function(**{**params, **extra_params})

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
