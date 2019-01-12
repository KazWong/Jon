import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import datetime as datetime
from mpl_finance import candlestick2_ohlc

returns = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0)
date = pd.read_excel('stock_data.xlsx', sheet_name=2)


plt.figure(1)

#print(date)

def trading_system(score) :
  dmi_plus = returns['DMI_PLUS']
  dmi_minus = returns['DMI_MINUS']
  px_last = returns['PX_LAST']
  bb_ma = returns['BB_MA']
  macd_diff = returns['MACD_DIFF']
  trender_up = returns['TRENDER_UP']
  trender_down = returns['TRENDER_DN']
  tas_k = returns['TAS_K']
  tas_d = returns['TAS_D']
  ema_5 = returns['EMA(5)']
  ema_20 = returns['EMA(20)']
  
  for i in range(360) :
    score.append(0)
    if (dmi_plus[i] > dmi_minus[i]) :
      score[i] += 1
    elif (dmi_plus[i] < dmi_minus[i]) :
      score[i] -= 1
    if (px_last[i] > bb_ma[i]) :
      score[i] += 1
    elif (px_last[i] < bb_ma[i]) :
      score[i] -= 1
    if (macd_diff[i] > 0) :
      score[i] += 2
    elif (macd_diff[i] < 0) :
      score[i] -= 2
    if (trender_up[i] == "#N/A N/A") :
      score[i] += 1
    if (trender_down[i] == "#N/A N/A") :
      score[i] -= 1
    if (tas_k[i] > tas_d[i]) :
      score[i] += 1
    elif (tas_k[i] < tas_d[i]) :
      score[i] -= 1
    if (ema_5[i] > ema_20[i]) :
      score[i] += 1
    elif (ema_5[i] > ema_20[i]) :
      score[i] -= 1


plt.subplot(211)
#returns.plot()
plt.title('Stock Data')
plt.xlabel('Time')
plt.legend(loc=0)
score = []
trading_system(score)
plt.plot(score)

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

ax = plt.subplot(212)
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
