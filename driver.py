from cProfile import label

import streamlit as st 
import pandas as pd
import json


def main_page_info():
    st.header("Motor  Vehicle Collision Data Visual of Newyork.")
    st.markdown("This is streamlit dashboard for motor vehicle collision in Newyork City 🗽 ")

main_page_info()


def dataset_reader(nrows):
    dataframe = pd.read_csv('dataset.csv', nrows=nrows, parse_dates=[['CRASH DATE', 'CRASH TIME']])
    dataframe.dropna(subset=['LONGITUDE', 'LATITUDE'], inplace=True)
    lowercase = lambda x:str(x).lower().capitalize()
    dataframe.rename(lowercase, axis='columns', inplace=True)
    dataframe.rename(columns={'Crash date_crash time':'Data/Time'}, inplace=True)
    return dataframe


# @st.cache(persist=True)
def raw_data_visual():
    data_df = dataset_reader(100)
    if st.checkbox("DataFrame", False):
        st.dataframe(data_df)
    
raw_data_visual()



def data_map_visual():
    data_df = dataset_reader(1000)
    
    map_df = pd.DataFrame()
    map_df['longitude'] = data_df['Longitude']
    map_df['latitude'] = data_df['Latitude']
    map_df['Injured person'] = data_df['Number of persons injured']
    map_df['Injured person'] = map_df['Injured person']
    st.subheader("No of injured persons map visuals")
    person_injured = st.slider(" No of injured Persons", 1,20)
    
    df = map_df[(map_df["Injured person"] >= person_injured)]
    # st.snow()
    st.map(df)
data_map_visual()


    

