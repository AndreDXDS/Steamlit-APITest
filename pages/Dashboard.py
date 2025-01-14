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
    st.write("")
    if st.button("Reports", use_container_width=True):
        st.switch_page("pages/Reports.py")

with col4:
    st.write("")
    if st.button("Logout", use_container_width=True):
        st.switch_page("Login.py")

with st.container(border=True):
    col5, col6, col7, col8, col9, col10 = st.columns(6)
    
    with col5:
        st.selectbox("Cell Phones",("Yes","No"),index=None,placeholder="Please select to filter")
    with col6:
        st.selectbox("Home Phones",("Yes","No"),index=None,placeholder="Please select to filter")
    with col7:
        st.selectbox("Work Phones",("Yes","No"),index=None,placeholder="Please select to filter")
    with col8:
        st.selectbox("Qualifications Phones",("Yes","No"),index=None,placeholder="Please select to filter")
    with col9:
        st.selectbox("Debtors Phones",("Yes","No"),index=None,placeholder="Please select to filter")
    with col10:
        st.selectbox("Property Phones",("Yes","No"),index=None,placeholder="Please select to filter")

col11, col12, col13, col14, col15, col116 = st.columns(6)

with col11:
    st.metric(label="Universe", value="58 M", border=True)
with col12:
    st.metric(label="Cell Phone", value="19 M", border=True)
with col13:
    st.metric(label="Home Phone", value="19 M", border=True)
with col14:
    st.metric(label="Work Phone", value="19 M", border=True)
with col15:
    st.metric(label="Qualifications", value="5 M", border=True)
with col116:
    st.metric(label="Debtors", value="4 M", border=True)
