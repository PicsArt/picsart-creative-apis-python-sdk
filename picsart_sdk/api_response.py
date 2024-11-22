from dataclasses import dataclass


@dataclass
class ApiResponseData:
    id: str
    url: str


@dataclass
class ApiResponse:
    status: str
    data: ApiResponseData
