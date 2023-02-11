from binance import Client
import kody
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

client = Client(kody.apiKey,kody.apiSecurity)
print('logged in')

pd.DataFrame(client.get_historical_klines('BTCUSDT' , '1m', '30 m ago UTC'))
def getminutedata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol , interval, lookback))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Open')
    # frame.index = pd.to_datetime(frame.index, unit = 'ms')
    frame = frame.astype(float)
    return frame
test = getminutedata('BTCUSDT', '1h','1d')

pd.set_option('display.max_rows', None)

n = 1  # number of points to be checked before and after

# Find local peaks
test['min'] = test.iloc[argrelextrema(test.Close.values, np.less_equal,order=n)[0]]['Close']
test['max'] = test.iloc[argrelextrema(test.Close.values, np.greater_equal,order=n)[0]]['Close']

# print(type(int(test['Volume']['22895.82000000'])))
# x = []
# pobrac minima z test[min] i zapisac je do array y nizej, a do array x zapisac liczby
# czasowe i sie wyswietli linia wsparcia
# Plot results

plt.scatter(test.index, test['min'], c='r')
plt.scatter(test.index, test['max'], c='g')
plt.plot(test.get('Close'))
plt.show()

from scipy.stats import linregress

x = np.array([2, 7,8,9,10])
y = np.array([5, 6,7,8,15])
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print("slope: %f, intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value ** 2)


plt.figure(figsize=(15, 5))
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line')
plt.legend()
plt.grid()
plt.show()

