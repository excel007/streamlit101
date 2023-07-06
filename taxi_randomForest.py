import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title("Welcome to NYC Taxi dataset project")
    st.write("We deep into the transaction of taxis in NYC")

with dataset:
    st.header("NYC Taxi dataset")
    st.text("you can find more information from https://data.cityofnewyork.us/Transportation/2018-Yellow-Taxi-Trip-Data/t29m-gskq")

    taxi_data = pd.read_csv('data/taxi_data.csv')
    st.write(taxi_data.head())
    st.subheader("Pick-up location ID distribution on the NYC dataset")
    pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts()).head(50)
    st.bar_chart(pulocation_dist)

with features:
    st.header("Features create")

    st.markdown('* **first feature:** I created this feature because..........')
    st.markdown('* **second feature:** I created this feature because..........')

with modelTraining:
    st.header("Time to train the model!!!!")
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes')
    
    sel_col , disp_col = st.columns(2)
    max_depth = sel_col.slider('What should be the max_depth of the model?',min_value=10,max_value=100,value=20,step=10)
    n_estimators = sel_col.selectbox('How many tree should there be?',options=[100,200,300,'No limit'],index=0)
    sel_col.text('Here is a list of features in my data: ')
    sel_col.write(taxi_data.columns)

    input_feature = sel_col.text_input('Which feature should be used as the input feature?','PULocationID')

    regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
    X = taxi_data[['PULocationID']]
    y = taxi_data[['PULocationID']]

    regr.fit(X,y)
    prediction = regr.predict(y)

    disp_col.subheader('Mean absolute error of the model is: ')
    disp_col.write(mean_absolute_error(y,prediction))

    disp_col.subheader('Mean square error of the model is: ')
    disp_col.write(mean_squared_error(y,prediction))

    disp_col.subheader('R square score of the model is: ')
    disp_col.write(r2_score(y,prediction))