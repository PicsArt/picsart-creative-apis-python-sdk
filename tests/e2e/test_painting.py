import os

import pytest

import picsart_sdk
from picsart_sdk.clients import InpaintingClient
from picsart_sdk.clients.inpainting_client import (
    PaintingApiResponse,
    PaintingDataItemApiResponse,
)
from picsart_sdk.clients.requests_models import PicsartImageFormat


@pytest.mark.parametrize(
    "method_name, client_name, image_path, mask_path, prompt",
    [
        (
            "inpainting",
            "inpainting",
            "../resources/painting/inpainting_image.jpeg",
            "../resources/painting/inpainting_mask.png",
            "a black cat",
        ),
        (
            "outpainting",
            "outpainting",
            "../resources/painting/outpainting_image.jpeg",
            "../resources/painting/outpainting_mask.png",
            "a green field",
        ),
    ],
)
def test_painting(method_name, client_name, image_path, mask_path, prompt):
    client: InpaintingClient = picsart_sdk.client(client_name)
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), image_path))
    mask_path = os.path.abspath(os.path.join(os.path.dirname(__file__), mask_path))

    count = 2
    function = getattr(client, method_name)
    result = function(
        prompt=prompt,
        image_path=image_path,
        mask_path=mask_path,
        count=count,
        output_format=PicsartImageFormat.PNG,
    )

    assert isinstance(result, PaintingApiResponse)
    assert result.status == "success"
    assert result.data is not None
    assert len(result.data) == count
    for item in result.data:
        assert isinstance(item, PaintingDataItemApiResponse)
        assert isinstance(item.id, str)
        assert isinstance(item.url, str)
