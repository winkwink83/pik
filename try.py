from binance import Client
import kody
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

client = Client(kody.apiKey,kody.apiSecurity)
print('logged in')

pd.DataFrame(client.get_historical_klines('BTCUSDT' , '1d', '30d'))
def getminutedata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol , interval, lookback))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    # frame.index = pd.to_datetime(frame.index, unit = 'ms')
    frame = frame.astype(float)
    return frame
test = getminutedata('BTCUSDT', '1h','10 day ago UTC')



n = 3  # number of points to be checked before and after

# Find local peaks
test['min'] = test.iloc[argrelextrema(test.Close.values, np.less_equal,order=n)[0]]['Close']
test['max'] = test.iloc[argrelextrema(test.Close.values, np.greater_equal,order=n)[0]]['Close']
pd.set_option('display.max_columns', None)
# print(test.index[0])
# print(test)


yy = []
xx = []
for mins in test['min']:
    if np.isnan(mins) == False:
        yy.append(mins)
        xx.append(test[test['min']==mins].index.values)
yymax = []
xxmax = []
for maxs in test['max']:
    if np.isnan(maxs) == False:
        yymax.append(maxs)
        xxmax.append(test[test['max']==maxs].index.values)

print(xx)
print(xx[0][0])

xes = []
for i in range(0,len(xx)):
    xes.append(xx[i][0])

xesmax = []
for i in range(0,len(xxmax)):
    xesmax.append(xxmax[i][0])




# pobrac minima z test[min] i zapisac je do array y nizej, a do array x zapisac liczby
# czasowe i sie wyswietli linia wsparcia
# Plot results
# print(test['min'][1])
plt.scatter(test.index, test['min'], c='r')
plt.scatter(test.index, test['max'], c='g')
plt.plot(test.get('Open'))



from scipy.stats import linregress

x = np.array(xes)
y = np.array(yy)
xma = np.array(xesmax)
yma = np.array(yymax)
slope, intercept, r_value, p_value, std_err = linregress(x, y)
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(xesmax, yma)
print("slope: %f, intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value ** 2)

print("slope1: %f, intercept1: %f" % (slope1, intercept1))
print("R-squared1: %f" % r_value1 ** 2)


plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line',color='blue')
plt.plot(xma, yma, 'o', label='original data')
plt.plot(xma, intercept1 + slope1 * xma, 'r', label='fitted line')
plt.legend()
plt.grid()
plt.show()


x = np.array([1,2,3,4,5,6,7,8,9])

y = np.array([1,2,3,4,5,6,7,8,9])
slope, intercept, r_value, p_value, std_err = linregress(x, y)
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line',color='blue')
plt.legend()
plt.grid()
plt.show()
print('psierwa')
print("slope: %f, intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value ** 2)

print(xes)
print(xesmax)