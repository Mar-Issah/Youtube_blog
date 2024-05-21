import streamlit as st


def main():
    with st.form("signin_form"):
        st.write("Sign in to your account")
        st.text_input("Enter Email", key="email")
        st.text_input("Enter Password", type="password", key="password")
        st.form_submit_button('Submit', type='primary')


if __name__ == '__main__':
    main()
