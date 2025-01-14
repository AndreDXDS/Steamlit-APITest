import streamlit as st
import Modules as md

st.set_page_config(layout="wide")

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

st.title("XDS Universe")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Universe", value="58 M", border=True)

