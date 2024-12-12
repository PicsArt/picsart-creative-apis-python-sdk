import asyncio
import os
import time

import pytest

import picsart_sdk
from picsart_sdk.api_responses.text2image_response import (
    Text2ImageApiResponse,
    Text2ImageCreateApiResponse,
)
from picsart_sdk.clients import AsyncText2ImageClient, Text2ImageClient
from picsart_sdk.clients.client_factory import ApiClient


def wait_for_result(
    client: Text2ImageClient, inference_id, max_retries=5, retry_delay=1
):
    """
    Polls the API for text2image results until the status is FINISHED or retries are exhausted.
    """
    result = None
    for _ in range(max_retries):
        result = client.get_result(inference_id=inference_id)
        if result.status == "FINISHED":
            return result
        time.sleep(retry_delay)
    raise TimeoutError(
        f"Result not generated in time after {max_retries * retry_delay} seconds. Last result: {result}"
    )


async def wait_for_result_async(
    client: AsyncText2ImageClient, inference_id, max_retries=5, retry_delay=1
):
    """
    Polls async the API for text2image results until the status is FINISHED or retries are exhausted.
    """
    result = None
    for _ in range(max_retries):
        result = await client.get_result(inference_id=inference_id)
        if result.status == "FINISHED":
            return result
        await asyncio.sleep(retry_delay)
    raise TimeoutError(
        f"Result not generated in time after {max_retries * retry_delay} seconds. Last result: {result}"
    )


def common_assertion(result1, result2, total):
    assert isinstance(result1, Text2ImageCreateApiResponse)
    assert result1.inference_id is not None
    assert result1.status == "ACCEPTED"

    assert isinstance(result2, Text2ImageApiResponse)
    assert result2.status == "FINISHED"
    assert isinstance(result2.data, list)
    assert len(result2.data) == total


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_create_text2image():
    client: Text2ImageClient = picsart_sdk.client(ApiClient.TEXT2IMAGE)
    total = 2

    result1 = client.text2image(prompt="a cat in a tree", count=total)
    result2 = wait_for_result(
        client, inference_id=result1.inference_id, max_retries=5, retry_delay=2
    )
    common_assertion(result1, result2, total)


@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
async def test_create_text2image_async():
    client: AsyncText2ImageClient = picsart_sdk.async_client(ApiClient.TEXT2IMAGE)
    total = 2

    result1 = await client.text2image(prompt="a cat in a tree", count=total)
    result2 = await wait_for_result_async(
        client, inference_id=result1.inference_id, max_retries=5, retry_delay=2
    )
    common_assertion(result1, result2, total)
