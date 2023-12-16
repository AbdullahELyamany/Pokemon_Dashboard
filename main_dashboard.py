# importing Libraries
import streamlit as st
import pandas as pd
import numpy as npc
import plotly.express as px

st.set_page_config(
    page_title='Pokemon Dashboard',
    page_icon=None,
    layout="wide",
    initial_sidebar_state='auto',
)

# loading dara
df = pd.read_csv('Pokemon.csv')

# sidebar
st.sidebar.header("Pokemon Dashboard")
st.sidebar.image("pokemon.png")
st.sidebar.write("This Dashboard Is Using Pokemon Dataset frim Seaborn for Educational Purposes.\n")
st.sidebar.write("Filter Your Data:")

cat_filter = st.sidebar.selectbox("Categorical", [None, 'Legendary', 'Generation', 'Type 1', 'Type 2'])
num_filter = st.sidebar.selectbox("Numerical", [None, 'Total', 'Speed'])
row_filter = st.sidebar.selectbox("Row Filtering", [None, 'Legendary', 'Generation', 'Type 1', 'Type 2'])
col_filter = st.sidebar.selectbox("Column Filtering", [None, 'Legendary', 'Generation', 'Type 1', 'Type 2'])

st.sidebar.write("")
st.sidebar.markdown("Made With :sparkling_heart: By Eng: [Abdullah EL-Yamany](https://github.com/AbdullahELyamany)")

### body

# row 1
a1, a2, a3, a4 = st.columns(4)
a1.metric("Max Total", df['Total'].max())
a2.metric("Max Speed", df['Speed'].max())
a3.metric("Min Total", df['Total'].min())
a4.metric("Min Speed", df['Speed'].min())

# row 2

st.subheader('Total vs. Speed')
fig = px.scatter(
    data_frame=df,
    x = 'Total',
    y = 'Speed',
    color = cat_filter,
    size = num_filter,
    facet_col = col_filter,
    facet_row = row_filter
)

st.plotly_chart(fig, use_container_width=True)

# row 3

c1, c2, c3 = st.columns(3)
with c1:
    st.text("Generation vs Total")
    fig = px.bar(data_frame=df, x='Generation', y='Total', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.text("Legendary vs Speed")
    fig = px.pie(data_frame=df, names='Legendary', values='Speed', color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
with c3:
    st.text("Type1 vs Total")
    fig = px.pie(data_frame=df, names='Type 1', values='Total', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)