import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

returns = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0)
returns['Date'] = pd.to_datetime(returns['Date'])
returns["Date"] = returns["Date"].apply(mdates.date2num)

ohlc= returns[['Date', 'PX_OPEN', 'PX_HIGH', 'PX_LOW','PX_LAST']].copy()
f1, ax = plt.subplots(figsize = (10,5))

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
plt.show()
# returns.plot()
# plt.title('Stock Data')
# plt.xlabel('Time')
# plt.legend(loc=0)

# prices = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0, usecols="A,B,C,D,E")
# prices.plot()
# plt.title('Prices')
# plt.xlabel('Time')
# plt.legend(loc=0)

# bb = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0, usecols="A,B,E,M,N,O")
# bb.plot()
# plt.title('BB')
# plt.xlabel('Time')
# plt.legend(loc=0)


plt.show();
