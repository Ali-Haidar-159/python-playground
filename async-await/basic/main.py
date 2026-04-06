import asyncio

counter = 0 

async def fetch_data() :
    global counter

    await asyncio.sleep(3)
    lock = asyncio.Lock()
    async with lock :
        counter = counter + 1 
    print (f"data is fetched - {counter}")


async def main():
    await fetch_data()
    await fetch_data()
    await fetch_data()
    await fetch_data()

asyncio.run(main())