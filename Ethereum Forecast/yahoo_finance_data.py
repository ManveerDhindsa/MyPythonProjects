import yfinance as yf
import csv
import numpy as np


eth_price = yf.Ticker("ETH-CAD")
hist = eth_price.history(period="max")
# hist.actions.to_csv("tickertag{}.csv".format('ETH-CAD'))

hist['Close'].to_csv("tickertagETH-CAD.csv", header = True)