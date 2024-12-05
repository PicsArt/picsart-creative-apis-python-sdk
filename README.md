<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# PICSART CREATIVE APIS Python SDK
=======
from picsart_sdk.clients.requests_models.upscale_request import UpscaleRequest

=======
>>>>>>> d7a079c (update readme)
# PICSART CREATIVE APIS
>>>>>>> a16605e (update readme)

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
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse
from picsart_sdk.clients import UploadClient

<<<<<<< HEAD
upload_client: UploadClient = picsart_sdk.client(PicsartAPI.UPLOAD)

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

> To find additional code snippets, explore the [examples](./examples) folder.


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

# License

Picsart Creative APIs SDK is provided under the MIT license that can be found in the
[LICENSE](./LICENSE) file.
By using, distributing, or contributing to this project, you agree to
the terms and conditions of this license.

This project has some third-party dependencies, each of which may have independent licensing:
- [httpx](https://github.com/projectdiscovery/httpx), ([MIT](https://github.com/projectdiscovery/httpx/blob/main/LICENSE.md)): Used as a http client

# How to contribute?

If you like Picsart Creative APIs SDK and would like to contribute to this open-source project, please check the [Contribution
guide](./CONTRIBUTING.md).
=======
=======
# PICSART CREATIVE APIS

## Description

This is a Python SDK of Picsart Programmable Image APIs and Picsart GenAI APIs. 
You can do many actions with your images just by adding a few lines of code to your Python projects.

## Requirements
Python 3.9+

## Usage

Create the client:
1. Default session. It is shorter if the `PICSART_API_KEY` environment variable is set.

```python
import picsart_sdk
from picsart_sdk.clients.client_factory import ApiClient
upload_client = picsart_sdk.client(ApiClient.UPLOAD)
```
otherwise you can create the session manually and passing the api key. 

```python
import picsart_sdk
from picsart_sdk.clients.client_factory import ApiClient
session = picsart_sdk.Session(api_key="API_KEY")
upload_client = session.client(ApiClient.UPLOAD)
```

afterwards, you can use the specific client. 

Example for uploading a file:
```python
import picsart_sdk
upload_client = picsart_sdk.client("upload")

<<<<<<< HEAD
>>>>>>> 936ede4 (readd coide)
upload_client.upload_from_path(file_path="/path/to/image.jpg")
upload_client.upload_from_url(url="https://domain.com/file.jpg")
=======
upload_client.upload_image(image_path="/path/to/image.jpg")
upload_client.upload_image(image_url="https://domain.com/file.jpg")
>>>>>>> a903eeb (refactor)
```

## Remove Background
### Simple remove background using a file or from url

```python
import picsart_sdk
from picsart_sdk.clients.client_factory import ApiClient

client = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

response1 = client.remove_background(image_path="./file.jpg")
response2 = client.remove_background(image_url="https://domain.com/image.jpg")
print(response1.data.url)
print(response2.data.url)
```

### More complex case

In case you want to apply different features available for [remove background](https://docs.picsart.io/reference/image-remove-background), 
you can pass them as parameters, having the same names.

```python
import picsart_sdk
from picsart_sdk.clients.client_factory import ApiClient

client = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

response = client.remove_background(image_url="https://domain.com/image.jpg", stroke_size=2, stroke_color="red")
print(response.data.url)
```
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9e83d5f (update readme; sugar syntax for removebg)
=======
=======
>>>>>>> 936ede4 (readd coide)

## Upscale

```python
import picsart_sdk
from picsart_sdk.clients.client_factory import ApiClient

client = picsart_sdk.client(ApiClient.UPSCALE)
response = client.upscale(url="https://domain.com/image.jpg", upscale_factor=2)
print(response.data.url)
```
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a16605e (update readme)
=======
=======
>>>>>>> 936ede4 (readd coide)

# Async Client
The SDK supports also an async client, which exposes the same interface:

```python
import asyncio

import picsart_sdk
from picsart_sdk.clients.upload_client import AsyncUploadClient
from picsart_sdk.clients.client_factory import ApiClient

async def call_upload():
    client: AsyncUploadClient = picsart_sdk.async_client(ApiClient.UPLOAD)
    response1 = await client.upload_image(image_path="./file.jpg")
    # or
    response2 = await client.upload_image(image_url="https://domain.com/image.jpg")
    
    print(response1)
    print(response2)

asyncio.run(call_upload())
```

# Async Endpoints

Some Picsart API endpoints support `async` mode, allowing clients to initiate a POST request that creates a transaction 
identified by a transaction_id. This enables the client to retrieve the results of the requested operation at a later 
time using that transaction ID. These specific operations also provide a `get_result` method on the client object for 
fetching the final output. For example, the ultra upscale operation:

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
- Upload
- Remove Background
- Upscale
- Ultra Upscale
- Face Enhancement
- Effects
- Effects Previews
- Balance (for Image APIs)
- Color Transfer
- Style Transfer
- Masks
- Masks Previews
- Adjust
- Basic Edit
- Texture Generator
- Vectorizer
- Surfacemap
- Image Tagging (TODO: e2e tests)
- Image Description (TODO: e2e tests)
- GenAI Text2Image
- GenAI Text2Text
- GenAI Balance

# Errors

If the API returns a 400 HTTP error, it will be translated into an `ApiError` in the SDK.
If the authentication is not successful it raises `ApiAuthenticationError` error.
If the pre-validation of the payload fails, the SDK will raise a `ValueError.`
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5fbc476 (add apierror)
=======
>>>>>>> 936ede4 (readd coide)
=======


## For developers
To develop this SDK purposes only:

Install poetry and pre-commit hook:
```bash
poetry install
poetry run pre-commit install
```

>>>>>>> 7053359 (style transfer, pre-commit hook, isort)
