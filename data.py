import aiohttp
import asyncio
import normalizer as n

polymarketEventUrl = "https://gamma-api.polymarket.com/events/slug/ethereum-all-time-high-by-december-31"
kalshiEventUrl = "https://api.elections.kalshi.com/trade-api/v2/events/KXETHATH-25DEC31?with_nested_markets=true"

# concurrently request data to each platforms API
async def get_tasks(session, url):
    async with session.get(url) as response: 
        response.raise_for_status() # check for errors 
        return await response.json() # return api response as json

# store requested data
async def get_data():
    urls = [polymarketEventUrl, kalshiEventUrl]
    async with aiohttp.ClientSession() as session: # start session for http requests
        tasks = []
        for url in urls:
            tasks.append(get_tasks(session, url)) # start tasks simultaneously 
        return await asyncio.gather(*tasks) # wait until tasks finish and return 

if __name__ == '__main__':
    raw_data = asyncio.run(get_data())
    raw_poly = raw_data[0]
    raw_kalshi = raw_data[1]
    print(n.normalize(raw_poly, 'polymarket'))
    print(n.normalize(raw_kalshi, 'kalshi'))
