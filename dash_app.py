"""
    Streamlit Dashboard App for Space Weather
    This script creates a Streamlit dashboard app for visualizing space weather data.
    Usage:
        Run this script using 'streamlit run dash_app.py' in the terminal.
    Author:
        Sander Belon
"""
import streamlit as st
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css', encoding='utf-8') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
import MAIN
import graphs
st.sidebar.header('Dashboard `Space Weather`')
st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('speed', 'longitude', 'latitude'))
st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('Class Type', 'x'))
st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.selectbox('Color by', ('speed', 'longitude + latitude + half angle'))
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)
st.sidebar.markdown('''
---
Template by [Data Professor](https://youtube.com/dataprofessor/).
''')
# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Solar Flare Duration", MAIN.flr_avrg_7, MAIN.duration_diff)
col2.metric("Solar Flare Count", MAIN.flr_count_7, MAIN.count_diff)
col3.metric("CME Speed", MAIN.cme_avrg_7, MAIN.speed_diff)
# Row B
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    graphs.heat_map(MAIN.cme_df)
with c2:
    st.markdown('### Donut chart')
    graphs.flr_class_dist(MAIN.flr_7)
# Row C
st.markdown('### Line chart')
graphs.ts_halfangle(MAIN.weekly_averages)
graphs.ts_speed(MAIN.weekly_averages)
