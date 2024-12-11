from dataclasses import dataclass
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


class UltraUpscaleMode(str, Enum):
    SYNC = "sync"
    ASYNC = "async"
    AUTO = "auto"


@dataclass
class UltraUpscaleRequest(BaseRequest):
    image: PicsartImage
    upscale_factor: int = 2
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
    mode: Optional[UltraUpscaleMode] = UltraUpscaleMode.SYNC
