from turtle import st
from typing import Sequence
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Load and draw the image with Streamlit
image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

# Display headers
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA.
""")
st.header('Enter DNA sequence')

# Create a text area
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

# Display the input and output
st.header('Input DNA sequence')
sequence

st.header('Output (DNA nucleotide count)')

# Print dictionary
st.subheader('1. Print dictionary')


# Count the nucleotide bases and store results in a dictionary
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

# Count the input sequence
X = DNA_nucleotide_count(sequence)

# The first way to display the dictionary infromation is by printing the raw dictionary
X

# The second way to display the dictionary information is by printing text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# The next way to display dictionary information is using a dataframe
st.subheader('3. Display DataFrame')
# create a dataframe from the dictionary and rename the column
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# Another way to display the dictionary information is using an Altair bar chart
st.subheader('4. Display DataFrame')
# create a chart from the dataframe
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    # Set the width of bars
    width=alt.Step(80)
)

st.write(p)