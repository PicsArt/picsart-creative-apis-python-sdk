from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class EffectsPreviewsRequest(BaseRequest):
    image: PicsartImage
    effect_names: list[str]
    preview_size: Optional[int] = 120
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
