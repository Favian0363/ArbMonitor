def check_for_arbitrage(market_a, market_b):
    spread = market_a.bid - market_b.ask
    
    if spread > 0.01:
        return f"Arbitrage found! Value of {spread}"
    else:
        return "No spread found"
