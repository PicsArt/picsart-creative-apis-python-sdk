from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.base.genai_base_client import GenAiBaseClient


class CommonGenAiBalanceClient(GenAiBaseClient):
    @property
    def _endpoint(self):
        return "balance"

    def parse_response(self, result: dict, request_method: str) -> BalanceApiResponse:
        return BalanceApiResponse(**result)


class GenAiBalanceClient(CommonGenAiBalanceClient):
    """
    Client for retrieving the account balance for the GenAI APIs.

    This client provides a method to fetch the current balance associated
    with the account using the API.
    """

    def get_balance(self) -> BalanceApiResponse:
        """
        Retrieve the current account balance.

        :return: The balance information returned by the API.
        """
        return self.get()


class AsyncGenAiBalanceClient(CommonGenAiBalanceClient):
    """
    Client for retrieving the account balance for the GenAI APIs.

    This client provides a method to fetch the current balance associated
    with the account using the API.
    """

    async def get_balance(self) -> BalanceApiResponse:
        """
        Retrieve the current account balance using the HTTP asynchronous client.

        :return: The balance information returned by the API.
        """
        return await self.async_get()
