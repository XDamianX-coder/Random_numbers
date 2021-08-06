######################
# Import libraries
######################
import numpy as np
import streamlit as st
import time
import pandas as pd



######################
# Page Title
######################

st.write("""
# Random values web app\n
Author: **Damian Nowak**
""")

######################
# Input numbers (Side Panel)
######################

st.sidebar.header('User Input Features')

## Read numbers input
number1_input = int(1)
number2_input = int(2233)
number3_input = int(45)

number1 = st.sidebar.text_area("Lower limit.", number1_input)
number2 = st.sidebar.text_area("Upper limit.", number2_input)
number3 = st.sidebar.text_area("Number of draws.", number3_input)


st.header('Input numbers.')
number1
number2
number3
time.sleep(0.1)
## Shows the result
st.header('Drawn numbers.')
#X = np.array([number1,number2,number3]).astype(np.int)
#X = np.random.randint(X)
baseData = np.random.randint(int(number1),int(number2),int(number3))
columnNames = ["Your values"]
dataframe = pd.DataFrame(data=baseData, columns=columnNames)

dataframe





