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


pip install yfinance


# In[ ]:


import yfinance as yf
import numpy as np

df = yf.download("^GSPC", start="2010-01-01")
returns = np.log(df["Close"]).diff().dropna()
df.head()


# In[ ]:


windows = [5, 21, 63]

for w in windows:
    df[f"vol_{w}"] = returns.rolling(w).std() * np.sqrt(252)

df[[f"vol_{w}" for w in windows]].plot(figsize=(10,5))
plt.title("Rolling Volatility")


# In[ ]:


(returns**2).plot(figsize=(10,4))
plt.title("Squared Returns")


# In[ ]:


from statsmodels.graphics.tsaplots import plot_acf
plot_acf(returns**2, lags=50)


# In[ ]:


forecast = returns.rolling(21).std().shift(1)
realized = returns.rolling(21).std()
import matplotlib.pyplot as plt
plt.plot(forecast, label="Forecast")
plt.plot(realized, label="Realized")
plt.legend()


# In[ ]:




