import os
import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pandas_datareader import data as pdr
import psycopg2
import wandb
import yfinance as yf

def download(symbols):
    symbols = symbols

    symbols = symbols.split()

    yf.pdr_override()

    os.makedirs('stocks', exist_ok=True)
    for stock in symbols:
        data = pdr.get_data_yahoo(stock, start="2019-01-01", end="2024-01-15")
        data['Symbol'] = stock

        data.to_csv(f'stocks/{stock}_data.csv')




def preprocess_data(data_folder):
    project_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    data_folder = project_dir + data_folder


    dfs = []
    all_data = pd.DataFrame()
    for file_name in os.listdir(data_folder):
        if file_name.endswith("_data.csv"):
            file_path = os.path.join(data_folder, file_name)
            stock_data = pd.read_csv(file_path)
            dfs.append(stock_data)

    all_data = pd.concat(dfs, ignore_index=True)

    return all_data


def init_wandb(configg):
    wandb.init(
    project="suml",
    config=configg)


def split(all_data , random_state:int, constring):

    all_data['Open_tmr'] = all_data['Open'].shift(-1)
    all_data['Up'] = (all_data['Open_tmr'] - all_data['Close'] > 0).astype(int)

    features = all_data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)


    features_scaled = pd.DataFrame(features_scaled, columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

    labels = all_data['Up']

    X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.2, random_state=random_state)


    return X_train, X_test, y_train, y_test
