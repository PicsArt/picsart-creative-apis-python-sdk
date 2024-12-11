from dataclasses import dataclass


@dataclass
class EffectsListApiResponse:
    effects: list[str]


@dataclass
class EffectsPreviewsApiResponseData:
    id: str
    url: str
    effect_name: str


@dataclass
class EffectsPreviewsApiResponse:
    status: str
    data: list[EffectsPreviewsApiResponseData]
