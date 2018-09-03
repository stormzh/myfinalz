from iexfinance import get_historical_data
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#import plotly.offline
import plotly
import plotly.graph_objs as go

start = datetime(2018, 8, 9)
end = datetime(2018, 9, 2)

df = get_historical_data("AAPL", start=start, end=end, output_format='pandas')
print(df.head(20))
df = df.reset_index()
trace = go.Candlestick(x=df.date,
                       open=df.open,
                       high=df.high,
                       low=df.low,
                       close=df.close)
data = [trace]
#plotly.offline.tools.set_credentials_file(username='stormzhg', api_key='p1tlAm0VVn16DeDmGHYr')
plotly.offline.plot(data, filename='simple_candlestick.html')