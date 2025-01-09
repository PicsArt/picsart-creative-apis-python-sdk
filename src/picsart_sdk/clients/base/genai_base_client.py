from abc import ABC

from picsart_sdk.clients.base.base_client import BaseClient
from picsart_sdk.settings import PICSART_IMAGE_GENAI_API_VERSION


class GenAiBaseClient(BaseClient, ABC):

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(GenAiBaseClient, self).__init__(session, *args, **kwargs)

    def set_payload(self, request):
        self._payload.update(request.get_dict())

    @property
    def base_url(self):
        return "https://genai-api.picsart.io"

    @property
    def version(self):
        return self._version or PICSART_IMAGE_GENAI_API_VERSION
