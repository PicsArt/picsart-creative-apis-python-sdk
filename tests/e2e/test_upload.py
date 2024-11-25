import os

import pytest

import picsart_sdk
from picsart_sdk.api_response import ApiResponse, ApiResponseData
from picsart_sdk.clients.upload_client import UploadClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
@pytest.mark.parametrize(
    "method, param",
    [
        ("upload_from_path", "../resources/image1.jpeg"),
        (
            "upload_from_url",
            "https://pastatic.picsart.com/cms-pastatic/49a41b68-a0c9-42c0-aed5-58296b4c5379.jpeg",
        ),
    ],
)
def test_upload(method, param):
    client: UploadClient = picsart_sdk.client("upload")

    if method == "upload_from_path":
        current_dir = os.path.dirname(__file__)
        param = os.path.abspath(os.path.join(current_dir, param))

    function = getattr(client, method)
    result = function(param)

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
