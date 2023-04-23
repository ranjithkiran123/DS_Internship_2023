import streamlit as st
import pandas as pd
import os

st.title('Pub Locations')


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA = os.path.join(dir_of_interest, "Data", "open_pubs_cleaned_data.csv")

df = pd.read_csv(DATA)

R1=st.radio('Search by',('Postal Code','Local Authority'))
if R1=='Postal Code':
    location=st.selectbox('Select the Postal Code',df['postcode'].unique())
    st.subheader(f"Total pubs found are {df[df['postcode']==location].shape[0]}")
    st.map(data=df[df['postcode']==location])
elif R1=='Local Authority':
    location1=st.selectbox('Select  Local Authority',df['local_authority'].unique())
    st.subheader(f"Total pubs found are {df[df['local_authority']==location1].shape[0]}")
    st.map(data=df[df['local_authority']==location1])