import streamlit as st
import MAIN
import graphs

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css', encoding='utf-8') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.sidebar.header('Dashboard `Space Weather`')
st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('speed', 'longitude', 'latitude'))
st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.selectbox('Color by', ('speed', 'longitude + latitude + half angle'))
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

#row b
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    heatmap_figure = graphs.heat_map(MAIN.cme_df, time_hist_color)
    st.pyplot(heatmap_figure)  

with c2:
    st.markdown('### Donut chart')
    donut_figure = graphs.flr_class_dist(MAIN.flr_7)
    st.pyplot(donut_figure)  

# Row C
st.markdown('### Line chart')

halfangle_figure = graphs.ts_halfangle(MAIN.weekly_averages)
speed_figure = graphs.ts_speed(MAIN.weekly_averages)

if plot_data == 'speed':
    selected_figure = speed_figure
elif plot_data == 'longitude + latitude + half angle':
    selected_figure = halfangle_figure

st.pyplot(selected_figure)
