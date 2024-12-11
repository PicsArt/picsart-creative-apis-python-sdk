from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class AdjustRequest(BaseRequest):
    image: PicsartImage
    brightness: Optional[int] = 0
    contrast: Optional[int] = 0
    clarity: Optional[int] = 0
    saturation: Optional[int] = 0
    hue: Optional[int] = 0
    shadows: Optional[int] = 0
    highlights: Optional[int] = 0
    temperature: Optional[int] = 0
    sharpen: Optional[int] = 0
    noise: Optional[int] = 0
    vignette: Optional[int] = 0
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
