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
from picsart_sdk import PicsartAPI

upload_client = picsart_sdk.client(PicsartAPI.UPLOAD)
```

**Option 2: Creating a Session Manually**

You can also create a session manually and pass the API key directly:

```python
import picsart_sdk
from picsart_sdk import PicsartAPI

session = picsart_sdk.Session(api_key="YOUR_API_KEY")
upload_client = session.client(PicsartAPI.UPLOAD)
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

#### 3. Upscale an Image

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses import ApiResponse

client = picsart_sdk.client(PicsartAPI.UPSCALE)
response: ApiResponse = client.upscale(url="https://domain.com/image.jpg", upscale_factor=2)
print(response.data.url)
```

#### 4. Ultra Upscale an Image

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
response: ApiResponse = client.ultra_upscale(image_path="./your-file.jpg", mode=UltraUpscaleMode.SYNC)
time.sleep(10)  # depending on the load of the service and the size of the image, the time to process can differ
response: ApiResponse = client.get_result(transaction_id=response.transaction_id)
print(response.data.url)
```

#### 5. Ultra Enhance

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import UltraEnhanceClient
from picsart_sdk.api_responses import ApiResponse

client: UltraEnhanceClient = picsart_sdk.client(PicsartAPI.ULTRA_ENHANCE)
response: ApiResponse = client.ultra_enhance(image_path="./your-file.jpg")
print(response.data.url)
```

#### 6. Face Enhancement

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import FaceEnhancementClient
from picsart_sdk.api_responses import ApiResponse

client: FaceEnhancementClient = picsart_sdk.client(PicsartAPI.FACE_ENHANCEMENT)
response: ApiResponse = client.face_enhancement(image_path="./your-file.jpg")
print(response.data.url)
```

#### 7. Effects

**1. Get the list of available effects** 

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import EffectsClient
from picsart_sdk.api_responses.effects_response import EffectsListApiResponse

client: EffectsClient = picsart_sdk.client(PicsartAPI.EFFECTS)
response: EffectsListApiResponse = client.get_available_effects()
for effect_name in response.effects:
    print(effect_name)
```

**2. Apply an effect**

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import EffectsClient
from picsart_sdk.api_responses import ApiResponse

client: EffectsClient = picsart_sdk.client(PicsartAPI.EFFECTS)
response: ApiResponse = client.effects(image_path="./your-file.jpg", effect_name="apr1")
print(response.data.url)
```

#### 8. Effects Preview

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import EffectsPreviewsClient
from picsart_sdk.api_responses.effects_response import EffectsPreviewsApiResponse

client: EffectsPreviewsClient = picsart_sdk.client(PicsartAPI.EFFECTS_PREVIEWS)
response: EffectsPreviewsApiResponse = client.effects_previews(
    image_path="./your-file.jpg", 
    effect_names=["apr1", "brnz3"]
)
for item in response.data:
    print(item.effect_name, item.url)
```

#### 9. AI Effects

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import AiEffectsClient, AsyncAiEffectsClient
from picsart_sdk.api_responses import ApiResponse

client: AiEffectsClient = picsart_sdk.client(PicsartAPI.AI_EFFECTS)

# get the list of available effects
effects = client.get_available_ai_effects()
print(effects.effects)

# apply an effect
response: ApiResponse = client.ai_effects(image_path="./your-file.jpg", effect_name="winterblues")
print(response.data.url)
```

#### 10. Color transfer

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import ColorTransferClient
from picsart_sdk.api_responses import ApiResponse

path1 = "./your-file.jpg"
path2 = "./your-file2.jpg"
client: ColorTransferClient = picsart_sdk.client(PicsartAPI.COLOR_TRANSFER)
response: ApiResponse = client.color_transfer(image_path=path1, reference_image_path=path2)
print(response.data.url)
```

#### 11. Style Transfer

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import StyleTransferClient
from picsart_sdk.api_responses import ApiResponse

path1 = "./your-file.jpg"
path2 = "./your-file2.jpg"
client: StyleTransferClient = picsart_sdk.client(PicsartAPI.STYLE_TRANSFER)
response: ApiResponse = client.style_transfer(image_path=path1, reference_image_path=path2)
print(response.data.url)
```

#### 12. Masks

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import MasksClient
from picsart_sdk.api_responses import ApiResponse

client: MasksClient = picsart_sdk.client(PicsartAPI.MASKS)
response: ApiResponse = client.masks(image_path="./your-file.jpg", mask="lace1")
print(response.data.url)
```

#### 13. Mask Previews

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import MasksPreviewsClient
from picsart_sdk.api_responses.masks_previews_response import MasksPreviewsApiResponse

client: MasksPreviewsClient = picsart_sdk.client(PicsartAPI.MASKS_PREVIEWS)
response: MasksPreviewsApiResponse = client.masks_previews(image_path="./your-file.jpg", mask=["lace1", "lace2"])
print(response.data[0].mask, response.data[0].url)
print(response.data[0].mask, response.data[1].url)
```

#### 14. Adjust

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import AdjustClient
from picsart_sdk.api_responses import ApiResponse

path = "tests/resources/image2.jpg"
client: AdjustClient = picsart_sdk.client(PicsartAPI.ADJUST)
response: ApiResponse = client.adjust(image_path=path, contrast=50)
```

#### 15. Basic Edit

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import EditClient
from picsart_sdk.api_responses import ApiResponse

path = "tests/resources/image2.jpg"
client: EditClient = picsart_sdk.client(PicsartAPI.EDIT)
response: ApiResponse = client.edit(image_path=path, rotate=90)
print(response.data.url)
```

