from dataclasses import dataclass


@dataclass
class EffectsListApiResponse:
    """
    Response object with the list of effects.

    :param effects: The list of available effects.
    """

    effects: list[str]


@dataclass
class EffectsPreviewsApiResponseData:
    """
    Represents the data of an API response.

    :param id: The unique identifier for the response data.
    :type id: str
    :param url: The URL associated with the response data.
    :type url: str
    :param effect_name: The effect name associated with the response data.
    :type effect_name: str
    """

    id: str
    url: str
    effect_name: str


@dataclass
class EffectsPreviewsApiResponse:
    """
    Represents the response returned by the Effects Previews API.

    :param status: The status of the API response (e.g., "success", "error").
    :type status: str
    :param data: The main data payload of the API response.
    :type data: EffectsPreviewsApiResponseData
    """

    status: str
    data: list[EffectsPreviewsApiResponseData]
