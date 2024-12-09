from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient


class CommonBalanceClient(ImageBaseClient):
    @property
    def endpoint(self):
        return "balance"

    def parse_response(self, result):
        return BalanceApiResponse(credits=result.get("credits"))


class BalanceClient(CommonBalanceClient):
    def get_balance(self) -> BalanceApiResponse:
        return super().get()


class AsyncBalanceClient(CommonBalanceClient):
    async def get_balance(self) -> BalanceApiResponse:
        return await super().async_get()
