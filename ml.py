import streamlit as st
import joblib

# Create a list of options
options = ["Apple", "Banana", "Orange"]

# Create a dropdown with dynamic options
selected_option = st.selectbox("Select a fruit", options)

# Display the selected option
st.write("You selected:", selected_option)

# Load the model using joblib
loaded_model = joblib.load('decision_tree_model.joblib')
# Example usage: Make predictions with the loaded model
new_data = pd.DataFrame([[3, 25, 100,0]], columns=['Pclass', 'Age', 'Fare', 'Sex'])
#0 = female
#1 = male

new_data = pd.get_dummies(new_data, drop_first=True)
prediction = loaded_model.predict(new_data)

st.write("Prediction:", prediction)
