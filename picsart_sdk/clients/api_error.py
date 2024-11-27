class ApiError(Exception):
    """
    Raise this exception for errors related to API requests.

    Attributes:
        detail (str): A detailed error message.
        message (str): A user-friendly error message.
        code (int): The error code returned by the API.
    """

    def __init__(
        self,
        detail: str = None,
        message: str = None,
        code: int = None,
        response_data: dict = None,
    ):
        self.detail = detail
        self.message = message
        self.code = code

        if response_data:
            self.detail = response_data.get("detail", self.detail)
            self.message = response_data.get("message", self.message)
            self.code = response_data.get("code", self.code)

        super().__init__(self.__str__())

    def __str__(self):
        return f"{self.__class__.__name__}(detail={self.detail}, message={self.message}, code={self.code})"


class ApiAuthenticationError(ApiError):
    """
    Raise this exception for authentication errors.
    """

    pass
