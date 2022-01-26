import asyncio
import logging
from typing import Dict, Optional

import aiohttp

from .exceptions import (
    HTTPException,
    # Not released yet: InvalidToken,
    NotFound,
)
from .objects import Guild, User

__all__ = ("DiswebClient",)

logger = logging.getLogger(__name__)


class DiswebClient:
    """
    The client used to make requests to the Disweb API.

    Attributes
    ----------
    session: aiohttp.ClientSession
        The client session used to make requests to the  API.
    """

    BASE_URL = "https://disweb.glitch.me/"
    HTTP_response_errors = {
        404: NotFound,
        # Not released yet: 403: InvalidToken,

    }

    def __init__(
            self,
            # Not released yet: token: str,
            /,
            *,
            session: Optional[aiohttp.ClientSession] = None,
    ):
        self.session = session or aiohttp.ClientSession()
        # Not released yet: self._default_headers = {"Authorization": token}

        self.lock = asyncio.Lock()

        # Ratelimit Section (In the raw api not released yet)
        """
        self.requests = 0
        self.last_reset = time.time()

        self.max_requests = 45
        self.request_period = 60
        """

    async def close(self):
        """
        Closes the client resources.

        This must be called once the client is no longer in use.
        """
        await self.session.close()

    async def fetch_user(self, user_id: int) -> User:
        """
        Fetches a user from the Disweb API.

        Parameters
        ----------
        user_id: int
            The id from the user.
        """
        data = await self.request(f"/user/{user_id}")
        return User(data)

    async def fetch_guild(self, guild_id: int) -> Guild:
        """
        Fetch guild id from the Disweb API.

        The disweb bot must be on the guild for fetch guild informations!

        Parameters
        ----------
        guild_id: int
            The guild ID to fetch the user from.
            

        """

        data = await self.request(
            f"guild/{guild_id}",
            method="GET",
        )

        return Guild(guild_id, data)

    @classmethod
    async def check_response_for_errors(cls, response: aiohttp.ClientResponse):
        if response.status > 399 or response.status < 200:
            error = cls.HTTP_response_errors.get(response.status, HTTPException)
            try:
                message = (await response.json())["error"]
            except Exception:
                message = await response.text()
            raise error(response, message)

    async def request(
            self,
            endpoint: str,
            *,
            method: str = "GET",
            json: Dict = {},
            # extra_headers: Dict = {},
    ) -> Dict:

        # headers = dict(self._default_headers, **extra_headers)

        async with self.session.request(
                method=method, url=self.BASE_URL + endpoint, json=json,  # headers=headers, params=params
        ) as response:
            pass
            """
            if self.useantiratelimit:
                self.requests += 1
            """
            await self.check_response_for_errors(response)

            return await response.json()


"""
    async def check_ratelimit(self):
        async with self.lock:
            elapsed = self.last_reset - time.time()

            if elapsed >= self.request_period:
                self.requests = 0

            if self.requests >= self.max_requests - 1:
                await self.wait_for_ratelimit_end()

    async def wait_for_ratelimit_end(self):
        for count in range(1, 6):
            wait_amount = 2 ** count

            logger.warning(
                "Slow down, you are about to be rate limited. "
                f"Trying again in {wait_amount} seconds."
            )
            await asyncio.sleep(wait_amount)

            if self.requests != self.max_requests - 1:
                break
"""
