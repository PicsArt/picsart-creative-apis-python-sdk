from dataclasses import dataclass, fields
from enum import Enum
from typing import Optional, Union

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
    mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC.value

    def get_dict(self):
        data = super().get_dict()
        del data["mask"]
        for field in fields(self):
            if isinstance(getattr(self, field.name), Enum):
                data[field.name] = getattr(self, field.name).value

        return data


@dataclass
class ReplaceBackgroundRequest(BaseRequest):
    image: PicsartImage
    prompt: str
    negative_prompt: Optional[str] = ""
    count: Optional[int] = 4
    format: Optional[PicsartImageFormat] = PicsartImageFormat.JPG
    mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC.value


@dataclass
class ExpandRequest(BaseRequest):
    image: PicsartImage
    prompt: str
    width: Optional[int] = 1024
    height: Optional[int] = 1024
    direction: Optional[str] = "center"
    negative_prompt: Optional[str] = ""
    count: Optional[int] = 4
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG
    mode: Union[Optional[PaintingMode], str] = PaintingMode.SYNC.value
