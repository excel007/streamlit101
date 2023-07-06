import streamlit as st
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Train the decision tree
tree = DecisionTreeClassifier()
tree.fit(X, y)

# Define the Streamlit app
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    # Use the trained decision tree to make predictions
    X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = tree.predict(X_new)
    species = data.target_names[prediction[0]]
    return species

st.title("Iris Species Prediction App")
st.markdown("Enter the following parameters to predict the species:")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0, 0.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0, 0.1)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0, 0.1)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0, 0.1)

if st.button("Predict"):
    species = predict_species(sepal_length, sepal_width, petal_length, petal_width)
    st.success(f"The predicted species is {species}.")
