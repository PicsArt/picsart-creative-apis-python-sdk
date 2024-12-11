from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class EditRequest(BaseRequest):
    image: PicsartImage
    mode: Optional[str] = None
    size: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    flip: Optional[str] = None
    rotate: Optional[int] = 0
    perspective_horizontal: Optional[int] = 0
    perspective_vertical: Optional[int] = 0
    quality: Optional[int] = 90
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
