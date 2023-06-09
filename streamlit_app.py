import streamlit as st
import pandas as pd
import numpy as np

def foo():
	print('bar')


st.set_page_config(layout='wide')
st.title('Streamlit Column Test with modified standard theme')
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

with col1:
	st.subheader("A wide column with a chart")
	st.line_chart(data)

with col2:
	st.subheader("A narrow column with the data")
	st.write(data) 
	st.slider('this is a slider', 0, 25, 50, 75, 100)
