import pytest

import picsart_sdk
from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.balance_client import AsyncBalanceClient, BalanceClient
from picsart_sdk.clients.client_factory import ApiClient


def assert_balance(result):
    assert isinstance(result, BalanceApiResponse)
    assert isinstance(result.credits, int)
    assert int(result.credits) >= 0


@pytest.mark.parametrize(
    "client_name",
    [
        ApiClient.BALANCE,
        ApiClient.GEN_AI_BALANCE,
    ],
)
def test_get_balance(client_name):
    client: BalanceClient = picsart_sdk.client(client_name)
    result = client.get_balance()

    assert_balance(result)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_name",
    [
        ApiClient.BALANCE,
        ApiClient.GEN_AI_BALANCE,
    ],
)
async def test_get_balance_async(client_name):
    client: AsyncBalanceClient = picsart_sdk.async_client(client_name)
    result = await client.get_balance()
    assert_balance(result)
