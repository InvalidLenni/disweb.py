from typing import Optional

import aiohttp

__all__ = (
    "HTTPException",
    "NotFound",
    # Not released yet: "RatelimitException",
    "DiswebServerError",
)


class DiswebAPIException(Exception):
    """Base module Exception class."""


class HTTPException(DiswebAPIException):
    """Base Exception for HTTP errors."""

    def __init__(self, response: aiohttp.ClientResponse, message: Optional[str] = None):
        self.status: int = response.status
        self.response: aiohttp.ClientResponse = response
        message = f"({self.status}): {message}" if message else f"({self.status})"
        super().__init__(message)


class NotFound(HTTPException):
    """Raised when the guild or user is not found."""

    def __init__(
            self,
            response: aiohttp.ClientResponse,
            message: Optional[str] = "Guild or user was not found.",
    ):
        super().__init__(response, message)


class RatelimitException(HTTPException):
    # Raised when ratelimit responses are recieved.
    # INFO: Not released in the raw api yet.

    def __init__(
            self,
            response: aiohttp.ClientResponse,
            message: Optional[str] = "Slow down! You are being ratelimited!",
    ):
        super().__init__(response, message)

    pass


class DiswebServerError(HTTPException):

    def __init__(
            self,
            response: aiohttp.ClientResponse,
            message: Optional[str] = "There was an internal error in the Disweb servers.",
    ):
        super().__init__(response, message)
