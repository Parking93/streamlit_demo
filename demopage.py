import streamlit as st
import os

st.set_page_config(initial_sidebar_state="collapsed")

st.page_link("demopage.py", label="Home", icon="🏠")

st.page_link("pages/untitled1.py", label="untitled1", icon="1️⃣")

st.page_link("pages/stockdashboard.py", label="stockdashboard", icon="📈")

st.page_link("https://titanic-dashboard.streamlit.app/", label="Google", icon="🌎")

