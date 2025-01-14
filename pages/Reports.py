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

col1, col2, col3 = st.columns([1,1,5])

with col1:
    st.title("Reports")
    st.write("")    
    if st.button("Account details", use_container_width=True):
        st.switch_page("pages/Enquiries.py")
    if st.button("Enquiries", use_container_width=True):
        st.switch_page("pages/Enquiries.py")
    if st.button("Contact", use_container_width=True):
        st.switch_page("pages/Enquiries.py")
    if st.button("Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")
    if st.button("Logout", use_container_width=True):
        st.switch_page("Login.py")
with col3:
    st.write("")
    st.write("")
    st.write("")
    st.title("")
    st.write("XDS is a company specializing in a range of data products designed to help businesses leverage their data for insights and decision-making. Their offerings include data analytics tools, data integration platforms, and business intelligence solutions that enable companies to streamline data management, improve operational efficiency, and drive growth. XDS’s products are built with advanced technologies to ensure scalability, security, and ease of use for organizations across various industries.")
