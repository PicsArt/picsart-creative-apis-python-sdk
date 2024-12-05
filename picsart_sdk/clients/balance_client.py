from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient


class BalanceClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "balance"

    def get_balance(self) -> BalanceApiResponse:
        result = self.http_client.get(
            url=self.get_url(),
            headers=self.headers,
        )
        return BalanceApiResponse(credits=result.get("credits"))


class AsyncBalanceClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "balance"

    async def get_balance(self) -> BalanceApiResponse:
        result = await self.http_client.get(
            url=self.get_url(),
            headers=self.headers,
        )

        return BalanceApiResponse(credits=result.get("credits"))
