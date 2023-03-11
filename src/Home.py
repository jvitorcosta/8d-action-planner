import streamlit as st
from utils.content import disciplines_text

def main():
    st.set_page_config(
        page_title="Action Planner",
        page_icon="🎱"
    )

    st.markdown(
        "text goes here"
    )

    st.markdown(disciplines_text())

if __name__ == "__main__":
    main()