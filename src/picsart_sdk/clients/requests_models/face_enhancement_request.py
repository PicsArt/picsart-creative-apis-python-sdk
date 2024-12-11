from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class FaceEnhancementRequest(BaseRequest):
    image: PicsartImage
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
