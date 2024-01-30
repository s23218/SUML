import os
import zipfile
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd

with open('symbols.txt', 'r') as file:
    data = file.read()
symbols = data.split()

print(symbols)
print(len(symbols))

yf.pdr_override()
stocks = [symbols]

all_data = pd.DataFrame()

for stock in symbols:
    data = pdr.get_data_yahoo(stock, start="2019-01-01", end="2024-01-15")
    data['Symbol'] = stock

    data.to_csv(f'{stock}_data.csv')


with zipfile.ZipFile('stocks_data.zip', 'w') as zipf:
    for stock in symbols:
        zipf.write(f'{stock}_data.csv')

for stock in symbols:
    os.remove(f'{stock}_data.csv')
