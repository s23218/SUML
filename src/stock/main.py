import os
import sys
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def preprocess_data(data_folder):
    """merge the csv and scale the data, returning train/test split data"""
    dfs = []
    all_data = pd.DataFrame()

    for file_name in os.listdir(data_folder):
        if file_name.endswith("_data.csv"):
            file_path = os.path.join(data_folder, file_name)
            stock_data = pd.read_csv(file_path)
            dfs.append(stock_data)

    all_data = pd.concat(dfs, ignore_index=True)

    all_data['Up'] = (all_data['Close'] - all_data['Open'] > 0).astype(int)

    features = all_data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    labels = all_data['Up']

    X_train, X_test, y_train, y_test = train_test_split(features_scaled,
                                                        labels, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def build_model(X_train, X_test, y_train, y_test):
    """build a logistic regression model"""
    model = LogisticRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy}")

    conf_matrix = confusion_matrix(y_test, predictions)
    print(f"Confusion Matrix:\n{conf_matrix}")

    return model

project_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
data_folder = project_dir + '/data'

X_train, X_test, y_train, y_test = preprocess_data(data_folder)

model = build_model(X_train, X_test, y_train, y_test)

with open(project_dir + '/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
