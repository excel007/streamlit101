import streamlit as st

import pandas as pd
import numpy as np

df = pd.DataFrame(
     np.random.randn(100, 2) / [50, 100] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

title = st.text_input('Movie title', 'Life of Briannn')
st.write('The current movie title is', title)