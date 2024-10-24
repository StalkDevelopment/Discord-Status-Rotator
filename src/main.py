import discord
import asyncio
import itertools
from src.config import TOKEN, STATUS_ROTATION_INTERVAL
from src.statuses import get_next_status

class StatusRotator:
    def __init__(self, client, statuses, interval):
        self.client = client
        self.statuses = statuses
        self.interval = interval
        self.status_cycle = itertools.cycle(self.statuses)

    async def rotate_status(self):
        while True:
            next_status = get_next_status(self.status_cycle)
            await self.client.change_presence(activity=discord.Game(name=next_status))
            await asyncio.sleep(self.interval)

async def main():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    statuses = ["Playing a game", "Listening to music", "Watching a movie"]

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        rotator = StatusRotator(client, statuses, STATUS_ROTATION_INTERVAL)
        await rotator.rotate_status()

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
