from dataclasses import dataclass
from typing import Optional, IO


@dataclass
class UploadRequest:
    file_path: Optional[str]
    file_url: Optional[str]
    file_descriptor: Optional[IO[bytes]]
