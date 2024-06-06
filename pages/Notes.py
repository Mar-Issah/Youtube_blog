import streamlit as st

with open('./data/notes.txt', 'r') as f:
	st.write(f.read())
