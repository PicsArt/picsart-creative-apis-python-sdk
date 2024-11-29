from dataclasses import dataclass


@dataclass
class EffectsList:
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
