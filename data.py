import requests
import json

# polymarket uses floats for pricing
# retrieving all markets for ethATH
# slug is polymarket's term for an event

polymarketEventUrl = "https://gamma-api.polymarket.com/events/slug/"
pM_file = "poly_data.json"
pM_slug = "ethereum-all-time-high-by-december-31" # pM returns event with markets by default

# kalshi uses integers for pricing
# retrieving all markets for ethATH

kalshiEventUrl = "https://api.elections.kalshi.com/trade-api/v2/events/"
kalshi_file = "kalshi_data.json"
kalshi_slug = "KXETHATH-25DEC31?with_nested_markets=true" # query param to return event with markets

def retrieve_event_data(url, slug, file):
    response = requests.get(polymarketEventUrl + slug)
    data = response.json()

    with open(file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

retrieve_event_data(polymarketEventUrl, pM_file, pM_slug)
retrieve_event_data(kalshiEventUrl, kalshi_file, kalshi_slug)
