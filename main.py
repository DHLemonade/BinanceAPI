import ccxt
from datetime import datetime

#티커 조회
binance = ccxt.binance()
markets = binance.fetch_tickers()
print(markets.keys())

#현재가 조회
ticker = binance.fetch_ticker('ETH/BTC')
print(ticker['open'], ticker['high'], ticker['low'], ticker['close'])

#과거 데이터 조회
ohlcvs = binance.fetch_ohlcv('ETH/BTC')
print(ohlcvs)

#리스트를 보기좋게 변환
for ohlc in ohlcvs:
    print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), "\t", ohlc[1], "\t", ohlc[2], "\t", ohlc[3], "\t", ohlc[4], "\t", ohlc[5])

#호가 조회
orderbook = binance.fetch_order_book('ETH/BTC')
print(orderbook['bids'])
print(orderbook['asks'])

for ask in orderbook['asks']:
    print(ask[0], ask[1])

#잔고 조회
binance = ccxt.binance({
    'apiKey': 'Li4J8h5tuNTZFlhoSVO5FwE5mipuRW7cxlyIgwsD3xyTWdTvUzI19c4YZ5iInfOb',
    'secret': 'KAfuEMrWMbNFgg4qqVJQGNi1w2iWEu4OeHyIo1XQ0hiZUgSC93vA21dcHXhuHhyz',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

balance = binance.fetch_balance()
print(balance.keys())

print(balance['USDT'])