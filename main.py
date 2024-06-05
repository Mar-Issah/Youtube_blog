import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
# from collections.abc import Mapping, MutableMapping
#from llama_index.core.query_engine import PandasQueryEngine
from utils import handle_csv


#https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/


def main():
    load_dotenv()
    st.set_page_config(page_title="AI Agent", page_icon='🤖💬', layout="centered")

    # st.sidebar.markdown("<div style='margin-top: 20rem;'></div>", unsafe_allow_html=True)
    # if st.sidebar.button("Logout 🔓"):
    #     st.switch_page("Home.py")

    st.markdown("<h3 style='text-align: center;'>Welcome to the AI-Agent</h3>", unsafe_allow_html=True)

    with st.form("my_form"):
        st.write("This AI Agent is a versatile Python application designed to efficiently handle queries and lookout for relevant information from diverse data sources, including CSV files and PDF documents.")
        query = st.text_input("Enter Query")
        submit = st.form_submit_button('Generate', type='primary')

    if submit:
        response = handle_csv('./data/population2023.csv', query)
        st.write(response)


if __name__ == '__main__':
    main()

