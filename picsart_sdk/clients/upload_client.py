from picsart_sdk import Session
from picsart_sdk.clients.base_client import BaseClient


class UploadClient(BaseClient):
    def __init__(self, session: Session, *args, **kwargs):
        super(UploadClient, self).__init__(session, *args, **kwargs)
