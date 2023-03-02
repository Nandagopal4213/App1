import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("D:\Python Recap\App1\images\photo.png",width=600)

with col2:
    st.title("Hari")
    content= """
    Hi, I'm Hari! I'm a python developer, student, and a traveller.I have worked as a freelancer for more than 3 years. I'm leaving a life that i wish to the fullest.
    """
    st.info(content)

content2 ="""
Below you can find some of the apps I have bulit in python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("D:\Python Recap\App1\images" + row["D:\Python Recap\App1\images"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("D:\Python Recap\App1\images" + row["D:\Python Recap\App1\images"])
        st.write(f"[Source Code]({row['url']})")
