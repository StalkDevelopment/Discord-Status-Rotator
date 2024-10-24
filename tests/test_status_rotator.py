import unittest
import asyncio
from src.main import StatusRotator
from unittest.mock import AsyncMock, MagicMock

class TestStatusRotator(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = MagicMock()
        self.statuses = ["Playing a game", "Listening to music", "Watching a movie"]
        self.interval = 1
        self.rotator = StatusRotator(self.client, self.statuses, self.interval)
        self.rotator.status_cycle = iter(self.statuses)

    async def test_rotate_status(self):
        self.client.change_presence = AsyncMock()
        task = asyncio.create_task(self.rotator.rotate_status())
        await asyncio.sleep(3)
        task.cancel()

        self.client.change_presence.assert_any_call(activity=unittest.mock.ANY)
        self.assertEqual(self.client.change_presence.call_count, 3)

if __name__ == "__main__":
    unittest.main()
