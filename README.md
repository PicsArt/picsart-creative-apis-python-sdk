# PICSART CREATIVE APIS Python SDK

## Overview

The Picsart Python SDK provides seamless access to Picsart Programmable Image APIs and Picsart GenAI APIs, 
enabling developers to enhance and manipulate images with minimal code. 
The SDK simplifies the integration of advanced image processing features, 
making it easy to build creative and AI-driven applications.

## Requirements
Python 3.9 or higher

## Getting Started

### Installation
Install the SDK via pip:

```bash
pip install picsart-sdk
```

### Create a Client

**Option 1: Using Default Session**

If the `PICSART_API_KEY` environment variable is set, you can quickly create a client:

```python
import picsart_sdk
from picsart_sdk.clients import UploadClient
from picsart_sdk import PicsartAPI

upload_client: UploadClient = picsart_sdk.client(PicsartAPI.UPLOAD)
```

**Option 2: Passing the PICSART_API_KEY manually**

You can also pass the API key directly to the API. 
Manually passing the API key takes precedence over using the environment variable:

```python
import picsart_sdk
from picsart_sdk.clients import UploadClient
from picsart_sdk import PicsartAPI

upload_client: UploadClient = picsart_sdk.client(PicsartAPI.UPLOAD, api_key="YOUR-API-KEY")
```

> **_NOTE:_** We recommend always using Python type hinting, such as 
> `upload_client: UploadClient = picsart_sdk.client(...)`, 
> to fully leverage IDE autocompletion and improve code readability.

### Features and Examples

#### 1. Uploading an Image

```python
import picsart_sdk
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UploadClient

upload_client: UploadClient = picsart_sdk.client("upload")

response: ApiResponse = upload_client.upload_image(image_path="/path/to/image.jpg")
print(response.data.url)
response: ApiResponse = upload_client.upload_image(image_url="https://domain.com/file.jpg")
print(response.data.url)
```

#### 2. Remove Background
#### Simple remove background using a file or from url

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import RemoveBackgroundClient
from picsart_sdk.api_responses import ApiResponse

client: RemoveBackgroundClient = picsart_sdk.client(PicsartAPI.REMOVE_BACKGROUND)

response: ApiResponse = client.remove_background(image_path="./file.jpg")
print(response.data.url)

response = client.remove_background(image_url="https://domain.com/image.jpg")
print(response.data.url)
```

#### Advanced Use Case

In case you want to apply different features available for [remove background](https://docs.picsart.io/reference/image-remove-background), 
you can pass them as parameters, having the same names.

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import RemoveBackgroundClient

client: RemoveBackgroundClient = picsart_sdk.client(PicsartAPI.REMOVE_BACKGROUND)
response: ApiResponse = client.remove_background(image_url="https://domain.com/image.jpg", stroke_size=2, stroke_color="red")
print(response.data.url)
```

