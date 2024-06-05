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

    st.markdown("<h3 style='text-align: center;'>Welcome to the AI-powered Youtube Blog Generator</h3>", unsafe_allow_html=True)

    with st.form("my_form"):
        st.write("To generate your blog post, simply enter the YouTube link below. Our form will extract the necessary details from the video to create a draft for your blog post. ")
        st.text_input("Enter YoutubeLink",
        key="link")
        st.form_submit_button('Generate', type='primary')

    #df = pd.read_csv('./data/population2023.csv')

    # query specifically for csv file takes the df as param
    #now that we have the query_engine we can nor run our query
    #query_engine = PandasQueryEngine(df=df, verbose=True)

    response = handle_csv('./data/population2023.csv')
    st.write(response)

if __name__ == '__main__':
    main()

