import streamlit as st
import Modules as md

st.set_page_config(layout="compact")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        visibility: hidden;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

md.login()
