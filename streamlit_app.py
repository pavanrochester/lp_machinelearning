import streamlit as st
import pandas as pd
st.title('🎈 App Name')
st.info('This is a machine learning app')
st.write('**Raw Data**')

df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df

st.write('**X**')
X=df.drop('Species',axis=1)
X
