import aiohttp
import asyncio
import time

async def fetch_url_async(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main_async():
    urls = ["https://httpbin.org/delay/2" for _ in range(5)]
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

    end_time = time.time()
    print(f"Time taken (asynchronous): {end_time - start_time} seconds")

asyncio.run(main_async())
