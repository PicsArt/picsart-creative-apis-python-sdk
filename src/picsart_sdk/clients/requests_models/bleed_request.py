from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class BleedRequest(BaseRequest):
    image: PicsartImage
    prompt: Optional[str] = None
    bleed_size: Optional[int] = 5
    negative_prompt: Optional[str] = ""
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
