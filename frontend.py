import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
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

# load dataframe
df = main()

# filter for 2023 onwards
df = df[df['date'] > '2023-01-01']

# title
st.title('Argentinean Crypto Ecosystem')

#tvl chart
st.header('Argentinean Crypto Projects by Total Value Locked')
fig = px.area(df, x="date", y="tvl", color="protocol")
st.plotly_chart(fig, use_container_width=True)

# ecosystem landscape (figma embed)
figma_url = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fdesign%2FPUo88BOv4TnB6g5wvE7u3H%2FCrypto-Landscape-in-Argentina%3Fnode-id%3D0-1%26t%3DmtgupHxoF481CKB4-1"
components.iframe(figma_url, width=None, height=800, scrolling=False)