import picsart_sdk
from picsart_sdk import PicsartAPI
from picsart_sdk.api_responses.balance_response import BalanceApiResponse
from picsart_sdk.clients import GenAiBalanceClient

client: GenAiBalanceClient = picsart_sdk.client(PicsartAPI.GEN_AI_BALANCE)
response: BalanceApiResponse = client.get_balance()
print(response.credits)
