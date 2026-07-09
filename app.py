import streamlit as st
from PyPDF2 import PdfReader

# Import our parser module
from modules.parser import parse_resume

from modules.search import JobSearcher
from utils.helpers import build_search_query

from components.sidebar import show_sidebar
from components.resume_card import show_resume
from components.job_card import show_jobs
from components.tabs import create_tabs
from modules.suggestions import generate_suggestions
from components.suggestions_card import show_suggestions

st.set_page_config(
    page_title="SmartHire Bot",
    page_icon="📄",
    layout="wide"
)

show_sidebar()

st.title("📄 SmartHire Bot")
st.subheader("AI Resume Analyzer & Job Matcher")

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

    resume_tab, jobs_tab, text_tab, ai_tab, mentor_tab = create_tabs()

    with resume_tab:
        show_resume(profile)

    with jobs_tab:
        show_jobs(results)

    with ai_tab:

        st.subheader("🤖 AI Resume Suggestions")

        selected_job = results[0]

        if st.button("Generate Suggestions"):

            with st.spinner("Analyzing resume..."):

                suggestions = generate_suggestions(profile, selected_job)

            if suggestions is None:

                st.error("Unable to generate AI suggestions. Please check your Gemini API key or quota.")

            else:

                show_suggestions(suggestions)

    with mentor_tab:
        st.info("Coming in Module 5.4")
    

    with text_tab:

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            label="Resume Text",
            value=text,
            height=450
        )