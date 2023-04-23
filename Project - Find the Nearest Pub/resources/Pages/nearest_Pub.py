import streamlit as st
import pandas as pd
import numpy as np
import os

st.title('Find the nearest pubs')

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA = os.path.join(dir_of_interest, "data", "open_pubs_cleaned_data.csv")

df = pd.read_csv(DATA)

lat=st.number_input(label="Enter the Latitude")
lon=st.number_input(label="Enter the Longitude")

def euc_dis(lat1,lon1,lat2,lon2):
    return np.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

df['dist']=df.apply(lambda row: euc_dis(row['latitude'],row['longitude'],lat,lon),axis=1)
distance=df.sort_values(by='dist')[:5]
st.subheader('5 nearest pubs')
st.dataframe(distance)
st.map(data=distance)