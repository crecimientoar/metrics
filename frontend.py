import pandas as pd
import streamlit as st

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

st.write('hello world')

st.write(df)

st.line_chart(np.random.randn(30, 3))
