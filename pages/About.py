"""
Author: Jared Park
This is the about page for the stock price app
"""

import streamlit as st

st.set_page_config(
    page_title = "Stock Info App (About)",
)

st.title("About")

st.markdown("""
    This streamlit stock price application was made using the [streamlit api](https://streamlit.io/), [pandas](https://pandas.pydata.org/), [plotly](https://plotly.com/), and the [yfinance api](https://pypi.org/project/yfinance/) written by Ran Aroussi.
    the yfinance api is a open source api that allows you to look up information about
    any ticker symbol that is recorded in their data base which include the opening price, closing price,
    volume, etc.

    The currency exchange rate app was also created using streamlit and [exchangerate.host](https://exchangerate.host/#/).
    exchangerate.host is a free open source api that allows you to gather current and historical data on the exchange rates
    of national currencies. The package used to get the currency symbols is [currency_symbols](https://pypi.org/project/currency-symbols/)
    written by Arshad Kazmi

    I hope you enjoy using this application 😊!
""")