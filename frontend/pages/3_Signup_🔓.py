import streamlit as st
import os
import requests

def handle_click(username, email, password):
    BASE_URL = os.getenv("API_URL")
    print(username, email, password)

    if not username or not email or not password:
        st.warning("Please fill in all fields")
    else:
        response = requests.post(f'{BASE_URL}/signup', json={username: username, email: email, password: password})
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print('POST request was successful!')
            print('Response:', response.json())
        else:
            print('POST request failed with status code:', response.status_code)



def main():
    with st.form("signup_form"):
        st.write("Create an account")
        username =st.text_input("Enter Full Name", key="name")
        email = st.text_input("Enter Email", key="email")
        password = st.text_input("Enter Password", type="password", key="password")
        password2 = st.text_input("Repeat Password", type="password", key="password2")

        if password != password2:
            st.warning("Passwords do not match")
        st.form_submit_button('Submit', type='primary', on_click=handle_click(username, email, password))


if __name__ == '__main__':
    main()
