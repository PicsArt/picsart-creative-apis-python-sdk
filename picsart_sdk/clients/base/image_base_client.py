from abc import ABC

from picsart_sdk.clients.base.base_client import BaseClient


class ImageBaseClient(BaseClient, ABC):

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(ImageBaseClient, self).__init__(session, *args, **kwargs)

    @property
    def base_url(self):
        return "https://api.picsart.io/tools"

    def set_payload(self, request):
        if request.image.image_url is not None:
            self._payload = self._payload or {}
            self._payload.setdefault("image_url", request.image.image_url)

        if request.image.image_path:
            self._files = self._files or {}
            self._files.setdefault(
                "image",
                (
                    request.image.image_path,
                    open(request.image.image_path, "rb"),
                ),
            )
