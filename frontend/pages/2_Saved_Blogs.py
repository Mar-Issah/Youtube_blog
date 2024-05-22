import streamlit as st
import os

def main():
    st.sidebar.markdown("<div style='margin-top: 20rem;'></div>", unsafe_allow_html=True)
    if st.sidebar.button("Logout 🔓"):
        st.switch_page("Home.py")

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

