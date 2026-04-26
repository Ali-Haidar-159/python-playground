import asyncio 

async def work() :
    print("processing ..")
    await asyncio.sleep(10)
    print("Work DONE")
    
async def main() :
    # await work()
    await asyncio.wait_for(work(),timeout=3)
    print("hello")
    
asyncio.run(main())