import os
from unittest.mock import patch

import pytest

import picsart_sdk
from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients import BalanceClient
from picsart_sdk.clients.client_factory import ApiClient
from picsart_sdk.errors import ApiAuthenticationError


@pytest.mark.skipif(
    not os.getenv("PICSART_API_KEY"),
    reason="PICSART_API_KEY environment variable is not set",
)
def test_authentication_success():
    client: BalanceClient = picsart_sdk.client(ApiClient.BALANCE)
    result = client.get_balance()
    assert isinstance(result, BalanceApiResponse)


@patch.dict(os.environ, {"PICSART_API_KEY": "invalid"})
def test_authentication_error():
    client: BalanceClient = picsart_sdk.client(ApiClient.BALANCE)
    with pytest.raises(ApiAuthenticationError):
        client.get_balance()
