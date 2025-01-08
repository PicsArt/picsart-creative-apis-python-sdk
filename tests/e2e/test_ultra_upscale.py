import os
import time

import pytest

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse, ApiResponseData
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.clients.requests_models import PicsartImageFormat


def assert_response(result: ApiResponse):
    assert isinstance(result, ApiResponse)
    assert result.status == "success"
    assert result.data is not None

    assert isinstance(result.data, ApiResponseData)
    assert isinstance(result.data.id, str)
    assert isinstance(result.data.url, str)


def wait_for_result(client, inference_id, max_retries=5, retry_delay=1) -> ApiResponse:
    """
    Polls the API results
    """

    result = None
    for _ in range(max_retries):
        result = client.get_result(inference_id=inference_id)
        if result.status != "processing":
            return result

        assert result.data is None
        time.sleep(retry_delay)
    raise TimeoutError(
        f"Result not generated in time after {max_retries * retry_delay} seconds. Last result: {result}"
    )


@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_ultra_upscale_mode_async():
    client: UltraUpscaleClient = picsart_sdk.client(PicsartAPI.ULTRA_UPSCALE)

    params = {
        "image_path": os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../resources/image1.jpeg")
        ),
        "upscale_factor": 2,
        "output_format": PicsartImageFormat.PNG,
        "mode": "async",
    }

    result: ApiResponse = client.ultra_upscale(**params)

    assert result.status == "queued"
    assert result.data is None
    assert result.inference_id is not None

    result = wait_for_result(client, result.inference_id)

    assert_response(result)
