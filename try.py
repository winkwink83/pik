from binance import Client
import kody
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

client = Client(kody.apiKey,kody.apiSecurity)
print('logged in')

pd.DataFrame(client.get_historical_klines('BTCUSDT' , '1m', '30 m ago UTC'))
def getminutedata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol , interval, lookback+'m ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit = 'ms')
    frame = frame.astype(float)
    return frame
test = getminutedata('BTCUSDT', '720m','7200')

plt.plot(test.get('Open'))
plt.show()




