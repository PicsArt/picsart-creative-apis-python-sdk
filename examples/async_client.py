import asyncio

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import AsyncUploadClient


async def upload_image_async():
    # Create an async client
    client: AsyncUploadClient = picsart_sdk.async_client(PicsartAPI.UPLOAD)

    # Upload an image using the async/await syntax
    response = await client.upload_image(image_path="../tests/resources/image1.jpeg")
    print(response.data.url)


asyncio.run(upload_image_async())
