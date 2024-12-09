import os

import pytest

import picsart_sdk
from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.clients.client_factory import ApiClient
from picsart_sdk.clients.upload_client import UploadClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.parametrize(
    "image_path, image_url",
    [
        ("../resources/image1.jpeg", None),
        (
            None,
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
    ],
)
def test_upload(image_path, image_url):
    client: UploadClient = picsart_sdk.client(ApiClient.UPLOAD)

    if image_path:
        current_dir = os.path.dirname(__file__)
        params = {"image_path": os.path.abspath(os.path.join(current_dir, image_path))}
    else:
        params = {"image_url": image_url}

    result = client.upload_image(**params)

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
