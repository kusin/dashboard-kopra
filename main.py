# library ui-dashboard
import streamlit as st

# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard Kopra",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
    }
)

# container-header-fuild
with st.container():
	st.markdown("## Classification of copra types using ensemble learning algorithm")
	
    