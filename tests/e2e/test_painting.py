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


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "method_name, client_name, client_type, params",
    [
        (
            "inpainting",
            "inpainting",
            "sync",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": "../resources/painting/inpainting_mask.png",
                "prompt": "a black cat",
                "mode": "sync",
            },
        ),
        (
            "inpainting",
            "inpainting",
            "sync",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": "../resources/painting/inpainting_mask.png",
                "prompt": "a black cat",
                "mode": "async",
            },
        ),
        (
            "outpainting",
            "outpainting",
            "sync",
            {
                "image_path": "../resources/painting/outpainting_image.jpeg",
                "mask_path": "../resources/painting/outpainting_mask.png",
                "prompt": "a green field",
                "mode": "sync",
            },
        ),
        (
            "outpainting",
            "outpainting",
            "sync",
            {
                "image_path": "../resources/painting/outpainting_image.jpeg",
                "mask_path": "../resources/painting/outpainting_mask.png",
                "prompt": "a green field",
                "mode": "async",
            },
        ),
        (
            "replace_background",
            "replace_background",
            "sync",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "mode": "sync",
            },
        ),
        (
            "replace_background",
            "replace_background",
            "sync",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "mode": "async",
            },
        ),
        (
            "expand",
            "expand",
            "sync",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "width": 1600,
                "height": 1600,
                "mode": "sync",
            },
        ),
        (
            "expand",
            "expand",
            "sync",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "width": 1600,
                "height": 1600,
                "mode": "async",
            },
        ),
        # async clients
        (
            "inpainting",
            "inpainting",
            "async",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": "../resources/painting/inpainting_mask.png",
                "prompt": "a black cat",
                "mode": "sync",
            },
        ),
        (
            "inpainting",
            "inpainting",
            "async",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": "../resources/painting/inpainting_mask.png",
                "prompt": "a black cat",
                "mode": "async",
            },
        ),
        (
            "outpainting",
            "outpainting",
            "async",
            {
                "image_path": "../resources/painting/outpainting_image.jpeg",
                "mask_path": "../resources/painting/outpainting_mask.png",
                "prompt": "a green field",
                "mode": "sync",
            },
        ),
        (
            "outpainting",
            "outpainting",
            "async",
            {
                "image_path": "../resources/painting/outpainting_image.jpeg",
                "mask_path": "../resources/painting/outpainting_mask.png",
                "prompt": "a green field",
                "mode": "async",
            },
        ),
        (
            "replace_background",
            "replace_background",
            "async",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "mode": "sync",
            },
        ),
        (
            "replace_background",
            "replace_background",
            "async",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "mode": "async",
            },
        ),
        (
            "expand",
            "expand",
            "async",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "width": 1600,
                "height": 1600,
                "mode": "sync",
            },
        ),
        (
            "expand",
            "expand",
            "async",
            {
                "image_path": "../resources/painting/inpainting_image.jpeg",
                "mask_path": None,
                "prompt": "a green field",
                "width": 1600,
                "height": 1600,
                "mode": "async",
            },
        ),
    ],
)
async def test_painting_async_client(method_name, client_name, client_type, params):
    if client_type == "async":
        client: InpaintingClient = picsart_sdk.async_client(
            client_name
        )  # get ASYNC client
    else:
        client: InpaintingClient = picsart_sdk.client(client_name)

    params["image_path"] = os.path.abspath(
        os.path.join(os.path.dirname(__file__), params["image_path"])
    )
    if params.get("mask_path") is not None:
        params["mask_path"] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), params.get("mask_path"))
        )
    else:
        del params["mask_path"]

    params["count"] = 2
    params["output_format"] = PicsartImageFormat.PNG

    function = getattr(client, method_name)
    if client_type == "async":
        result: PaintingApiResponse = await function(**params)
    else:
        result: PaintingApiResponse = function(**params)

    if params["mode"] == "async":
        assert result.status == "success"
        assert result.data == []
        assert result.inference_id is not None
        if client_type == "async":
            result: PaintingApiResponse = await wait_for_result_async(
                client=client,
                inference_id=result.inference_id,
                max_retries=20,
                retry_delay=2,
            )
        else:
            result: PaintingApiResponse = wait_for_result(
                client=client,
                inference_id=result.inference_id,
                max_retries=20,
                retry_delay=2,
            )

    assert_response(result, params["count"])
