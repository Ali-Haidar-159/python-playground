import asyncio

async def fake_api() :
    await asyncio.sleep(2)
    # raise Exception("API does not working")
    print("API working")


async def api_call (api_url_func,retry,timeout) :
    
    attempt = 1 
    
    for attempt in range(retry) :
        try : 
            attempt+=1
            await asyncio.wait_for(api_url_func(),timeout=timeout)
            break

        except Exception as e : 
            print("Find exception : ",e , "Attempt - ",attempt)
        
        if attempt == retry :
            break


async def main() :
    await api_call(fake_api,5,3)
    print("main func ending .")
        
        
asyncio.run(main())