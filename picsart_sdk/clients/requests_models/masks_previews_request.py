from dataclasses import dataclass, field
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class MasksPreviewsRequest(BaseRequest):
    image: PicsartImage
    blend: str = "screen"
    mask: list[str] = field(default_factory=lambda: ["lace1"])
    opacity: int = 100
    hue: int = 0
    mask_flip: str = ""
    preview_size: Optional[int] = 120
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
