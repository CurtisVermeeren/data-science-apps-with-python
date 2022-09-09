import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Print application headers
st.write("""
# Simple Iris Flow Prediciton App

The app predicts the type of an **Iris flower**
""")

# Create the sidebar for user inputs
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    # Create a dataframe for the sidebar input data
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

# Load the iris dataset from sklearn
iris = datasets.load_iris()
# iris.data is the 4 petal features (Petal and Sepal length and width)
X = iris.data 
# The names of the data classes (setosa, versicolour, virginica)
Y = iris.target

# Use a random forest classifier and apply the iris data to it.
clf = RandomForestClassifier()
clf.fit(X, Y)

# Create a prefiction using the classifier
prediction = clf.predict(df)
# prediciton probability is the chance that the predicition is correct 
prediction_proba = clf.predict_proba(df)

# Print the results of the prediction
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)