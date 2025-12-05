class MarketData:
    def __init__(self, ticker, bid, ask, site):
        self.ticker = ticker
        self.bid = float(bid)
        self.ask = float(ask)
        self.site = site

    def __repr__(self):
        return f"[{self.site}] {self.ticker} | Bid: ${self.bid:.2f} | Ask: ${self.ask:.2f}"

# pass in a single markets json and return its formatted price
class KalshiNormalizer: 
    def normalize(self, raw_json):
        pass

class PolymarketNormalizer:
    def normalize(self, raw_json):
        pass

