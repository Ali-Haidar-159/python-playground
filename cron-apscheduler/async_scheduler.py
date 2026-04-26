import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def job():
    print("Sync running")


async def main():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        job,
        "interval",
        seconds=5,
        id="api_sync",
        max_instances=1
    )

    scheduler.start()

    # # keep app alive
    await asyncio.Event().wait()


asyncio.run(main())