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
  bill_length_mm=st.slider('Bill length(mm)',32.1,59.6,43.9)
  bill_depth_mm=st.slider('Bill depth(mm)',13.1,21.5,17.2)
  flipper_length_mm=st.slider('Flipper length(mm)',172.0,231.0,201.0)
  body_mass_g=st.slider('Body mass(g)',2700.0,6300.0,4207.0)


#creating data frame for the input features
date={'island':island,
      'gender':gender,
      'bill_length_mm': bill_length_mm,
      'bill_depth_mm':bill_depth_mm,
      'flipper_length_mm':flipper_length_mm,
      'body_mass_g':body_mass_g}
input_df=pd.Dataframe(data,index=[0])
input_df
      
  
  
  
