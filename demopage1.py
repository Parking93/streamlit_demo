import streamlit as st
import os
st.write(os.getcwd())
# st.set_page_config(initial_sidebar_state="collapsed")

st.page_link("demopage1.py", label="Home", icon="🏠")

# st.page_link("pages/untitled1.py", label="untitled1", icon="1️⃣")

# st.page_link("pages/stockdashboard.py", label="stockdashboard", icon="📈")

st.page_link("https://appdemo2-bkmdfjtjetu6dgtzjzixp7.streamlit.app/", label="Google", icon="🌎")

