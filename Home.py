import streamlit as st
from dotenv import load_dotenv

# Apply styles
with open('./styles/styles.css') as file:
    style = file.read()
    st.markdown(f"""<style>{style}</style>""", unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Youtube Blog", page_icon='🎥🔴')

    st.header("Youtube Blog Generator")

    # with st.form("my_form"):
    #     st.write("Inside the form")



if __name__ == '__main__':
    main()
