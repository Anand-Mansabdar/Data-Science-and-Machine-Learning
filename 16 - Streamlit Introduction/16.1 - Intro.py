import streamlit as st
import pandas as pd
import numpy as np

# Streamlit is an open source app framework for ML and Data Science Projects. It allows us to create UI for web apps with simple Python Scripts

# Title/Heading of the page
st.title('Hello from Streamlit')

# Displaying text
st.write('This is a simple text')

# Displaying a dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 5],
  'second column': [11, 22, 33, 44, 55]
})

st.write('The following is a dataframe')
st.write(df)

# Creating a line chart
chart_data = pd.DataFrame(
  np.random.randn(20, 3), columns=['a', 'b', 'c']
)

st.line_chart(chart_data)