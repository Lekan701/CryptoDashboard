from os import read
import re
import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go
from PIL import Image

st.write("""
# Cryptocurrency Dashboard Application
Visually show data or crypto (BTC, ETH, LINK, ADA & VET) from **'2020-07-14' to '2021-07-14'**
""")
image = Image.open("E:/PythonProjectsDump/CryptoDashboard/StockImages/crypto_image1.jpg")
st.image(image, use_column_width=True)

st.sidebar.header("User Input")

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-07-14")
    end_date = st.sidebar.text_input("End Date", "2020-12-25")
    crypto_symbol = st.sidebar.text_input("Crypto Symbol", "BTC")
    return start_date, end_date, crypto_symbol

def get_crypto_name(symbol):
    symbol = symbol.upper()
    if symbol == "BTC":
        return "Bitcoin"
    elif symbol == "ETH":
        return "Ethereum"
    elif symbol == "ADA":
        return "Cardano"
    elif symbol == "LINK":
        return "Link"
    elif symbol == "VET":
        return "VeChain"
    else:
        return "None"

def get_data(symbol, start, end):
    symbol = symbol.upper()
    if symbol == "BTC":
        df = pd.read_csv("E:/PythonProjectsDump/CryptoDashboard/CryptoCSV/BTC-GBP.csv")
    elif symbol == "ETH":
        df = pd.read_csv("E:/PythonProjectsDump/CryptoDashboard/CryptoCSV/ETH-GBP.csv")
    elif symbol == "ADA":
        df = pd.read_csv("E:/PythonProjectsDump/CryptoDashboard/CryptoCSV/ADA-GBP.csv")
    elif symbol == "LINK":
        df = pd.read_csv("E:/PythonProjectsDump/CryptoDashboard/CryptoCSV/LINK-GBP.csv")
    elif symbol == "VET":
        df = pd.read_csv("E:/PythonProjectsDump/CryptoDashboard/CryptoCSV/VET-GBP.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.loc[start:end]

start, end, symbol = get_input()
df = get_data(symbol, start, end)
crypto_name = get_crypto_name(symbol)

fig = go.Figure(
    data = [go.Candlestick(
        x = df.index,
        open = df['Open'],
        high = df['High'],
        low = df['Low'],
        close = df['Close'],
        increasing_line_color = 'green',
        decreasing_line_color = 'red'
    )
    ]
)

st.header(crypto_name+" Data")
st.write(df)

st.header(crypto_name + " Data Statistics")
st.write(df.describe())

st.header(crypto_name + " Close Price")
st.line_chart(df['Close'])

st.header(crypto_name + " Volume")
st.bar_chart(df['Volume'])

st.header(crypto_name + " Candle stick")
st.plotly_chart(fig)