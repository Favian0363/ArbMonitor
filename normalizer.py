# return normalized data
class MarketData:
    def __init__(self, ticker, bid, ask, site):
        self.ticker = ticker
        self.bid = float(bid)
        self.ask = float(ask)
        self.site = site

    def __repr__(self):
        return f"[{self.site}] {self.ticker} | Bid: ${self.bid:.2f} | Ask: ${self.ask:.2f}"

# pass in a single markets json and return ticker & prices
class KalshiNormalizer: 
    def handle_float(self, value):
        if value is None:
            return 0.0
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0
        
    def normalize(self, raw_json):
        ticker = raw_json['event']['event_ticker']
        market_info = raw_json['event']['markets'][0]

        bid_price = self.handle_float(market_info.get('yes_bid_dollars'))
        ask_price = self.handle_float(market_info.get('yes_ask_dollars'))
        return MarketData(ticker, bid_price, ask_price, 'KALSHI')

class PolymarketNormalizer:
    def handle_float(self, value):
        if value is None:
            return 0.0
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0
        
    def normalize(self, raw_json):
        ticker = raw_json['ticker']
        market_info = raw_json['markets'][0]

        bid_price = self.handle_float(market_info.get('bestBid'))
        ask_price = self.handle_float(market_info.get('bestAsk'))
        return MarketData(ticker, bid_price, ask_price, 'POLYMARKET')

def normalize(json, platform):
    if platform == 'polymarket':
        pM = PolymarketNormalizer()
        normalized_polyM = pM.normalize(json)
        return normalized_polyM
    elif platform == 'kalshi':
        k = KalshiNormalizer()
        normalized_kalshi = k.normalize(json)
        return normalized_kalshi
    return 'unrecognized platform'
