import os

import pytest

import picsart_sdk
from picsart_sdk.api_response import ApiResponse, ApiResponseData
from picsart_sdk.clients.upload_client import UploadClient


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_upload_from_file():
    client: UploadClient = picsart_sdk.client("upload")
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../resources/image1.jpeg")

    result = client.upload_from_path(file_path=file_path)

    assert isinstance(result, ApiResponse)
    assert isinstance(result.data, ApiResponseData)
    assert result.status == "success"
    assert len(result.data.url) > 0
    assert len(result.data.id) > 0
