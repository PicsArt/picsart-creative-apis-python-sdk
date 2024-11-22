from dataclasses import dataclass
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


class RemoveBackgroundOutputType(str, Enum):
    CUTOUT = "cutout"
    MASK = "mask"


class RemoveBackgroundScale(str, Enum):
    FIT = "fit"
    FILL = "fill"


class RemoveBackgroundShadow(str, Enum):
    DISABLED = "disabled"
    CUSTOM = "custom"
    BOTTOM = "bottom"
    BOTTOM_RIGHT = "bottom-right"
    BOTTOM_LEFT = "bottom-left"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    TOP_RIGHT = "top-right"
    TOP_LEFT = "top-left"


@dataclass
class RemoveBackgroundRequest(BaseRequest):
    image: PicsartImage
    output_type: Optional[RemoveBackgroundOutputType] = (
        RemoveBackgroundOutputType.CUTOUT
    )
    bg_image: Optional[PicsartImage] = None
    bg_color: Optional[str] = None
    bg_width: Optional[int] = None
    bg_height: Optional[int] = None
    scale: Optional[RemoveBackgroundScale] = RemoveBackgroundScale.FIT
    auto_center: Optional[bool] = False
    stroke_size: Optional[int] = 0
    stroke_color: Optional[str] = "FFFFFF"
    stroke_opacity: Optional[int] = 100
    shadow: Optional[RemoveBackgroundShadow] = RemoveBackgroundShadow.DISABLED
    shadow_opacity: Optional[int] = 20
    shadow_blur: Optional[int] = 50
    shadow_offset_x: Optional[int] = None
    shadow_offset_y: Optional[int] = None
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
