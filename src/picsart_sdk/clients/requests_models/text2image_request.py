from dataclasses import dataclass
from typing import Optional

from picsart_sdk.clients.base.genai_base_request import GenAiBaseRequest


@dataclass
class Text2ImageRequest(GenAiBaseRequest):
    prompt: str
    negative_prompt: str
    width: Optional[int] = 1024
    height: Optional[int] = 1024
    count: Optional[int] = 2
