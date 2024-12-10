from picsart_sdk.api_responses.balance_response import BalanceApiResponsefrom picsart_sdk.api_responses import ApiResponse

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

If the PICSART_API_KEY environment variable is set, you can quickly create a client:

```python
import picsart_sdk
from picsart_sdk.clients import ApiClient

upload_client = picsart_sdk.client(ApiClient.UPLOAD)
```

**Option 2: Creating a Session Manually**

You can also create a session manually and pass the API key directly:

```python
import picsart_sdk
from picsart_sdk.clients import ApiClient

session = picsart_sdk.Session(api_key="YOUR_API_KEY")
upload_client = session.client(ApiClient.UPLOAD)
```

### Features and Examples

#### 1. Uploading an Image

```python
import picsart_sdk
from picsart_sdk.api_responses import ApiResponse

upload_client = picsart_sdk.client("upload")

response: ApiResponse = upload_client.upload_image(image_path="/path/to/image.jpg")
print(response.data.url)
response: ApiResponse = upload_client.upload_image(image_url="https://domain.com/file.jpg")
print(response.data.url)
```

#### 2. Remove Background
#### Simple remove background using a file or from url

```python
import picsart_sdk
from picsart_sdk.clients import RemoveBackgroundClient, ApiClient
from picsart_sdk.api_responses import ApiResponse

client: RemoveBackgroundClient = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

response: ApiResponse = client.remove_background(image_path="./file.jpg")
print(response.data.url)

response = client.remove_background(image_url="https://domain.com/image.jpg")
print(response.data.url)
```

#### Advanced Use Case

