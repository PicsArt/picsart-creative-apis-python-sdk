from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class TextureGeneratorRequest(BaseRequest):
    image: PicsartImage
    width: Optional[int] = 1024
    height: Optional[int] = 1024
    offset_x: Optional[int] = 0
    offset_y: Optional[int] = 0
    pattern: Optional[str] = "hex"
    rotate: Optional[int] = 0
    scale: Optional[float] = 1
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
