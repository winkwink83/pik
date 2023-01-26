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
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit = 'ms')
    frame = frame.astype(float)
    return frame

test = getminutedata('BTCUSDT', '1m','1d')
# test1 = {'col1': ['1674422959', '1674682222'], 'col2': [22424, 22374]}
# df = pd.DataFrame(data=test1)
# df = df.set_index('col1')
# df.index = pd.to_datetime(df.index, unit = 's')
# plt.plot(test.get('Open'))
# plt.plot(df.get('col2'))
# plt.show()


# np.random.seed(0)
# rs = np.random.randn(200)
# xs = [0]
# for r in rs:
#     xs.append(xs[-1] * 0.9 + r)
# df = pd.DataFrame(xs, columns=['data'])

n = 5  # number of points to be checked before and after

# Find local peaks

test['min'] = test.iloc[argrelextrema(test.Open.values, np.less_equal,order=n)[0]]['Open']
test['max'] = test.iloc[argrelextrema(test.Open.values, np.greater_equal,order=n)[0]]['Open']

# Plot results

plt.scatter(test.index, test['min'], c='r')
plt.scatter(test.index, test['max'], c='g')
plt.plot(test.get('Open'))
plt.show()



