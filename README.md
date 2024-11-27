# PICSART CREATIVE APIS

## Description

This is a Python SDK of Picsart Programmable Image APIs and Picsart GenAI APIs. 
You can do many actions with your images just by adding a few lines of code to your Python projects.

## Usage

Create the client:
1. Default session. It is shorter if the `PICSART_API_KEY` environment variable is set.

```python
import picsart_sdk
upload_client = picsart_sdk.client("upload")
```
otherwise you can create the session manually and passing the api key. 

```python
import picsart_sdk
session = picsart_sdk.Session(api_key="API_KEY")
upload_client = session.client("upload")
```

afterwards, you can use the specific client. 

Example for uploading a file:
```python
import picsart_sdk
upload_client = picsart_sdk.client("upload")

upload_client.upload_from_path(file_path="/path/to/image.jpg")
upload_client.upload_from_url(url="https://domain.com/file.jpg")
```

## Remove Background
### Simple remove background using a file or from url

```python
import picsart_sdk
client = picsart_sdk.client("removebg")

response1 = client.remove_background_from_path(file_path="./file.jpg")
response2 = client.remove_background_from_url(url="https://domain.com/image.jpg")
print(response1.data.url)
print(response2.data.url)
```

### More complex case

In case you want to apply different features available for [remove background](https://docs.picsart.io/reference/image-remove-background), it can be used a `RemoveBackgroundRequest`:

```python
import picsart_sdk
from picsart_sdk.clients.requests_models.remove_background_request import RemoveBackgroundRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage

client = picsart_sdk.client("removebg")

removebg_request = RemoveBackgroundRequest(
    image=PicsartImage(image_url="https://domain.com/image.jpg"),
    stroke_size=2,
    stroke_color="red",
)
response = client.remove_background(removebg_request)
print(response.data.url)
```

## Upscale

```python
import picsart_sdk

client = picsart_sdk.client("upscale")
response = client.upscale_from_url(url="https://domain.com/image.jpg", upscale_factor=2)
print(response.data.url)
```

or using `UpscaleRequest`

```python
import picsart_sdk
from picsart_sdk.clients.requests_models.upscale_request import UpscaleRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage

client = picsart_sdk.client("upscale")
request = UpscaleRequest(
    image=PicsartImage(image_path="./file.jpg"),
    upscale_factor=4
)
response = client.upscale(request)
print(response.data.url)
```

# Async Client
The SDK supports also async client, which exposes the same interface:

```python
import asyncio

import picsart_sdk
from picsart_sdk.clients.upload_client import AsyncUploadClient
from picsart_sdk.clients.requests_models.upload_request import UploadRequest
from picsart_sdk.clients.requests_models.picsart_image import PicsartImage

async def call_upload():
    client: AsyncUploadClient = picsart_sdk.async_client("upload")
    response1 = await client.upload_image(
        request=UploadRequest(
            PicsartImage(
                image_path="./file.jpg"
            )
        )
    )
    # or
    response2 = await client.upload_from_path(file_path="./file.jpg")
    
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
from picsart_sdk.clients.client_factory import Clients
from picsart_sdk.clients.requests_models.ultra_upscale_request import UltraUpscaleMode

client: UltraUpscaleClient = picsart_sdk.client(Clients.ULTRA_UPSCALE)
response1 = client.ultra_upscale_from_path(file_path="./file.jpg", mode=UltraUpscaleMode.ASYNC)
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


# Errors

If the API returns a 400 HTTP error, it will be translated into an `ApiError` in the SDK.
If the authentication is not successful it raises `ApiAuthenticationError` error.
If the pre-validation of the payload fails, the SDK will raise a `ValueError.`
