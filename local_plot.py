import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from iexfinance import get_historical_data
from mpl_finance import candlestick_ohlc


df = get_historical_data("AAPL", start="2017-8-9", end="2018-9-2", output_format='pandas')
#print(df.head(20))
#df = df.reset_index()
df['date'] = df.index.map(mdates.datestr2num)
f1, ax = plt.subplots(figsize = (10,5))
ohlc = df[['date','open','high','low','close']]
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.show()
