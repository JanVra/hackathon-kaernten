import streamlit as st
import pandas as pd
import requests
import plotly.express as px 

def do_inference():
    pass
    
with st.form("student"):
    bi = st.number_input("Business_Intelligence", min_value=1, max_value=5)
    sm = st.number_input("Statistik_und_Mathematik", min_value=1, max_value=5)
    ii = st.number_input("Informatik_und_Infrastruktur", min_value=1, max_value=5)
    st.form_submit_button("go")

with st.expander("1"):
    bi, sm, ii
df = pd.read_csv("data/sd_kats.csv")
df

fig = px.histogram(df, barmode="group")
st.plotly_chart(fig)