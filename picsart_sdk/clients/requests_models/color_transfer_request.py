from dataclasses import dataclass, asdict, fields
from enum import Enum
from typing import Optional

from picsart_sdk.clients.base.base_request import BaseRequest
from picsart_sdk.clients.requests_models.picsart_image import (
    PicsartImage,
    PicsartImageFormat,
)


@dataclass
class ColorTransferRequest(BaseRequest):
    image: PicsartImage
    reference_image: PicsartImage
    format: Optional[PicsartImageFormat] = PicsartImageFormat.PNG

    def get_dict(self):
        data = super().get_dict()
        del data["reference_image"]
        for field in fields(self):
            if isinstance(getattr(self, field.name), Enum):
                data[field.name] = getattr(self, field.name).value

        return data
