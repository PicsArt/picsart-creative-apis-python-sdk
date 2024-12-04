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

upload_client.upload_image(image_path="/path/to/image.jpg")
upload_client.upload_image(image_url="https://domain.com/file.jpg")
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

## Upscale

```python
import picsart_sdk
from picsart_sdk.clients.client_factory import ApiClient

client = picsart_sdk.client(ApiClient.UPSCALE)
response = client.upscale(url="https://domain.com/image.jpg", upscale_factor=2)
print(response.data.url)
```

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
- Text2Image (TODO: e2e tests)

# Errors

If the API returns a 400 HTTP error, it will be translated into an `ApiError` in the SDK.
If the authentication is not successful it raises `ApiAuthenticationError` error.
If the pre-validation of the payload fails, the SDK will raise a `ValueError.`


## For developers
To develop this SDK purposes only:

Install poetry and pre-commit hook:
```bash
poetry install
poetry run pre-commit install
```

