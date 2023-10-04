"""
Author: Jared Park
This streamlit page will compare national currencies
"""

import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
from currency_symbols import CurrencySymbols
from forex_python.converter import CurrencyRates

#-------------------------Function For Getting Historical Data---------------------------

#def get_history(base_currency:str, target_currency:str) -> pd.DataFrame:
#    """
#    This function takes in a base currency and target currency to get historic
#    data between the two currencies
#    """
#    start_date = datetime.today().date() - timedelta(days = 365)
#    end_date = datetime.today().date()
#    url = f'https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}'
#    params = {'base': base_currency}
#    request = requests.get(url, params)
#    data = request.json()


#    history = {}
#
#    for item in data['rates']:
#        
#        # data['rates'] gives the date for each rate
#        current_date = item
#        # data['rates']['date']['target_currency'] gives the exchange rate on that date
#        current_rate = data['rates'][item][target_currency]

        # In a dictionary [current_date] is the key word arg. current_rate is the arg
#        history[current_date] = current_rate

#    currencyDf = pd.DataFrame.from_dict(
#        history, 
 #       orient = 'index',
 #       columns = ['Convertion Rate'])

#    currencyDf.index.name = 'Time'

#    return currencyDf

#def average(Df: pd.DataFrame, column:str) -> float:
#    sum_elements = Df[column].sum()
#    avg = sum_elements / len(Df.index)
#    return avg

    
#--------------------------------Main UI Page-----------------------------------------



st.set_page_config(
    page_title = "Stock Info App (Currency)",
)

st.title("Currency Exchange Rates")

st.subheader("Look up the currency exchange rate between any two national currencies supported by **exchangerate.host**")

with st.form(key = 'my_form'):
    base_currency = st.text_input(
        label = "Base Currency",
        placeholder = "CAD",
    )
    target_currency = st.text_input(
        label = "Compared Currency",
        placeholder = "USD"
    )
    
    submit_button = st.form_submit_button(label = "Search")

    if submit_button:
        try:

            c = CurrencyRates()
            conversion = round(c.get_rate(base_currency, target_currency), 2)


            if CurrencySymbols.get_symbol(base_currency) == None or CurrencySymbols.get_symbol(target_currency) == None:
                raise ValueError("currency variables cannot have a currency symbol of None")
            
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            col1.metric(f"{base_currency}", f"{CurrencySymbols.get_symbol(base_currency)} 1")
            col2.metric(f"{target_currency}", f"{CurrencySymbols.get_symbol(target_currency)}{conversion}")

            #currencyDf = get_history(base_currency=base_currency, target_currency=target_currency)

            #plot = px.line(
            #currencyDf,
            #x = currencyDf.index,
            #y = 'Convertion Rate',
            #title = f"Historical Conversion Rates From {base_currency} To {target_currency} Over 1 Year"
            #)

            #st.plotly_chart(plot)

            #avg = round(average(currencyDf, 'Convertion Rate'), 2)
        

            #st.markdown(f"""
            #    - average conversion rate: ${avg} {target_currency} / {base_currency}
            #""")
        except TypeError:
            st.markdown("**Invalid** Currencies")
        except ValueError:
            st.markdown("**Invalid** Currencies")