import httpx


class BaseClient:
    def __init__(self, api_key: str, base_url: str = "https://api.picsart.io", timeout: int = 30):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    # def _validate_response(self, response: httpx.Response):
    #     if response.status_code != 200:
    #         raise PicsartSDKException(f"API Error: {response.status_code} - {response.text}")
    #     return validate_response(response.json())
