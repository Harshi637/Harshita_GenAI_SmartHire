import streamlit as st
from PyPDF2 import PdfReader

# Import our parser module
from modules.parser import parse_resume

from modules.search import JobSearcher
from utils.helpers import build_search_query

st.set_page_config(
    page_title="SmartHire Bot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 SmartHire Bot")
st.subheader("Resume Upload Module")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    st.success("Resume uploaded successfully!")

    with st.spinner("Parsing resume using Gemini..."):
        profile = parse_resume(text)
        searcher = JobSearcher()
        query = build_search_query(profile)
        results = searcher.search(query)

    # Display structured JSON
    st.subheader("📋 Parsed Resume")

    st.json(profile)
    st.subheader("🎯 Top Matching Jobs")

    for i, job in enumerate(results, start=1):

        with st.expander(f"{i}. {job['job_title']}"):

            st.write(f"**Company:** {job['company']}")
            st.write(f"**Location:** {job['job_location']}")
            st.write(f"**Type:** {job['job_type']}")

            st.write("**Skills:**")
            st.write(job["job_skills"])

            st.write("**Summary:**")
            st.write(job["job_summary"])

    # Display original text
    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        label="Resume Text",
        value=text,
        height=350
    )