import streamlit as st

st.set_page_config(layout="wide")
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
def refresh_state():
    st.session_state.refresh += 1
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
            st.session_state["selected_page"] = "AccountDetail"

        if st.button("Account Detail"):
            st.session_state["selected_page"] = "AccountDetail"

        if st.button("Contact"):
            st.session_state["selected_page"] = "Contact"

        if st.button("Enquiries"):
            st.session_state["selected_page"] = "Enquiries"

        if st.button("Logout"):
            st.session_state["selected_page"] = "Logout"        

        return st.session_state["selected_page"]

# Define the content for each page
def account_detail():
    st.title("Account Detail")
    
    # Input box for entering ID
    user_id = st.text_input("Enter ID:")

    # Simulated user data
    user_data = {
        "1": {"name": "John", "surname": "Doe", "email": "john.doe@example.com", "alive": True},
        "2": {"name": "Jane", "surname": "Smith", "email": "jane.smith@example.com", "alive": False},
    }

    if user_id:
        user_info = user_data.get(user_id, None)

        if user_info:
            st.write(f"**Name:** {user_info['name']}")
            st.write(f"**Surname:** {user_info['surname']}")
            st.write(f"**Email:** {user_info['email']}")
            st.write(f"**Alive:** {'Yes' if user_info['alive'] else 'No'}")
        else:
            st.error("No user found with this ID.")


def contact():
    st.title("Contact")
    st.write("This is the About page. Learn more about the application here.")

def enquiries():
    st.title("Enquiries")
    st.write("Adjust your preferences in the Settings page.")

# Main app logic
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

set_css()

if not st.session_state["authenticated"]:
    login()
else:
    selected_page = sidebar_navigation()

    if selected_page == "AccountDetail":
        account_detail()
    elif selected_page == "Contact":
        contact()
    elif selected_page == "Enquiries":
        enquiries()
    elif selected_page == "Logout":
        refresh_state()




