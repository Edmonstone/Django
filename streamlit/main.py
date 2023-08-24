import streamlit as st
import requests
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/django')
db = client['mongo_db']
collect = db['authtoken_token']

# Streamlit app setup
st.title("OAuth")
token_input = st.text_input("Enter Token")
submit_button = st.button("Submit")

if submit_button:
    # Django API endpoint for user validation
    django_api_url = "http://localhost:8000/users/"

    # Make a GET request to the Django API
    response = requests.get(django_api_url, headers={"Authorization": f"Token {token_input}"})

    if response.status_code == 200:
        st.success("Token is valid. Access granted.")
        # Your Streamlit app logic goes here
    else:
        st.error("Invalid token. Access denied.")
