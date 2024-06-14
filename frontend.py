import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from argentinian_tvl import main

st.set_page_config(
    page_title="Crecimiento Research",
    page_icon="🇦🇷",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://t.me/+4hL7Vc7llSoxOWRk',
        'Report a bug': "https://t.me/+4hL7Vc7llSoxOWRk",
        'About': "# Argentinean Crypto Projects Analytics"
    }
)


st.title('Argentinean Crypto Projects Analytics')

df = main()
# st.dataframe(df,use_container_width=True)

df = df[df['date'] > '2023-01-01']

fig = px.area(df, x="date", y="tvl", color="protocol")
st.plotly_chart(fig, use_container_width=True)
