from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient


class CommonBalanceClient(ImageBaseClient):
    @property
    def _endpoint(self):
        return "balance"

    def parse_response(self, result: dict, request_method: str) -> BalanceApiResponse:
        return BalanceApiResponse(credits=result.get("credits"))


class BalanceClient(CommonBalanceClient):
    """
    Client for retrieving account balance.

    This client provides a method to fetch the current balance associated
    with the account using the API.
    """

    def get_balance(self) -> BalanceApiResponse:
        """
        Retrieve the current account balance.

        :return: The balance information returned by the API.
        """
        return self.get()


class AsyncBalanceClient(CommonBalanceClient):
    async def get_balance(self) -> BalanceApiResponse:
        """
        Retrieve the current account balance using the HTTP asynchronous client.

        :return: The balance information returned by the API.
        """
        return await self.async_get()
