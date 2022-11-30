"""
Author: Jared Park
This streamlit application will allow the users to veiw stock prices and historical data plots
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def average(tickerDf:pd.DataFrame, column:str) -> float:
    """
    This function will will the average value of any column of the input pandas
    dataframe.

    Example: >>> average(pd.DataFrame({'row1': [1,2,3,4]}), 'row1')
    >>> 5/2
    """
    sum_of_column = tickerDf[column].sum()
    avg = sum_of_column / len(tickerDf.index)
    return avg

st.set_page_config(
    page_title = "Stock Info App (Home)",
)

st.title("Stock Prices App")
st.subheader("Streamlit App By: Jared Park")
st.subheader("Search up a company by ticker symbol or company name to get the stock price and other info supported by **yfinance**")

with st.sidebar:
    plot = st.multiselect(
        "Stock Statistics Options",
        ["Open", "Close", "High", "Low", "Volume"]
    )

with st.form(key = 'my_form'):
    user_input = st.text_input(
        label = "Search Ticker Symbol",
        placeholder = "AAPL",
    )
    submit_button = st.form_submit_button(label = "Search")

    
try:
    tickerData = yf.Ticker(user_input)
    tickerName = tickerData.info['longName']
    currentMarketPrice = tickerData.info['regularMarketPrice']
    previousClosingPrice = tickerData.info['regularMarketPreviousClose']
    deltaPrice = ((currentMarketPrice - previousClosingPrice)/previousClosingPrice) * 100
    tickerDf = pd.DataFrame(tickerData.history(
        period = '1y', 
        start = datetime.today().date() - timedelta(days = 365),
        end = datetime.today().date()))

    st.subheader(tickerName)

    col1, col2 = st.columns(2)

    col1.metric("Previous Closing Price", previousClosingPrice)
    col2.metric("Current Market Price", currentMarketPrice, f"{float(round(deltaPrice, 2))}%")

    for i in range(len(plot)):
        plt = px.line(
            tickerDf,
            x = tickerDf.index,
            y = plot[i],
            labels = {
                plot[i]: f"{plot[i]} Price ($)"
            },
            title = f"{plot[i]} prices over the course of one year"
        )

        st.plotly_chart(plt)

        st.markdown(f"""
        - The average **{plot[i]}** price over the past year is ${round(average(tickerDf, plot[i]), 2)}
        """)
        st.markdown("---")
except KeyError:
    if user_input == "":
       st.markdown("Enter a **ticker symbol**") 
    else:
        st.markdown("This is an **Invalid** ticker")