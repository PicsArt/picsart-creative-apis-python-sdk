import asyncio
import os
import time

import pytest

import picsart_sdk
from picsart_sdk.api_responses.painting_response import (
    PaintingApiResponse,
    PaintingDataItemApiResponse,
)
from picsart_sdk.clients import InpaintingClient
from picsart_sdk.clients.requests_models import PicsartImageFormat


def assert_response(result, count):
    assert isinstance(result, PaintingApiResponse)
    assert result.status == "success"
    assert result.data is not None
    assert len(result.data) == count
    for item in result.data:
        assert isinstance(item, PaintingDataItemApiResponse)
        assert isinstance(item.id, str)
        assert isinstance(item.url, str)


def wait_for_result(
    client, inference_id, max_retries=5, retry_delay=1
) -> PaintingApiResponse:
    """
    Polls the API results
    """
    result = None
    for _ in range(max_retries):
        result = client.get_results(inference_id=inference_id)
        if result.status != "processing":
            return result
        time.sleep(retry_delay)
    raise TimeoutError(
        f"Result not generated in time after {max_retries * retry_delay} seconds. Last result: {result}"
    )


async def wait_for_result_async(
    client, inference_id, max_retries=5, retry_delay=1
) -> PaintingApiResponse:
    """
    Polls the API results
    """
    result = None
    for _ in range(max_retries):
        result = await client.get_results(inference_id=inference_id)
        if result.status != "processing":
            return result
        await asyncio.sleep(retry_delay)
    raise TimeoutError(
        f"Result not generated in time after {max_retries * retry_delay} seconds. Last result: {result}"
    )


@pytest.mark.parametrize(
    "method_name, client_name, image_path, mask_path, prompt, response_mode",
    [
        (
            "inpainting",
            "inpainting",
            "../resources/painting/inpainting_image.jpeg",
            "../resources/painting/inpainting_mask.png",
            "a black cat",
            "sync",
        ),
        (
            "inpainting",
            "inpainting",
            "../resources/painting/inpainting_image.jpeg",
            "../resources/painting/inpainting_mask.png",
            "a black cat",
            "async",
        ),
        (
            "outpainting",
            "outpainting",
            "../resources/painting/outpainting_image.jpeg",
            "../resources/painting/outpainting_mask.png",
            "a green field",
            "sync",
        ),
        (
            "outpainting",
            "outpainting",
            "../resources/painting/outpainting_image.jpeg",
            "../resources/painting/outpainting_mask.png",
            "a green field",
            "async",
        ),
        (
            "replace_background",
            "replace_background",
            "../resources/painting/inpainting_image.jpeg",
            None,
            "a green field",
            "sync",
        ),
        (
            "replace_background",
            "replace_background",
            "../resources/painting/inpainting_image.jpeg",
            None,
            "a green field",
            "async",
        ),
    ],
)
def test_painting(
    method_name, client_name, image_path, mask_path, prompt, response_mode
):
    client: InpaintingClient = picsart_sdk.client(client_name)  # get SYNC client
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), image_path))
    if mask_path is not None:
        mask_path = os.path.abspath(os.path.join(os.path.dirname(__file__), mask_path))

    count = 2

    params = {
        "prompt": prompt,
        "image_path": image_path,
        "count": count,
        "output_format": PicsartImageFormat.PNG,
        "mode": response_mode,
    }

    if mask_path:
        params["mask_path"] = mask_path

    function = getattr(client, method_name)
    result = function(**params)

    if response_mode == "async":
        assert result.status == "success"
        assert result.data == []
        assert result.inference_id is not None
        result: PaintingApiResponse = wait_for_result(
            client=client,
            inference_id=result.inference_id,
            max_retries=20,
            retry_delay=2,
        )

    assert_response(result, count)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "method_name, client_name, image_path, mask_path, prompt, response_mode",
    [
        (
            "inpainting",
            "inpainting",
            "../resources/painting/inpainting_image.jpeg",
            "../resources/painting/inpainting_mask.png",
            "a black cat",
            "sync",
        ),
        (
            "inpainting",
            "inpainting",
            "../resources/painting/inpainting_image.jpeg",
            "../resources/painting/inpainting_mask.png",
            "a black cat",
            "async",
        ),
        (
            "outpainting",
            "outpainting",
            "../resources/painting/outpainting_image.jpeg",
            "../resources/painting/outpainting_mask.png",
            "a green field",
            "sync",
        ),
        (
            "outpainting",
            "outpainting",
            "../resources/painting/outpainting_image.jpeg",
            "../resources/painting/outpainting_mask.png",
            "a green field",
            "async",
        ),
        (
            "replace_background",
            "replace_background",
            "../resources/painting/inpainting_image.jpeg",
            None,
            "a green field",
            "sync",
        ),
        (
            "replace_background",
            "replace_background",
            "../resources/painting/inpainting_image.jpeg",
            None,
            "a green field",
            "async",
        ),
    ],
)
async def test_painting_async_client(
    method_name, client_name, image_path, mask_path, prompt, response_mode
):
    client: InpaintingClient = picsart_sdk.async_client(client_name)  # get ASYNC client
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), image_path))
    if mask_path is not None:
        mask_path = os.path.abspath(os.path.join(os.path.dirname(__file__), mask_path))

    count = 2

    params = {
        "prompt": prompt,
        "image_path": image_path,
        "count": count,
        "output_format": PicsartImageFormat.PNG,
        "mode": response_mode,
    }

    if mask_path:
        params["mask_path"] = mask_path

    function = getattr(client, method_name)
    result: PaintingApiResponse = await function(**params)

    if response_mode == "async":
        assert result.status == "success"
        assert result.data == []
        assert result.inference_id is not None
        result: PaintingApiResponse = await wait_for_result_async(
            client=client,
            inference_id=result.inference_id,
            max_retries=20,
            retry_delay=2,
        )

    assert_response(result, count)
