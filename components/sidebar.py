import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🤖 SmartHire Bot")

        st.markdown("---")

        st.subheader("✨ Features")

        st.success("📄 Resume Parsing")
        st.success("🎯 Semantic Job Matching")
        st.success("🤖 AI Resume Suggestions")
        st.success("💬 Career Mentor")

        st.markdown("---")

        st.subheader("⚙ Tech Stack")

        st.write("• Gemini 2.5 Flash")
        st.write("• Sentence Transformers")
        st.write("• FAISS")
        st.write("• Streamlit")

        st.markdown("---")

        st.caption("Version 1.0")