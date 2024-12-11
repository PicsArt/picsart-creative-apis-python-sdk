from typing import Optional


class ApiError(Exception):
    """
    Exception raised for errors related to API requests.

    This exception provides detailed information about API errors,
    including the error message, code, and any additional response data.

    :param detail: A detailed error message returned by the API.
    :type detail: Optional[str]
    :param message: A user-friendly error message returned by the API.
    :type message: Optional[str]
    :param code: The error code returned by the API.
    :type code: Optional[int]
    :param response_data: The full error response returned by the API.
    :type response_data: Optional[dict]
    """

    def __init__(
        self,
        detail: Optional[str] = None,
        message: Optional[str] = None,
        code: Optional[int] = None,
        response_data: Optional[dict] = None,
    ):
        """
        Initialize the ApiError exception.
        """

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
