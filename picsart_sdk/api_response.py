from dataclasses import dataclass
from typing import Optional


@dataclass
class ApiResponseData:
    id: str
    url: str


@dataclass
class ApiResponse:
    status: str
    data: ApiResponseData
    transaction_id: Optional[str] = None
