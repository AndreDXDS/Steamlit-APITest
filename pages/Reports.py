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

col1, col2 = st.columns([1,5])

with col1:
    with st.container(border=True):
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
with col2:
    with st.container(border=True):
        st.write("")
        st.write("")
        st.title("")
        st.write("XDS is a company specializing in a range of data products designed to help businesses leverage their data for insights and decision-making. Their offerings include data analytics tools, data integration platforms, and business intelligence solutions that enable companies to streamline data management, improve operational efficiency, and drive growth. XDS’s products are built with advanced technologies to ensure scalability, security, and ease of use for organizations across various industries.")
        st.write("XDS is taking its technology to the next level by integrating advanced cloud solutions into its data products. By leveraging cloud technology, XDS enhances scalability, flexibility, and performance, allowing businesses to access and manage their data more efficiently than ever before. Cloud-based features enable real-time analytics, seamless collaboration, and secure storage, empowering companies to make faster, data-driven decisions. This shift to the cloud ensures that XDS customers can easily scale their operations and stay ahead in an increasingly data-driven world.")
