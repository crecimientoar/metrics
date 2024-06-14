import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import argentinian_tvl as tvl

st.set_page_config(
    page_title="Crecimiento Research",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

df = tvl

st.dataframe(df)

st.line_chart(np.random.randn(30, 3))
