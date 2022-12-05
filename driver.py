from tkinter.tix import Tree
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
    return dataframe


# @st.cache(persist=True)
def raw_data_visual():
    data_df = dataset_reader(1000)
    if st.checkbox("DataFrame", False):
        st.snow()
        st.dataframe(data_df)
    

raw_data_visual()
    

