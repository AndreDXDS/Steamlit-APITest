import streamlit as st
import Modules as md

# Inject custom CSS for wide buttons
def set_css():
    st.markdown(
        """
        <style>
        .stButton > button {
            width: 100%;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

md.login()
