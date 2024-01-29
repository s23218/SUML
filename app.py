import streamlit as st
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
import os
import urllib.request
import pickle
import pandas as pd

bootstrap_project(os.getcwd())
session = KedroSession.create()
urla = "http://127.0.0.1:8000/model_download"
model = pickle.load(urllib.request.urlopen(urla))
print(model)

st.write("Stocks pred")

if st.button("run pipeline"):
    session.run()    
    
if st.button("load new model"):
    model = pickle.load(urllib.request.urlopen(urla))

open = st.text_input("Open")
high = st.text_input("High")
low = st.text_input("Low")
close = st.text_input("close") 
adj_close = st.text_input("Adj_close") 
volume = st.text_input("Volume")

pred = None

if st.button("predict"):
    d = {"Open": [open], "High": [high], "Low": [low], "Close": [close], "Adj Close": [adj_close], "Volume": [volume]}
    df = pd.DataFrame(data=d)
    pred = model.predict(df)[0]
    if pred == 1:
        pred = "wzrosnie"
    if pred == 0:
        pred = "nie wzrosnie"
st.header(pred)