import streamlit as st
import Modules as md

# Inject custom CSS for wide buttons
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

