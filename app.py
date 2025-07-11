import requests
import pandas as pd
import plotly.graph_objs as go
import streamlit as st

# API Key
API_KEY = 'Your_AlphaVantage_API_Key'

# Streamlit UI
st.title('📈 Real-Time Stock Market Dashboard')
symbol = st.text_input("Enter Stock Symbol (e.g. AAPL, MSFT):", 'AAPL')

if st.button('Get Data'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if "Time Series (5min)" in data:
        df = pd.DataFrame.from_dict(data['Time Series (5min)'], orient='index')
        df = df.astype(float)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['1. open'], mode='lines+markers', name='Open Price'))
        st.plotly_chart(fig)
    else:
        st.error("Invalid Symbol or API Limit Reached. Try again later.")