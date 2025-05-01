import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import plotly.express as px
import streamlit as st
import PIL.Image
import streamlit.components.v1 as components
import time


st.set_page_config('Sales_Homepage', page_icon= '🏠', layout= 'wide', initial_sidebar_state= 'collapsed', menu_items= {
    'Get help': 'https://www.bmts.ae/',
    'Report a bug': 'https://www.bmts.ae/',
    'About': 'BMTS Sales Dashboard'
    })








st.markdown("<h1 style= 'text-align: center; color: #2682B3; font-size: 60px'> BMTS HOME PAGE</h1>", unsafe_allow_html=True)

image= PIL.Image.open('/Users/anishmnair/Desktop/Streamlit/My_new_app/BMTS-APP/pages/Sales-Dashboard_image.jpg')

st.image(image, width= 500, output_format= 'auto', use_container_width= True)

col1, col2, col3, col4 = st.columns(4, border=False)

with col1:
    st.page_link('pages/Tickets-Dashboard.py', label= '''# **TICKETS DASHBOARD**''',  icon= '🎫', use_container_width= True)

with col2:
    st.page_link('pages/Monthly_sales.py', label= '''# **SALES DASHBOARD**''', icon= '📊', use_container_width= True)



