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

def pretty_number(value):
    sign = '-' if value < 0 else ''
    abs_value = abs(value)
    if abs_value < 1e3:
        return f'{sign}{abs_value:.2f}'
    elif 1e3 <= abs_value < 1e6:
        return f'{sign}{abs_value / 1e3:.2f}K'
    elif 1e6 <= abs_value < 1e9:
        return f'{sign}{abs_value / 1e6:.2f}M'
    elif 1e9 <= abs_value < 1e12:
        return f'{sign}{abs_value / 1e9:.2f}B'
    elif 1e12 <= abs_value < 1e15:
        return f'{sign}{abs_value / 1e12:.2f}T'
    else:
        return f'{sign}{abs_value:.2e}'

def pretty_currency(value):
    return f'${pretty_number(value)}'

# load dataframe
df = main()

# filter for 2023 onwards
df = df[df['date'] > '2023-01-01']

# title
st.title('Argentinean Crypto Ecosystem')

# KPIs
# st.dataframe(df)

# define columns
col1, col2 = st.columns(2)

# latest tvl
with col1:
    latest_tvl = df[ df['date'] == df['date'].max() ]['tvl'].sum()
    st.metric(label='Total Value Locked',value=pretty_currency(latest_tvl))

# quantity of protocols
    with col2:
        quantity_protocols = df['protocol'].nunique()
        st.metric(label='Protocols tracked',value=quantity_protocols)

#tvl chart
st.header('Argentinean Crypto Projects by Total Value Locked')
fig = px.area(df, x="date", y="tvl", color="protocol")
st.plotly_chart(fig, use_container_width=True)

# ecosystem landscape (figma embed)
figma_url = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fdesign%2FPUo88BOv4TnB6g5wvE7u3H%2FCrypto-Landscape-in-Argentina%3Fnode-id%3D0-1%26t%3DmtgupHxoF481CKB4-1"
components.iframe(figma_url, width=None, height=800, scrolling=False)
