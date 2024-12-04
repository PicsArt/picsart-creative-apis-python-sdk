from dataclasses import dataclass


@dataclass
class Text2ImageApiResponse:
    inference_id: str
    status: str
