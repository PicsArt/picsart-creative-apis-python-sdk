import time

import picsart_sdk
from picsart_sdk.api_responses.text2image_response import (
    Text2ImageApiResponse,
    Text2ImageCreateApiResponse,
)
from picsart_sdk.clients import Text2ImageClient
from picsart_sdk.clients.client_factory import ApiClient


def wait_for_result(client, inference_id, max_retries=5, retry_delay=1):
    """
    Polls the API for text2image results until the status is FINISHED or retries are exhausted.
    """
    result = None
    for _ in range(max_retries):
        result = client.get_text2image_result(inference_id=inference_id)
        if result.status == "FINISHED":
            return result
        time.sleep(retry_delay)
    raise TimeoutError(
        f"Result not generated in time after {max_retries * retry_delay} seconds. Last result: {result}"
    )


def test_create_text2image():
    client: Text2ImageClient = picsart_sdk.client(ApiClient.TEXT2IMAGE)
    total = 2  # Number of images to generate

    result1 = client.text2image(prompt="a cat in a tree", count=total)
    assert isinstance(result1, Text2ImageCreateApiResponse)
    assert result1.inference_id is not None
    assert result1.status == "ACCEPTED"

    result2 = wait_for_result(
        client, inference_id=result1.inference_id, max_retries=5, retry_delay=2
    )
    assert isinstance(result2, Text2ImageApiResponse)
    assert result2.status == "FINISHED"
    assert isinstance(result2.data, list)
    assert len(result2.data) == total
