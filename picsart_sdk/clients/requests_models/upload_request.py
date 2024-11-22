from dataclasses import dataclass

from picsart_sdk.clients.requests_models.picsart_image import PicsartImage


@dataclass
class UploadRequest:
    image: PicsartImage
