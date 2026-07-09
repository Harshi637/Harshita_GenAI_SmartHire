import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🤖 SmartHire Bot")

        st.markdown("---")

        st.success("✅ Resume Parser")

        st.success("✅ Semantic Search")

        st.info("🚧 Resume Suggestions")

        st.info("🚧 Career Mentor")

        st.markdown("---")

        st.caption("Version 1.0")