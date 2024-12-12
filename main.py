import streamlit as st

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

# Define the sidebar navigation
def sidebar_navigation():
    with st.sidebar:
        st.header("Navigation")
        selected_page = st.radio("Go to:", ["Home", "About", "Settings"])
        return selected_page

# Define the content for each page
def home():
    st.title("Home")
    st.write("Welcome to the Home page!")

def about():
    st.title("About")
    st.write("This is the About page. Learn more about the application here.")

def settings():
    st.title("Settings")
    st.write("Adjust your preferences in the Settings page.")

# Main app logic
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    selected_page = sidebar_navigation()

    if selected_page == "Home":
        home()
    elif selected_page == "About":
        about()
    elif selected_page == "Settings":
        settings()
