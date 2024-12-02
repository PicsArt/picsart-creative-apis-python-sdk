import pytest

import picsart_sdk
from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients.balance_client import BalanceClient, AsyncBalanceClient


def assert_balance(result):
    assert isinstance(result, BalanceApiResponse)
    assert isinstance(result.credits, int)
    assert int(result.credits) >= 0


def test_get_balance():
    client: BalanceClient = picsart_sdk.client("balance")
    result = client.get_balance()

    assert_balance(result)


@pytest.mark.asyncio
async def test_get_balance_async():
    client: AsyncBalanceClient = picsart_sdk.async_client("balance")
    result = await client.get_balance()
    assert_balance(result)
