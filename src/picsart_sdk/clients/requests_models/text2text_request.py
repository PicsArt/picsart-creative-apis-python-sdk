from dataclasses import dataclass, field
from typing import Optional

from picsart_sdk.clients.base.genai_base_request import GenAiBaseRequest


@dataclass
class Text2ImageMessage:
    role: str
    content: str


@dataclass
class Text2TextRequest(GenAiBaseRequest):
    max_tokens: Optional[int] = 512
    temperature: Optional[int] = 1
    messages: list[Text2ImageMessage] = field(default_factory=lambda: [])
