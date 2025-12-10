import aiohttp
import asyncio
import normalizer as n
from logic import check_for_arbitrage

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
    raw_poly, raw_kalshi = asyncio.run(get_data())
    norm_poly = n.normalize(raw_poly, 'polymarket')
    norm_kalshi = n.normalize(raw_kalshi, 'kalshi')
    print(norm_kalshi)
    print(norm_poly)
    print(check_for_arbitrage(norm_kalshi, norm_poly))
    # spread = bid_a - ask_b
