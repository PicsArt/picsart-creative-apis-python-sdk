import httpx
from picsart_sdk.api_client import BaseClient

class SyncClient(BaseClient):
    def __init__(self, api_key: str, base_url: str = "https://api.picsart.io", timeout: int = 30):
        super().__init__(api_key, base_url, timeout)
        self.client = httpx.Client(base_url=self.base_url, timeout=self.timeout)

    def upload(self, file_path: str):
        return upload.upload(self.client, self._build_headers(), file_path)

    def remove_background(self, image_url: str, options: dict):
        return remove_background.remove_background(self.client, self._build_headers(), image_url, options)

    def upscale(self, image_url: str, upscale_factor: int):
        return upscale.upscale(self.client, self._build_headers(), image_url, upscale_factor)

    def get_balance(self):
        return balance.get_balance(self.client, self._build_headers())

    def close(self):
        self.client.close()
