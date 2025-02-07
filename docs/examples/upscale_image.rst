Upscale Image
=============

This page explains how to use the Picsart Creative APIs Python SDK to upscale an image.
Please refer to the `Upscale API documentation <https://docs.picsart.io/reference/image-upscale>`_ for the full list
of the features and their possible values and to the API Reference :ref:`upscale_client` for the SDK usage.

Example:
~~~~~~~~

Using synchronous HTTP call
---------------------------

.. code-block:: python

    import picsart_sdk
    from picsart_sdk import PicsartAPI
    from picsart_sdk.clients import UpscaleClient

    client: UpscaleClient = picsart_sdk.client(PicsartAPI.UPSCALE)
    response = client.upscale(image_path="./image-file.jpg", upscale_factor=2)
    print(response.data.url)


Using asynchronous HTTP call
----------------------------

.. code-block:: python

    import asyncio

    import picsart_sdk
    from picsart_sdk import PicsartAPI
    from picsart_sdk.clients import AsyncUpscaleClient

    async def async_upscale():
        client: AsyncUpscaleClient = picsart_sdk.async_client(PicsartAPI.UPSCALE)
        response = await client.upscale(image_path="./image-file.jpg", upscale_factor=2)
        print(response.data.url)

    asyncio.run(async_upscale())

