from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class UpscaleRequest(BaseRequest):
    image: PicsartImage
    upscale_factor: int
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
