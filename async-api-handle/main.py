import aiohttp
import asyncio

async def api_call(url) :
    async with aiohttp.ClientSession() as session :
        async with session.get(url) as response :
            data = await response.json()
            
            return data
        
async def main() :
    data = await api_call("https://jsonplaceholder.typicode.com/users")
    
    for v in data :
        print(v.get("email"))


asyncio.run(main())
        
    