#### 16. Texture Generator

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import TextureGeneratorClient
from picsart_sdk.api_responses import ApiResponse

path = "tests/resources/image2.jpg"
client: TextureGeneratorClient = picsart_sdk.client(PicsartAPI.TEXTURE_GENERATOR)
response: ApiResponse = client.texture_generator(image_path="./your-file.jpg")
print(response.data.url)
```

#### 17. Vectorizer

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import VectorizerClient
from picsart_sdk.api_responses import ApiResponse

client: VectorizerClient = picsart_sdk.client(PicsartAPI.VECTORIZER)
response: ApiResponse = client.vectorizer(image_path="./your-file.jpg")
print(response.data.url)
```

#### 18. Surfacemap

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import SurfacemapClient
from picsart_sdk.api_responses import ApiResponse

client: SurfacemapClient = picsart_sdk.client(PicsartAPI.SURFACEMAP)
response: ApiResponse = client.surfacemap(
    image_path="./your-file.jpg", 
    mask_path="./mask-file.png", 
    sticker_path="./sticker.jpg"
)
print(response.data.url)
```

#### 18. Image Tagging

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import ImageTaggingClient
from picsart_sdk.api_responses.image_tagging_api_response import ImageTaggingApiResponse

client: ImageTaggingClient = picsart_sdk.client(PicsartAPI.IMAGE_TAGGING)
response: ImageTaggingApiResponse = client.get_tags(image_path="./your-file.jpg")
print(response.data.tags)
```

#### 19. Image Description

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import ImageDescriptionClient
from picsart_sdk.api_responses.image_description_api_response import ImageDescriptionApiResponse

client: ImageDescriptionClient = picsart_sdk.client(PicsartAPI.IMAGE_DESCRIPTION)
response: ImageDescriptionApiResponse = client.get_description(image_path="./your-file.jpg")
print(response.data.description)
```

#### 20. Get the balance

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import BalanceClient
from picsart_sdk.api_responses.balance_response import BalanceApiResponse

client: BalanceClient = picsart_sdk.client(PicsartAPI.BALANCE)
response: BalanceApiResponse = client.get_balance()
print(response.credits)
```

#### 21. Text2Image

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import Text2ImageClient
from picsart_sdk.api_responses.text2image_response import Text2ImageApiResponse, Text2ImageCreateApiResponse

client: Text2ImageClient = picsart_sdk.client(PicsartAPI.TEXT2IMAGE)
response1: Text2ImageCreateApiResponse = client.text2image(prompt="a cat in the green field", count=2)
response2: Text2ImageApiResponse = client.get_text2image_result(response1.inference_id)
print(response2.data[0].url)  # will generate 2 images
```

#### 22. Text2Text

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import Text2TextClient
from picsart_sdk.api_responses.text2text_response import Text2TextApiResponse 

client: Text2TextClient = picsart_sdk.client(PicsartAPI.TEXT2IMAGE)
response: Text2TextApiResponse = client.chat_completions(role="assistant", content="what is cat?")
print(response.data)
```

#### 23. Inpainting

#### Getting the results synchronously (request -> response)

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import InpaintingClient
from picsart_sdk.api_responses.painting_response import PaintingApiResponse

client: InpaintingClient = picsart_sdk.client(PicsartAPI.INPAINTING)
response: PaintingApiResponse = client.inpainting(
    image_path="./your-file.jpeg",
    mask_path="./your_mask.png",
    prompt="a green field",
    mode="sync",
    count=2,
)
print(response.data[0].url)
print(response.data[1].url)
```

#### Getting the results asynchronously

```python
import time
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import InpaintingClient
from picsart_sdk.api_responses.painting_response import PaintingApiResponse

client: InpaintingClient = picsart_sdk.client(PicsartAPI.INPAINTING)
response: PaintingApiResponse = client.inpainting(
    image_path="./your-file.jpeg",
    mask_path="./your_mask.png",
    prompt="a green field",
    mode="async",  # <- ask for results asynchronously
    count=2,
)
time.sleep(10)  # wait for the results to be ready
response: PaintingApiResponse = client.get_result(inference_id=response.inference_id)
print(response.data[0].url)
print(response.data[1].url)
```

#### 24. Outpainting

Similar with Inpainting, but using 

```python
client: OutpaintingClient = picsart_sdk.client(PicsartAPI.OUTPAINTING)
```

#### 25. Smart Replace Background

Similar with Inpainting, but using 

```python
client: PaintingReplaceBackgroundClient = picsart_sdk.client(PicsartAPI.REPLACE_BACKGROUND)
```

#### 25. Expand

Similar with Inpainting, but using 

```python
client: PaintingExpandClient = picsart_sdk.client(PicsartAPI.EXPAND)
```


#### 26. Bleed

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import BleedClient

client: BleedClient = picsart_sdk.client(PicsartAPI.BLEED)
res = client.bleed(image_path="./your-file.jpg", bleed_size=30)
print(res)
```

#### 27. GenAI Balance

```python
import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.clients import GenAiBalanceClient
from picsart_sdk.api_responses.balance_response import BalanceApiResponse

client: GenAiBalanceClient = picsart_sdk.client(PicsartAPI.GEN_AI_BALANCE)
response: BalanceApiResponse = client.get_balance()
print(response.credits)
```


# Async Client
The SDK includes an async HTTP client built on Python's async implementation, enabling non-blocking API requests for optimal performance in high-concurrency applications. The async client mirrors the interface of the synchronous client, making it easy to switch between the two.

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

# Async Endpoints

Some Picsart API endpoints support `asynchronous processing`, 
allowing you to initiate a request that returns a transaction_id. 
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

