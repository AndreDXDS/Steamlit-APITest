import streamlit as st

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

# Define a function to display the login screen
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state["authenticated"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# Define the sidebar navigation with static buttons
def sidebar_navigation():
    with st.sidebar:
        st.header("Navigation")

        if "selected_page" not in st.session_state:
            st.session_state["selected_page"] = "Account Detail"

        if st.button("Home"):
            st.session_state["selected_page"] = "Home"

        if st.button("Contact"):
            st.session_state["selected_page"] = "About"

        if st.button("Enquiries"):
            st.session_state["selected_page"] = "Settings"

        return st.session_state["selected_page"]

# Define the content for each page
def account_detail():
    st.title("Home")
    st.write("Welcome to the Home page!")

def contact():
    st.title("About")
    st.write("This is the About page. Learn more about the application here.")

def enquiries():
    st.title("Settings")
    st.write("Adjust your preferences in the Settings page.")

# Main app logic
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

set_css()

if not st.session_state["authenticated"]:
    login()
else:
    selected_page = sidebar_navigation()

    if selected_page == "Home":
        account_detail()
    elif selected_page == "About":
        contact()
    elif selected_page == "Settings":
        enquiries()
