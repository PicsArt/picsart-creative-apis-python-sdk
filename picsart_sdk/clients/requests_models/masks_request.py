from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class MasksRequest(BaseRequest):
    image: PicsartImage
    blend: str = "screen"
    mask: str = "lace1"
    opacity: int = 100
    hue: int = 0
    mask_flip: str = ""
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
