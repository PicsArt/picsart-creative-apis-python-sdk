from dataclasses import dataclass


@dataclass
class BalanceApiResponse:
    """
    Balance API Response

    :param credits: The number of credits remained
    """

    credits: int
