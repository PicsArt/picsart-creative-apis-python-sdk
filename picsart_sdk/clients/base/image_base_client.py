from abc import ABC

from picsart_sdk.clients.base.base_client import BaseClient


class ImageBaseClient(BaseClient, ABC):

    def __init__(self, session, *args, **kwargs):
        self.session = session
        super(ImageBaseClient, self).__init__(session, *args, **kwargs)

    @property
    def base_url(self):
        return "https://api.picsart.io/tools"
