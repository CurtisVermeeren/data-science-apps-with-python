# Before running this application build the penguins model using the 'penguins-model-building.py' script

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Print headers
st.write("""
# Penguin Prediction App

This app precitds the **Palmer Penguin** species!

Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collect user input into a dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

# Load data from a csv file or collect data from the sidebar 
if uploaded_file is not None:
    # Create a dataframe from a CSV file like penguins_example.csv
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        # Create selectors and sliders for all penguin properties
        island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
        sex = st.sidebar.selectbox('Sex', ('male', 'female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        # Create a dataframe with the collected data
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Combine user input features with entire penguins dataset.
penguins_raw = pd.read_csv('penguins_clean.csv')
# Remove the species column as it is the target
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

# Encoding of ordinal features
# Expecting multiple options for sex and island
encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1]

# Display user input features
st.subheader('User Input Features')

if uploaded_file is not None:
    st.write(df)
else: 
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Read saved classification model from penguins-model-building.py
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

# Display the results
st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)