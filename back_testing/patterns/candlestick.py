import os
import pandas as pd
import vectorbt as vbt
import yfinance as yf

from datetime import datetime, timedelta

import talib
# See github talib documentation for more information -- hammer patterns
# Buy hammer
# Sell shooting star, hanging man
hour_test = os.path.join(os.path.dirname(__file__), "test", "Bitstamp_BTCUSD_1h.csv")

end = datetime.now()
start = end - timedelta(days=20)

#data = yf.download("BTC-USD", start=start, end=end, interval="1h")
data = pd.read_csv(hour_test)
data["unix"] = pd.to_datetime(data["unix"], unit="s")
data = data.iloc[::-1]
data = data.set_index("unix")
data = data[["open", "high", "low", "close"]]
data.columns = ["Open", "High", "Low", "Close"]

#data = data.set_index("Date")
#data.index = pd.to_datetime(data.index)
#data = data.sort_index()

#print(data)
hammer = talib.CDLHAMMER(data.Open, data.High, data.Low, data.Close)
hanging_man = talib.CDLHANGINGMAN(data.Open, data.High, data.Low, data.Close)

# Hammer will return either 0, 100, or -100
print("-- Hammer Pattern --")
print(hammer[hammer == 100])

print("-- Hanging Man Pattern --")
print(hanging_man[hanging_man == -100])

buys = (hammer == 100)
sells = (hanging_man == -100)

pf = vbt.Portfolio.from_signals(data.Close, buys, sells, fees = 0.005)

print(pf.stats())
pf.plot().show()
