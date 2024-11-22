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
