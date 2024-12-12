import streamlit as st
import requests

# Base URL of the Flask API
BASE_URL = "https://fad40a73e5ddd14d6adeb2520d9c1df3.serveo.net"

# Streamlit App
st.title("Flask API Client")
st.write("This is a Streamlit app to interact with the Flask API.")

# Option to fetch all data
if st.button("Fetch All Data"):
    response = requests.get(f"{BASE_URL}/data")
    if response.status_code == 200:
        data = response.json()
        st.write("Fetched Data:", data)
    else:
        st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")

# Input to fetch a specific entry by ID
st.subheader("Fetch Data by ID andre")
entry_id = st.number_input("Enter ID", min_value=1, step=1)
if st.button("Fetch by ID"):
    response = requests.get(f"{BASE_URL}/data/{entry_id}")
    if response.status_code == 200:
        entry = response.json()
        st.write("Fetched Entry:", entry)
    else:
        st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")

# Form to add a new entry
st.subheader("Add New Entry")
with st.form("add_entry_form"):
    new_id = st.number_input("ID", min_value=1, step=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add Entry")

    if submitted:
        new_entry = {
            "id": int(new_id),
            "name": name,
            "age": int(age),
            "email": email
        }
        response = requests.post(f"{BASE_URL}/data", json=new_entry)
        if response.status_code == 201:
            st.success("Entry added successfully!")
        else:
            st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
