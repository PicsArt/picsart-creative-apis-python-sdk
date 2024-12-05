from dataclasses import dataclass, fields
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models import PicsartImage, PicsartImageFormat


class PaintingMode(str, Enum):
    SYNC = "sync"
    ASYNC = "async"
    AUTO = "auto"


@dataclass
class InpaintingRequest(BaseRequest):
    image: PicsartImage
    mask: PicsartImage
    prompt: str
    negative_prompt: Optional[str] = ""
    count: Optional[int] = 4
    format: Optional[PicsartImageFormat] = PicsartImageFormat.JPG
    mode: Optional[PaintingMode] = PaintingMode.SYNC

    def get_dict(self):
        data = super().get_dict()
        del data["mask"]
        for field in fields(self):
            if isinstance(getattr(self, field.name), Enum):
                data[field.name] = getattr(self, field.name).value

        return data
