import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import datetime as datetime
from mpl_finance import candlestick2_ohlc

from Algorithm.Demo import Demo as IW

returns = pd.read_excel('Data/stock_data.xlsx', sheet_name=2, index_col=0)
date = pd.read_excel('Data/stock_data.xlsx', sheet_name=2)


plt.figure(1)

#print(date)



plt.subplot(411)
#returns.plot()
plt.title('Stock Data')
plt.xlabel('Time')
plt.legend(loc=0)
  
oiw = IW.Model(returns)
score, cap, cap_daily_p = oiw.Core()
plt.plot(score)
plt.subplot(412)
plt.plot(cap_daily_p)
plt.subplot(413)
plt.plot(cap)


cap.append(0)
score.append(0)
px_last = returns['PX_LAST']
d = returns.index.tolist()
ex = pd.DataFrame({'Score': score, 'Capital': cap, 'Last_Price': px_last})
ex.to_excel('export.xlsx', sheet_name='export')

'''
plt.subplot(311)
prices = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0, usecols="A,B,C,D,E")
#prices.plot()
plt.title('Prices')
plt.xlabel('Time')
plt.legend(loc=0)
plt.plot(prices)

plt.subplot(312)
bb = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0, usecols="A,B,E,M,N,O")
#bb.plot()
plt.title('BB')
plt.xlabel('Time')
plt.legend(loc=0)
plt.plot(bb)
'''

ax = plt.subplot(414)
candlestick2_ohlc(ax, returns['PX_OPEN'], returns['PX_HIGH'], returns['PX_LOW'], returns['PX_LAST'], width=0.3)
xdate = returns.index

#ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

def mydate(x, pos) :
  try:
    return xdate[int(x)]
  except IndexError:
    return ''
    
ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))


plt.tight_layout()
plt.show()
