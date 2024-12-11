from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient


class CommonGenAiBalanceClient(GenAiBaseClient):
    @property
    def endpoint(self):
        return "balance"

    def parse_response(self, result: dict, request_method: str) -> BalanceApiResponse:
        return BalanceApiResponse(**result)


class GenAiBalanceClient(CommonGenAiBalanceClient):
    def get_balance(self) -> BalanceApiResponse:
        return self.get()


class AsyncGenAiBalanceClient(CommonGenAiBalanceClient):
    async def get_balance(self) -> BalanceApiResponse:
        return await self.async_get()
