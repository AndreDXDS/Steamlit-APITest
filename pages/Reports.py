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

col1, col2 = st.columns([1,4])

with col1:
    st.title("Reports")
    
    if st.button("Account details", use_container_width=True):
        st.switch_page("pages/Enquiries.py")
    if st.button("Enquiries", use_container_width=True):
        st.switch_page("pages/Enquiries.py")
    if st.button("Contact", use_container_width=True):
        st.switch_page("pages/Enquiries.py")
with col2:
    st.write("")
    st.write("")
    st.write("")
    st.title("Enquiries")
