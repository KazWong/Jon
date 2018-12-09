import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

returns = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0)
returns.plot()
plt.title('Stock Data')
plt.xlabel('Time')
plt.legend(loc=0)

prices = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0, usecols="A,B,C,D,E")
prices.plot()
plt.title('Prices')
plt.xlabel('Time')
plt.legend(loc=0)

bb = pd.read_excel('stock_data.xlsx', sheet_name=2, index_col=0, usecols="A,B,E,M,N,O")
bb.plot()
plt.title('BB')
plt.xlabel('Time')
plt.legend(loc=0)


plt.show();
