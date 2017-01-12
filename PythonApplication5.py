
from pandas.io.data import DataReader
from datetime import datetime
import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import pickle

spy= DataReader('spy',  'yahoo', datetime(2005, 1, 1), datetime(2016, 12, 23))
gld = DataReader('gld',  'yahoo', datetime(2005, 1, 1), datetime(2016, 12, 23))
gld_close= gld['Adj Close']
spy_close=spy['Adj Close']

#print([gld_close,spy_close])
spy_pct= (spy_close-spy_close [0])/spy_close[0]*100.0
gld_pct= (gld_close-gld_close [0])/gld_close[0]*100.0

#stk_correlation = gld_close.corr()
#print(stk_correlation)

#spy.plot()
#plt.legend().remove()
#plt.show()

spy_pct.plot()
gld_pct.plot()
plt.ylabel('Price (USD)')
plt.title('SPY vs GLD')
plt.legend()
plt.show()

