# library ui-dashboard
import streamlit as st
from streamlit_extras import add_vertical_space as avs

# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# library data visualization
import plotly.express as px

# call method from other file
from class_dataset import dataset
from class_visualization import visualization

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard Kopra",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2023 all rights reserved by Aryajaya Alamsyah"
    })

# container-sidebar
with st.sidebar:    
    st.selectbox(
        "Choose a supervised learning algorithm",
        ("Use all algorithm", "K nearest-neighbor", "Suport Vector Machine", "Decision Tree (C45)", "Gaussian Naive Bayes", "Logistic Regression ", "Linear Discriminant Analysis", "Quadratic Discriminant Analysis")
    )
    st.selectbox(
        "Choose a ensemble learning algorithm",
        ("Use all algorithm", "Bagging", "AdaBoost", "Stacking", "Voting")
    )
    st.button("Submit", type="primary")
    st.write("<hr>", unsafe_allow_html=True)
    st.info("Created by Aryajaya Alamsyah, M.Kom")

# container-header
with st.container():
	st.markdown("## Classification of copra types using ensemble learning algorithm")

# container-dataset
with st.container():
    # show dataset of type copra
    st.text("Dataset of type copra")
    st.dataframe(data=np.round(dataset().get_dataset(),2), use_container_width=True, hide_index=True)

# container result-supervised
with st.container():
    # visualization supervised learning
    df_supervised = dataset.get_result_supervised()    
    st.plotly_chart(visualization.line_plot(df_supervised, "Accuracy of supervised learning"), use_container_width=True)

# container result-ensemble
with st.container():
    # visualization ensemble learning
    df_ensemble = dataset.get_result_ensemble()    
    st.plotly_chart(visualization.line_plot(df_ensemble, "Accuracy of ensemble learning"), use_container_width=True)

# container footer
with st.container():
    avs.add_vertical_space(2);
    st.text("Copyright all rights reserved 2023 by Aryajaya Alamsyah, M.Kom.");