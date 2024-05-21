import streamlit as st
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    st.set_page_config(page_title="Youtube Blog", page_icon='🎥🔴', layout="centered")

    st.sidebar.link_button("Logout 🔓", os.getenv("URL"))
    st.sidebar.link_button("Signup 🔓 ", "./signup.py")
    st.sidebar.link_button("Signin 🔑", "./signin.py")

    # Apply styles
    # with open('./styles/styles.css') as file:
    #     style = file.read()
    #     st.markdown(f"""<style>{style}</style>""", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>Welcome to the AI-powered Youtube Blog Generator</h3>", unsafe_allow_html=True)

    with st.form("my_form"):
        st.write("To generate your blog post, simply enter the YouTube link below. Our form will extract the necessary details from the video to create a draft for your blog post. ")
        st.text_input("Enter YoutubeLink",
        key="link")
        st.form_submit_button('Generate', type='primary')


if __name__ == '__main__':
    main()

