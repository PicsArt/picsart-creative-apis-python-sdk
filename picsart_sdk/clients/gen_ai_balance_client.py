from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient


class CommonGenAiBalanceClient(GenAiBaseClient):
    @property
    def endpoint(self):
        return "balance"

    def parse_response(self, result) -> BalanceApiResponse:
        return BalanceApiResponse(**result)


class GenAiBalanceClient(CommonGenAiBalanceClient):
    def get_balance(self) -> BalanceApiResponse:
        result = self.http_client.get(
            url=self.get_url(),
            headers=self.headers,
        )
        return BalanceApiResponse(credits=result.get("credits"))


class AsyncGenAiBalanceClient(CommonGenAiBalanceClient):
    async def get_balance(self) -> BalanceApiResponse:
        result = await self.http_client.get(
            url=self.get_url(),
            headers=self.headers,
        )

        return BalanceApiResponse(credits=result.get("credits"))
