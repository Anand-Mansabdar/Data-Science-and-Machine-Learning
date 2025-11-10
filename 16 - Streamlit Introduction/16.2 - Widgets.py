import streamlit as st
import pandas as pd
import numpy as np

st.title('Widgets in Streamlit')

name = st.text_input('Enter your name: ')
age = st.slider('Enter your age: ', 0, 100, 0)

if name:
  st.write(f'Hello {name}!!!')
  
if age>0:
  st.write(f'Your age is {age}')
  

options = ['Javascript', 'Python', 'Java', 'C++', 'RubyOnRails']
choice = st.selectbox('Choose your favourite programming language:', options, index=None, placeholder='Select Language')
st.write(f'You selected {choice}')

uploaded_file = st.file_uploader('Choose a CSV file:', type='csv')

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)