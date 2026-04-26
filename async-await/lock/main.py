import asyncio

counter = 0
lock = asyncio.Lock()

async def work():
    global counter

    # temp = counter
    # await asyncio.sleep(0)   
    # counter = temp + 1 
    
    async with lock  : 
        temp = counter
        await asyncio.sleep(0)   
        counter = temp + 1 

async def main():
    await asyncio.gather(work(), work(), work())
    print(counter)

asyncio.run(main())