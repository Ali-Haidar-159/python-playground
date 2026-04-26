import asyncio

async def magic() :
    print("hello world")
    
x = magic() # returns a coroutine 

asyncio.run(magic())
asyncio.run(x)


# Every Async func is a Coroutine 