from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat


@dataclass
class EffectsPreviewsRequest(BaseRequest):
    image: PicsartImage
    effect_names: list[str]
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
