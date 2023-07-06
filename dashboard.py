from operator import index
import streamlit as st

 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

cryptoDF = pd.json_normalize(data['data'])

df = pd.DataFrame(data=cryptoDF[['symbol','quote.USD.percent_change_24h']],index=cryptoDF['symbol'])

pd = pd.DataFrame(cryptoDF,columns=['symbol','quote.USD.percent_change_24h'])
pd.set_index('symbol',inplace=True)

st.write(cryptoDF)
st.write(pd)

st.bar_chart(pd)

st.sidebar.header('Filter')
coin = st.sidebar.multiselect(
     'What are your coins',
     cryptoDF['symbol'])

st.write("ok")