import streamlit as st
from dotenv import load_dotenv
#from population_engine import agent

def main():
    load_dotenv()
    st.set_page_config(page_title="AI Agent", page_icon='🤖💬', layout="centered")

    st.markdown("<h3 style='text-align: center;'>Welcome to the AI-Agent</h3>", unsafe_allow_html=True)

    with st.form("my_form"):
        st.write("This AI Agent is a versatile Python application designed to efficiently handle queries and lookout for relevant information from diverse data sources, including CSV files and PDF documents. You can ask questions about Africa, world population, and also save the answers in a .txt file.")
        query = st.text_input("Enter Query")
        submit = st.form_submit_button('Generate', type='primary')

    if submit:
        # response = agent.query(query)
        st.write("response")


if __name__ == '__main__':
    main()

