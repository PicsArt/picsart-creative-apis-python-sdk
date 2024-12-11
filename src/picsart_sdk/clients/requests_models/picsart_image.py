import os
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PicsartImageFormat(str, Enum):
    PNG = "png"
    JPG = "jpg"
    WEBP = "webp"


@dataclass
class PicsartImage:
    image_url: Optional[str] = None
    image_path: Optional[str] = None

    def __post_init__(self):
        """
        Ensure at least one field is provided
        """
        provided_fields = sum(
            bool(field) for field in [self.image_url, self.image_path]
        )
        if provided_fields == 0:
            raise ValueError(
                "At least one of `image_url`, or `image_path` must be provided."
            )
        if provided_fields > 1:
            raise ValueError(
                "Only one of `image_url`, or `image_path` can be provided."
            )

        if self.image_path and not os.path.isfile(self.image_path):
            raise ValueError(f"The file path does not exist: {self.image_path}")
