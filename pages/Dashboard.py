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


col1, col2, col3 ,col4 = st.columns([2,4,1,1])

with col1:
    st.title("XDS Universe")

with col3:
    if st.button("Reports", use_container_width=True):
        st.switch_page("pages/Reports.py")

with col4:
    if st.button("Logout", use_container_width=True):
        st.switch_page("Login.py")

col5, col6, col7, col8, col9, col10 = st.columns(6)

with col5:
    st.metric(label="Universe", value="58 M", border=True)
with col6:
    st.metric(label="Universe", value="58 M", border=True)
with col7:
    st.metric(label="Universe", value="58 M", border=True)
with col8:
    st.metric(label="Universe", value="58 M", border=True)
with col9:
    st.metric(label="Universe", value="58 M", border=True)
with col10:
    st.metric(label="Universe", value="58 M", border=True)