> You can check the [API Reference](https://docs.picsart.io/reference) 
> to find the available options for any of the supported APIs. 

#### 3. Ultra Upscale an Image

**Using synchronous mode** (not feasible for large images)

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(PicsartAPI.ULTRA_UPSCALE)
response: ApiResponse = client.ultra_upscale(image_path="./your-file.jpg", mode=UltraUpscaleMode.SYNC)
print(response.data.url)
```

**Using asynchronous mode** (_recommended_)

```python
import time
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(PicsartAPI.ULTRA_UPSCALE)
response: ApiResponse = client.ultra_upscale(image_path="./your-file.jpg", mode=UltraUpscaleMode.ASYNC)
time.sleep(10)  # depending on the load of the service and the size of the image, the time to process can differ
response: ApiResponse = client.get_result(transaction_id=response.transaction_id)
print(response.data.url)
```

> To find additional code snippets, explore the `examples` folder.


# HTTP Async Client
The SDK includes an async HTTP client built on Python's async implementation, enabling non-blocking API requests for 
optimal performance in high-concurrency applications. 
The async client mirrors the interface of the synchronous client, making it easy to switch between the two.

```python
import asyncio

import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import AsyncUploadClient

async def upload_image_async():
    # Create an async client
    client: AsyncUploadClient = picsart_sdk.async_client(PicsartAPI.UPLOAD)

    # Upload an image using the async/await syntax
    response = await client.upload_image(image_path="./file.jpg")
    print(response.data.url)

asyncio.run(upload_image_async())
```

# Asynchronous processing

Some Picsart API endpoints support `asynchronous processing`, allowing you to initiate a request that returns a `transaction_id`. 
This enables the client to retrieve the results of the requested operation at a later time using that transaction ID.

The SDK provides a convenient `get_result` method on the client object for fetching the final output of such operations.

Please refer to the [API Documentation](https://docs.picsart.io/) for details. 

```python
import time
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(PicsartAPI.ULTRA_UPSCALE)
response1 = client.ultra_upscale(image_path="./file.jpg", mode=UltraUpscaleMode.ASYNC)
print(response1)
# expect something like: ApiResponse(status='queued', data=None, transaction_id='6862207a-838c-48c6-ba12-cf6083a9d76e')

time.sleep(10)
response2 = client.get_result(transaction_id=response1.transaction_id)
print(response2)
```

The response would be something like 

```python
ApiResponse(
  status='success', 
  data=ApiResponseData(
      id='702eb942-62fb-4c73-834b-db189cca923e.png', 
      url='https://cdn.picsart.io/702eb942-62fb-4c73-834b-db189cca923e.png'
  ), 
  transaction_id=None
)
```

# Supported APIs

The SDK supports interactions with the following Picsart APIs

## Image APIs
- [Upload](https://docs.picsart.io/reference/image-upload)
- [Remove Background](https://docs.picsart.io/reference/image-remove-background)
- [Upscale](https://docs.picsart.io/reference/image-upscale)
- [Ultra Upscale](https://docs.picsart.io/reference/image-ultra-upscale)
- [Ultra Enhance](https://docs.picsart.io/reference/image-ultra-enhance)
- [Face Enhancement](https://docs.picsart.io/reference/image-face-enhance)
- [Effects](https://docs.picsart.io/reference/image-apply-effect)
- [Effects Previews](https://docs.picsart.io/reference/image-create-effect-previews)
- [AI Effects](https://docs.picsart.io/reference/image-apply-ai-effect)
- [Color Transfer](https://docs.picsart.io/reference/image-transfer-color)
- [Style Transfer](https://docs.picsart.io/reference/image-transfer-style)
- [Masks](https://docs.picsart.io/reference/image-apply-mask)
- [Masks Previews](https://docs.picsart.io/reference/image-create-mask-previews)
- [Adjust](https://docs.picsart.io/reference/image-adjust)
- [Basic Edit](https://docs.picsart.io/reference/image-edit)
- [Texture Generator](https://docs.picsart.io/reference/image-generate-texture)
- [Vectorizer](https://docs.picsart.io/reference/image-vectorize-raster-to-svg)
- [Surfacemap Image](https://docs.picsart.io/reference/image-surfacemap)
- [Image Tagging](https://docs.picsart.io/reference/image-tagging)
- [Image Description](https://docs.picsart.io/reference/image-describer)
- [Balance](https://docs.picsart.io/reference/image-credits-balance)

## GenAI
- [Text2Image](https://docs.picsart.io/reference/genai-text2image-1)
- [Text2Text](https://docs.picsart.io/reference/genai-text2text-completions)
- [Inpainting](https://docs.picsart.io/reference/genai-image-inpainting)
- [Outpainting](https://docs.picsart.io/reference/genai-image-outpainting)
- [Smart Background / Replace Background](https://docs.picsart.io/reference/genai-smart-background)
- [Expand](https://docs.picsart.io/reference/genai-expand-image)
- [Bleed](https://docs.picsart.io/reference/genai-generate-image-bleed)
- [Balance](https://docs.picsart.io/reference/genai-credits-balance)

# Error Handling

The SDK converts API errors into Python exceptions for easier debugging:

- **ApiError**: Raised for non-20x HTTP responses.
- **ApiAuthenticationError**: Raised for authentication failures.
- **ValueError**: Raised for invalid payloads.
