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


col1, col2, col3 ,col4 = st.columns([1,4,2,1])

with col1:
    st.title("XDS Universe")

with col3:
    if st.button("Reports"):
        st.switch_page("pages/Reports.py")

with col4:
    if st.button("Logout"):
        st.switch_page("Login.py")





# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(label="Universe", value="58 M", border=True)
# with col2:
#     st.metric(label="Universe", value="58 M", border=True)
# with col3:
#     st.metric(label="Universe", value="58 M", border=True)