In case you want to apply different features available for [remove background](https://docs.picsart.io/reference/image-remove-background), 
you can pass them as parameters, having the same names.

```python
response: ApiResponse = client.remove_background(image_url="https://domain.com/image.jpg", stroke_size=2, stroke_color="red")
print(response.data.url)
```

> You can check the [API Reference](https://docs.picsart.io/reference) 
> to find the available options for any of the supported APIs. 

#### 3. Upscale an Image

```python
client = picsart_sdk.client(ApiClient.UPSCALE)
response: ApiResponse = client.upscale(url="https://domain.com/image.jpg", upscale_factor=2)
print(response.data.url)
```

#### 4. Ultra Upscale an Image

**Using synchronous mode** (not feasible for large images)

```python
import picsart_sdk
from picsart_sdk.clients import UltraUpscaleClient, ApiClient
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(ApiClient.ULTRA_UPSCALE)
response: ApiResponse = client.ultra_upscale(image_path="./your-file.jpg", mode=UltraUpscaleMode.SYNC)
print(response.data.url)
```

**Using asynchronous mode** (_recommended_)

```python
client: UltraUpscaleClient = picsart_sdk.client(ApiClient.ULTRA_UPSCALE)
response: ApiResponse = client.ultra_upscale(image_path="./your-file.jpg", mode=UltraUpscaleMode.SYNC)
time.sleep(10)  # depending on the load of the service and the size of the image, the time to process can differ
response: ApiResponse = client.get_result(transaction_id=response.transaction_id)
print(response.data.url)
```

#### 5. Ultra Enhance

```python
import picsart_sdk
from picsart_sdk.clients import UltraEnhanceClient, ApiClient
from picsart_sdk.api_responses import ApiResponse

client: UltraEnhanceClient = picsart_sdk.client(ApiClient.ULTRA_ENHANCE)
response: ApiResponse = client.ultra_enhance(image_path="./your-file.jpg")
print(response.data.url)
```

#### 6. Face Enhancement

```python
import picsart_sdk
from picsart_sdk.clients import FaceEnhancementClient, ApiClient
from picsart_sdk.api_responses import ApiResponse

client: FaceEnhancementClient = picsart_sdk.client(ApiClient.FACE_ENHANCEMENT)
response: ApiResponse = client.face_enhancement(image_path="./your-file.jpg")
print(response.data.url)
```

#### 7. Effects

**1. Get the list of available effects** 

```python
import picsart_sdk
from picsart_sdk.clients import EffectsClient, ApiClient
from picsart_sdk.api_responses.effects_response import EffectsList

client: EffectsClient = picsart_sdk.client(ApiClient.EFFECTS)
response: EffectsList = client.get_available_effects()
for effect_name in response.effects:
    print(effect_name)
```

2. Apply an effect

```python
import picsart_sdk
from picsart_sdk.clients import EffectsClient, ApiClient
from picsart_sdk.api_responses import ApiResponse

client: EffectsClient = picsart_sdk.client(ApiClient.EFFECTS)
response: ApiResponse = client.effects(image_path="./your-file.jpg", effect_name="apr1")
print(response.data.url)
```

#### 8. Effects Preview

```python
import picsart_sdk
from picsart_sdk.clients import ApiClient, EffectsPreviewsClient
from picsart_sdk.api_responses.effects_response import EffectsPreviewsApiResponse

client: EffectsPreviewsClient = picsart_sdk.client(ApiClient.EFFECTS_PREVIEWS)
response: EffectsPreviewsApiResponse = client.effects_previews(image_path="./your-file.jpg", effect_names=["apr1", "brnz3"])
for item in response.data:
    print(item.effect_name, item.url)
```

#### 9. AI Effects

```python
import picsart_sdk
from picsart_sdk.clients import ApiClient, AiEffectsClient
from picsart_sdk.api_responses import ApiResponse

client: AiEffectsClient = picsart_sdk.client(ApiClient.AI_EFFECTS)
response: ApiResponse = client.ai_effects(image_path="./your-file.jpg")
print(response.data.url)
```

#### 10. Get the balance
```python
import picsart_sdk
from picsart_sdk.clients import ApiClient, BalanceClient, AsyncBalanceClient
from picsart_sdk.api_responses.balance_response import BalanceApiResponse

client: BalanceClient = picsart_sdk.client(ApiClient.BALANCE)
response: BalanceApiResponse = client.get_balance()
print(response.credits)

# async
client: AsyncBalanceClient = picsart_sdk.async_client(ApiClient.BALANCE)
response: BalanceApiResponse = await client.get_balance()
print(response.credits)
```

# TODO - EXAMPLES FOR ALL APIs 

# Async Client
The SDK includes an async HTTP client built on Python's async implementation, enabling non-blocking API requests for optimal performance in high-concurrency applications. The async client mirrors the interface of the synchronous client, making it easy to switch between the two.

```python
import asyncio

import picsart_sdk
from picsart_sdk.clients import AsyncUploadClient
from picsart_sdk.clients.client_factory import ApiClient

async def upload_image_async():
    # Create an async client
    client: AsyncUploadClient = picsart_sdk.async_client(ApiClient.UPLOAD)

    # Upload an image using the async/await syntax
    response = await client.upload_image(image_path="./file.jpg")
    print(response.data.url)

asyncio.run(upload_image_async())
```

# Async Endpoints

Some Picsart API endpoints support `asynchronous processing`, 
allowing you to initiate a request that returns a transaction_id. 
This enables the client to retrieve the results of the requested operation at a later time using that transaction ID.

The SDK provides a convenient `get_result` method on the client object for fetching the final output of such operations.

Please refer to the [API Documentation](https://docs.picsart.io/) for details. 

```python
import time
import picsart_sdk
from picsart_sdk.clients import UltraUpscaleClient
from picsart_sdk.clients.client_factory import ApiClient
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(ApiClient.ULTRA_UPSCALE)
response1 = client.ultra_upscale(image_path="./file.jpg", mode=UltraUpscaleMode.ASYNC)
print(response1)
# expect something like: ApiResponse(status='queued', data=None, transaction_id='6862207a-838c-48c6-ba12-cf6083a9d76e')

time.sleep(10)
response2 = client.get_result(transaction_id=response1.transaction_id)
print(response2)
# expect something like: 
# ApiResponse(
#   status='success', 
#   data=ApiResponseData(
#       id='702eb942-62fb-4c73-834b-db189cca923e.png', 
#       url='https://cdn.picsart.io/702eb942-62fb-4c73-834b-db189cca923e.png'
#   ), 
#   transaction_id=None
# )
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
- [Balance](https://docs.picsart.io/reference/genai-credits-balance)
- [Inpainting](https://docs.picsart.io/reference/genai-image-inpainting)
- [Outpainting](https://docs.picsart.io/reference/genai-image-outpainting)
- [Smart Background / Replace Background](https://docs.picsart.io/reference/genai-smart-background)
- [Expand](https://docs.picsart.io/reference/genai-expand-image)
- [Bleed](https://docs.picsart.io/reference/genai-generate-image-bleed)

# Error Handling

The SDK converts API errors into Python exceptions for easier debugging:

- **ApiError**: Raised for non-20x HTTP responses.
- **ApiAuthenticationError**: Raised for authentication failures.
- **ValueError**: Raised for invalid payloads.


## Development
### Setup for Developers

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Set up pre-commit hooks:
```bash
poetry run pre-commit install
```

### Run Tests
#### The tests should be run only by the SDK Developers with the specific PICSART_API_KEY otherwise the calls will consume from the credit. 

```bash
PICSART_LOG_HTTP_CALLS=true PICSART_LOG_HTTP_CALLS_HEADERS=true PICSART_API_KEY=<YOUR_API_KEY> pytest tests/
```
