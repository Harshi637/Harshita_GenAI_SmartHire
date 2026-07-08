import streamlit as st
from PyPDF2 import PdfReader

# Import our parser module
from modules.parser import parse_resume

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

    # Parse the resume using Gemini
    profile = parse_resume(text)

    # Display structured JSON
    st.subheader("📋 Parsed Resume")

    st.json(profile)

    # Display original text
    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        label="Resume Text",
        value=text,
        height=350
    )