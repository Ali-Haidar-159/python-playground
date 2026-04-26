import asyncio

async def task1(x) :
    print("hello ali-",x)
    await asyncio.sleep(5)
    print("world")
    
async def main() :
    
    # await asyncio.gather(task1(1), task1(2),task1(3))
    
    asyncio.create_task(task1(1))
    asyncio.create_task(task1(2))
    asyncio.create_task(task1(3))
    
    print("this is main function")
    
    await asyncio.sleep(10)

asyncio.run(main())