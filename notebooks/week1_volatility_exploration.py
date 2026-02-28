#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf

ticker = "AAPL"
data = yf.download(ticker, start="2023-01-01", end="2024-01-01")
close_prices = data['Close']

returns = close_prices.pct_change().dropna()

import numpy as np

vol_daily = returns.std()
vol_annual = vol_daily * np.sqrt(252)  # annualized
print("Annualized Volatility:", vol_annual)

rolling_vol = returns.rolling(window=21).std() * np.sqrt(252)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(close_prices, label='Price')
plt.title(f'{ticker} Price')
plt.show()

plt.figure(figsize=(12,6))
plt.plot(rolling_vol, label='Rolling Volatility')
plt.title(f'{ticker} 1-Month Rolling Volatility')
plt.show()


# In[ ]:


import yfinance as yf

ticker = "SPY"
data = yf.download(ticker, start="2023-01-01", end="2024-01-01")
close_prices = data['Close']

returns = close_prices.pct_change().dropna()

import numpy as np

vol_daily = returns.std()
vol_annual = vol_daily * np.sqrt(252)  # annualized
print("Annualized Volatility:", vol_annual)

rolling_vol = returns.rolling(window=21).std() * np.sqrt(252)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(close_prices, label='Price')
plt.title(f'{ticker} Price')
plt.show()

plt.figure(figsize=(12,6))
plt.plot(rolling_vol, label='Rolling Volatility')
plt.title(f'{ticker} 1-Month Rolling Volatility')
plt.show()


# In[ ]:




