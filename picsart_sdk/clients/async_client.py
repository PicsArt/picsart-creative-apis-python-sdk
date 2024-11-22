import httpx
from picsart_sdk.client import BaseClient
from picsart_sdk.endpoints import upload, remove_background, upscale, balance


class AsyncClient(BaseClient):
    def __init__(self, api_key: str, base_url: str = "https://api.picsart.io", timeout: int = 30):
        super().__init__(api_key, base_url, timeout)
        self.client = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)

    async def upload(self, file_path: str):
        return await upload.upload(self.client, self._build_headers(), file_path)

    async def remove_background(self, image_url: str, options: dict):
        return await remove_background.remove_background(self.client, self._build_headers(), image_url, options)

    async def upscale(self, image_url: str, upscale_factor: int):
        return await upscale.upscale(self.client, self._build_headers(), image_url, upscale_factor)

    async def get_balance(self):
        return await balance.get_balance(self.client, self._build_headers())

    async def close(self):
        await self.client.aclose()
