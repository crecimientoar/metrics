import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from argentinian_tvl import main
import protocols.poap as poap
import protocols.decentraland as decentraland
import protocols.exactly as exactly

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
figma_url = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FPUo88BOv4TnB6g5wvE7u3H%2FCrypto-Landscape-in-Argentina%3Fpage-id%3D0%253A1%26node-id%3D1-2%26viewport%3D-39%252C-4%252C0.76%26t%3D1som4tZp4BQaRzYk-1%26scaling%3Dscale-down%26content-scaling%3Dfixed"

components.iframe(figma_url, width=None, height=800, scrolling=False)

# ecosystem directory

projects = pd.read_csv('Argentinean Crypto Projects.csv')

st.dataframe(
    projects,
    use_container_width=True,
    hide_index=True,
    column_order=['category', 'name', 'website'],
    column_config={
        'website': st.column_config.LinkColumn(
            display_text="https://(.*?)\/"
        )
    }
    )

#poap
st.header('POAP')
cola, colb, colc = st.columns(3)
with cola:
    st.metric(label='POAP Holders',value=pretty_number(poap.poap_holders()))

    st.write('POAP historic minters')
    hist_minters = pd.DataFrame(poap.poap_historic_minters())
    fig_a = px.line(hist_minters, x="time", y="minters")
    st.plotly_chart(fig_a, use_container_width=True)

with colb:
        st.metric(label='POAP Collections',value=pretty_number(poap.poap_collections()))
        
        st.write('POAP historic mints')
        hist_mints = pd.DataFrame(poap.poap_historic_minted())
        fig_b = px.line(hist_mints, x="time", y="amount")
        st.plotly_chart(fig_b, use_container_width=True)

with colc:
    st.metric(label='POAPs Minted',value=pretty_number(poap.poap_minted()))

    st.write('POAP historic collections')
    hist_collec = pd.DataFrame(poap.poap_historic_collections())
    fig_c = px.line(hist_collec, x="time", y="amount")
    st.plotly_chart(fig_c, use_container_width=True)

# Decentraland
st.header('DECENTRALAND')
cold, cole = st.columns(2)

with cold:
    st.metric(label='Holders',value=pretty_number(decentraland.main_stats()[0]))

with cole:
    st.metric(label='Collection Assets',value=pretty_number(decentraland.main_stats()[1]))

colf, colg, colh, coli = st.columns(4)
with colf:
    st.metric(label='7 Days Volume',value=pretty_number(decentraland.timeline_stats()[0]*1e3))

with colg:
    st.metric(label='All Time Volume',value=pretty_number(decentraland.timeline_stats()[1]*1e3))

with colh:
    st.metric(label='7 Days Sales',value=pretty_number(decentraland.timeline_stats()[2]))

with coli:
    st.metric(label='All Time Sales',value=pretty_number(decentraland.timeline_stats()[3]*1e3))

st.write('Historic trends')
historic_values = pd.DataFrame(decentraland.historic_floor_and_volumes())
colj, colk = st.columns(2)

with colj:
    df_volume = historic_values[['time', 'volume']]
    fig_a = px.line(df_volume, x="time", y="volume", title="Volume")
    st.plotly_chart(fig_a, use_container_width=True)

with colk:
    df_buyers = historic_values[['time', 'buyers']]
    fig_b = px.line(df_buyers, x="time", y="buyers", title="Buyers")
    st.plotly_chart(fig_b, use_container_width=True)

coll, colm = st.columns(2)

with coll:
    df_floor = historic_values[['time', 'floor']]
    fig_c = px.line(df_floor, x="time", y="floor", title="USD Floor Price")
    st.plotly_chart(fig_c, use_container_width=True)

with colm:
    df_floor_eth = historic_values[['time', 'floor_eth']]
    fig_d = px.line(df_floor_eth, x="time", y="floor_eth", title="Eth Floor Price")
    st.plotly_chart(fig_d, use_container_width=True)

# Exactly Finance
st.header('EXACTLY')
coln, colo, colp = st.columns(3)

with coln:
    st.metric(label='Total Tx',value=pretty_number(exactly.total_transactions()*1))

with colo:
    st.metric(label='Active Depositors',value=pretty_number(exactly.active_depositors()/1))

with colp:
    st.metric(label='Active Borrowers',value=pretty_number(exactly.active_borrowers()/1))

colq, colr = st.columns(2)
with colq:  
        st.write('Daily active users')
        daily_active_users = pd.DataFrame(exactly.daily_active_users())
        fig_b = px.line(daily_active_users, x="day", y="total")
        st.plotly_chart(fig_b, use_container_width=True)

with colr:     
        st.write('Total users')
        total_users = pd.DataFrame(exactly.total_users())
        # st.write("Columns in the dataframe: ", total_users.columns.tolist())
        fig_b = px.line(total_users, x="day", y="users")
        st.plotly_chart(fig_b, use_container_width=True)

cols, colt = st.columns(2)
with cols:  
        st.write('Historic depositors')
        historic_depositors = pd.DataFrame(exactly.historic_depositors())
        fig_b = px.line(historic_depositors, x="day", y="users")
        st.plotly_chart(fig_b, use_container_width=True)

with colt:  
        st.write('Historic borrowers')
        historic_borrowers = pd.DataFrame(exactly.historic_borrowers())
        fig_b = px.line(historic_borrowers, x="day", y="users")
        st.plotly_chart(fig_b, use_container_width=True)