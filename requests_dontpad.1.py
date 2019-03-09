# modified fetch function with semaphore
import random
import asyncio
from aiohttp import ClientSession
import time

async def fetch(url, session):
    async with session.post(url, data={'text':'bot11'} ) as response:
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        print("{}:{} with delay {}".format(date, response.url, delay))
        return await response.read()


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        await fetch(url, session)


async def run(r):
    url = "http://34.219.164.43:3500/porradeirasinistra"
    tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(60000)

    # Create client session that will ensure we dont open new connection
    # per each request.
    async with ClientSession() as session:
        for i in range(r):
            # pass Semaphore and session to every GET request
            task = asyncio.ensure_future(bound_fetch(sem, url.format(i), session))
            tasks.append(task)
           

        responses = asyncio.gather(*tasks)
        await responses
    
def worker(): 
    number = 600000
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(number))
    return loop.run_until_complete(future)
      

if __name__ == "__main__": 
    while True:
        worker()
       
  
       
        
    
    
   