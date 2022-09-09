# This file is used for building the Penguins model before running the penguin-app

import pandas as pd

penguins = pd.read_csv('penguins_clean.csv')

# Ordinal feature encoding
df = penguins.copy()
# The target prediction is the species of the penguin
target = 'species'
# USe the sex and island of the penguin as input
encode = ['sex', 'island']

# Encode the columns
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

# Encode the target
target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# Separating X and Y
# X is the input features
# Y is the species
X = df.drop('species', axis=1)
Y = df['species']

# Build random forest model
from sklearn.ensemble import RandomForestClassifier
# Use the random forest classifier and build the model using the X and Y data
clf = RandomForestClassifier()
clf.fit(X, Y)

# Saving the model
import pickle
pickle.dump(clf, open('penguins_clf.pkl', 'wb'))