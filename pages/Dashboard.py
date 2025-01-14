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


col1, col2, col3 = st.columns(3)

with col1:
    st.title("XDS Universe")

with col3:
    if st.button("Reports"):
        st.write("Why hello there")







# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(label="Universe", value="58 M", border=True)
# with col2:
#     st.metric(label="Universe", value="58 M", border=True)
# with col3:
#     st.metric(label="Universe", value="58 M", border=True)
