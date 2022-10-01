import pandas as pd
import yfinance as yf
from prophet import Prophet
from matplotlib import pyplot as plt

# eth_price = yf.Ticker("ETH-CAD")
# hist = eth_price.history(period="max")

# df = pd.DataFrame(hist)
# df.iloc[:,3]

df = pd.read_csv('tickertagETH-CAD.csv')
df['cap'] = 10000
df['floor'] = 1

m = Prophet(growth = 'logistic', seasonality_mode="multiplicative")
m.fit(df)

future = m.make_future_dataframe(periods=365)
future['cap'] = 10000
future['floor'] = 1
future.tail()


forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
# fig2 = m.plot_components(forecast)
plt.show()