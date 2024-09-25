import streamlit as st
import pandas as pd
st.title('🎈 App Name')
st.info('This is a machine learning app')
st.write('**Raw Data**')


with st.expander('Data'):
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  
  st.write('**X**')
  X=df.drop('species',axis=1)
  X
  
  st.write('**Y**')
  Y=df.species
  Y

with st.expander('data Visualisation'):
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')


#data prep
with st.sidebar:
  st.header('Input features')
  island=st.selectbox('island',('Biscoe','Dream','Torgersen'))
  gender=st.selectbox('gender',('male','female'))
  
  
