import os
from dataclasses import dataclass, field
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

    _field_name: str = field(default="image", init=True)

    def __post_init__(self):
        """
        Ensure at least one field is provided
        """
        provided_fields = sum(
            bool(field) for field in [self.image_url, self.image_path]
        )
        if provided_fields == 0:
            raise ValueError(
                f"At least one of `{self._field_name}_url`, or `{self._field_name}_path` must be provided."
            )
        if provided_fields > 1:
            raise ValueError(
                f"Only one of `{self._field_name}_url`, or `{self._field_name}_path` can be provided."
            )

        if self.image_path and not os.path.isfile(self.image_path):
            raise ValueError(f"The file path does not exist: {self.image_path}")
