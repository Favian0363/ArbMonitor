import requests
import json

api = "https://gamma-api.polymarket.com/"
markets = "https://gamma-api.polymarket.com/markets/slug/"
events = "https://gamma-api.polymarket.com/events/slug/"
file = "data.json"

event = requests.get(events + "russia-x-ukraine-ceasefire-in-2025")
data = event.json()

with open(file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
