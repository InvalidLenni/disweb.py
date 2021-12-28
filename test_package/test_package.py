import pytest


class TestEverything:
    async def check_client(self):
        try:
            _ = self.client
        except AttributeError:
            _ = self.client
            # Not released yet: self.client = DiswebClient(self.get_token())

    @pytest.mark.asyncio
    async def test_guild(self):
        """Tests the fetching guil function"""
        #await self.check_client()

        await self.client.fetch_guild(898212491409121280)

    @pytest.mark.asyncio
    async def pytest_sessionfinish(self):
        """Closes the session at the end of the tests"""
        await self.client.close()

        """
        # Not released yet: get_token
        def get_token(self):
                with open(__file__[:-15] + "disweb_secret", "r") as secret:
                    return secret.read()
        """
