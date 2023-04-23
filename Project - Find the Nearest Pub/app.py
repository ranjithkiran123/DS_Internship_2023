import streamlit as st
import pandas as pd
import os
from PIL import Image

st.title('''Welcome  to Open-Pub ''')
st.image('pubimg.png')
uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "data_dictionary.xlsx"


df = pd.read_csv("open_pubs_cleaned_data.csv")

st.text('''Let’s assume you are on a Vacation in the United Kingdom with your friends. Just for 
some fun, you decided to go to the Pubs nearby for some drinks. Google Map 
is down because of some issues. 
While searching the internet, you came across https://www.getthedata.com/open-pubs. 
On this website, you found all the pub locations (Specifically Latitude 
and Longitude info). 
In order to impress your friends, you decided to create a Web Application 
with the data available in your hand. 
''')

st.image('pubimg.png')

st.header('DATA INFORMATION')
st.subheader("Data")
st.dataframe(df)

ds = pd.read_excel("data_dictionary.xlsx")
st.dataframe(ds)


st.header("DATA DESCRIPTION:")
x = df.describe()
x