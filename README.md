# ArbMonitor
Real time arbitrage monitor between Kalshi and Polymarket. 

Goal is to identify price discrepancies for identical events between both platforms
and capitalize on opportunities.

1. Creating MVP (prototype)
- Level 1 Ticker Data <-/->
- Extracting & Normalizing <-/-> 
- Binary Market Support <-/->
- Setting up concurrency with asyncio <-/->

2. Support multiple events <-!->
- Support non-binary markets 

3. Implement persistent Websockets API instead of passive RestAPI

3. Refactor 
- Level 2 Orderbook Data
- Calculate VWAP (Volume Weighted Average Price)
- Actual execution & liquidity
