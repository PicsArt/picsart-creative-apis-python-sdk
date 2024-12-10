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
        # (
        #     "remove_background",
        #     "remove_background",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "remove_background",
        #     "remove_background",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "upscale",
        #     "upscale",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "upscale",
        #     "upscale",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "ultra_upscale",
        #     "ultra_upscale",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "ultra_upscale",
        #     "ultra_upscale",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "ultra_enhance",
        #     "ultra_enhance",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "ultra_enhance",
        #     "ultra_enhance",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "face_enhancement",
        #     "face_enhancement",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "face_enhancement",
        #     "face_enhancement",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "upload",
        #     "upload_image",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "upload",
        #     "upload_image",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "effects",
        #     "effects",
        #     "../resources/image1.jpeg",
        #     None,
        #     {"effect_name": "apr1"},
        # ),
        # (
        #     "effects",
        #     "effects",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     {"effect_name": "apr1"},
        # ),
        # (
        #     "ai_effects",
        #     "ai_effects",
        #     "../resources/image1.jpeg",
        #     None,
        #     {"effect_name": "winterblues"},
        # ),
        # (
        #     "ai_effects",
        #     "ai_effects",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     {"effect_name": "winterblues"},
        # ),
        # (
        #     "color_transfer",
        #     "color_transfer",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/e8a93f25-ea57-4a6c-aaf9-4032cac5ed2b.jpg",  # image2.jpg
        #     {
        #         "reference_image_url": "https://pastatic.picsart.com/cms-pastatic/d68aa804-0d8b-412c-9507-32df9f167da4.jpg"  # image3.jpg
        #     },
        # ),
        # (
        #     "color_transfer",
        #     "color_transfer",
        #     "../resources/image2.jpg",
        #     None,
        #     {"reference_image_path": "../resources/image3.jpg"},
        # ),
        # (
        #     "style_transfer",
        #     "style_transfer",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/e8a93f25-ea57-4a6c-aaf9-4032cac5ed2b.jpg",  # image2.jpg
        #     {
        #         "reference_image_url": "https://pastatic.picsart.com/cms-pastatic/d68aa804-0d8b-412c-9507-32df9f167da4.jpg"  # image3.jpg
        #     },
        # ),
        # (
        #     "style_transfer",
        #     "style_transfer",
        #     "../resources/image2.jpg",
        #     None,
        #     {"reference_image_path": "../resources/image3.jpg"},
        # ),
        # (
        #     "masks",
        #     "masks",
        #     "../resources/image1.jpeg",
        #     None,
        #     None,
        # ),
        # (
        #     "masks",
        #     "masks",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     None,
        # ),
        # (
        #     "adjust",
        #     "adjust",
        #     "../resources/image1.jpeg",
        #     None,
        #     {"brightness": 50},
        # ),
        # (
        #     "adjust",
        #     "adjust",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     {"brightness": 50},
        # ),
        # (
        #     "edit",
        #     "edit",
        #     "../resources/image1.jpeg",
        #     None,
        #     {"flip": "horizontal"},
        # ),
        # (
        #     "edit",
        #     "edit",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     {"flip": "horizontal"},
        # ),
        # (
        #     "texture_generator",
        #     "texture_generator",
        #     "../resources/image1.jpeg",
        #     None,
        #     {"rotate": 90},
        # ),
        # (
        #     "texture_generator",
        #     "texture_generator",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     {"rotate": 90},
        # ),
        # (
        #     "vectorizer",
        #     "vectorizer",
        #     "../resources/image1.jpeg",
        #     None,
        #     {"downscale_to": 500},
        # ),
        # (
        #     "vectorizer",
        #     "vectorizer",
        #     None,
        #     "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        #     {"downscale_to": 500},
        # ),
        (
            "bleed",
            "bleed",
            "../resources/image1.jpeg",
            None,
            {
                "bleed_size": 10,
            },
        ),
        (
            "bleed",
            "bleed",
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
            {
                "bleed_size": 10,
            },
        ),
    ],
)
def test_generic(client_name, method_name, image_path, image_url, extra_params):
    if extra_params is None:
        extra_params = {}

    client = picsart_sdk.client(client_name)

    params = {"image_url": image_url}
    if image_path:
        params = {
            "image_path": os.path.abspath(
                os.path.join(os.path.dirname(__file__), image_path)
            )
        }

    reference_image_path = extra_params.get("reference_image_path")
    if reference_image_path:
        params["reference_image_path"] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), reference_image_path)
        )
        del extra_params["reference_image_path"]

    function = getattr(client, method_name)
    data = {**params, **extra_params}
    result = function(**data)

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
