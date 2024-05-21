import streamlit as st
import os

def main():
    st.sidebar.link_button("Logout 🔓", os.getenv("URL"))
    st.sidebar.link_button("Signup 🔓 ", "./signup.py")
    st.sidebar.link_button("Signin 🔑", "./signin.py")
    with st.expander("Blog Post Title"):
        st.write('''
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        ''')
        st.info("Youtube Title : ")

        st.info("Youtube Link : ")




if __name__ == '__main__':
    main()

