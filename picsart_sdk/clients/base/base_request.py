from dataclasses import dataclass, asdict, fields
from enum import Enum


@dataclass
class BaseRequest:
    def get_dict(self):
        data = asdict(self)
        del data["image"]
        for field in fields(self):
            if isinstance(getattr(self, field.name), Enum):
                data[field.name] = getattr(self, field.name).value

        return data
